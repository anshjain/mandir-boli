"""
Jain Calendar views integrated into mandir-boli Django project.
Ported from the standalone Flask jain_calendar app.
"""
from __future__ import annotations

import calendar
import json
import os
from datetime import date, datetime
from typing import Any

from django.http import JsonResponse
from datetime import date as _date_cls
from django.shortcuts import redirect, render

from mandir.kalyanaks import (
    FESTIVALS_2026,
    KALYANAKS_2026,
    PARV_TITHIS_2026,
    TIRTHANKARS_INFO,
    format_kalyanak,
    sun_times_for_date,
    tithi_for_date,
)

SUBSCRIPTIONS_FILE = os.path.join(os.path.dirname(__file__), 'jain_subscriptions.json')

MONTH_NAMES = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

SUPPORTED_YEAR = 2026


def parse_date(s: str) -> date:
    return datetime.strptime(s, "%d-%m-%Y").date()


def fmt_date(d: date) -> str:
    return d.strftime("%d-%m-%Y")


def load_subscriptions() -> dict[str, bool]:
    default = {
        "ashtami":     False,
        "chaturdashi": False,
        "kalyanak":    False,
        "festival":    False,
    }
    if not os.path.exists(SUBSCRIPTIONS_FILE):
        return default
    try:
        with open(SUBSCRIPTIONS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        default.update({k: bool(v) for k, v in data.items() if k in default})
        return default
    except (json.JSONDecodeError, OSError):
        return default


def save_subscriptions(subs: dict[str, bool]) -> None:
    with open(SUBSCRIPTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(subs, f, indent=2, ensure_ascii=False)


def parv_tithis_for_month(year: int, month: int) -> list[dict[str, Any]]:
    out = []
    for ds, tithi in PARV_TITHIS_2026:
        d = parse_date(ds)
        if d.year == year and d.month == month:
            out.append({
                "date": ds, "day": d.day, "weekday": d.strftime("%A"),
                "tithi": tithi,
                "is_ashtami": "Ashtami" in tithi,
                "is_chaturdashi": "Chaturdashi" in tithi,
            })
    return sorted(out, key=lambda x: parse_date(x["date"]))


def kalyanaks_for_month(year: int, month: int) -> list[dict[str, Any]]:
    out = []
    for ds, tirthankar, types in KALYANAKS_2026:
        d = parse_date(ds)
        if d.year == year and d.month == month:
            info = TIRTHANKARS_INFO.get(tirthankar, {})
            out.append({
                "date": ds, "day": d.day, "weekday": d.strftime("%A"),
                "tirthankar": tirthankar,
                "kalyanak_label": format_kalyanak(types),
                "types": types,
                "number": info.get("number", ""),
                "symbol": info.get("symbol", ""),
            })
    return sorted(out, key=lambda x: (parse_date(x["date"]), x["number"] or 0))


def festivals_for_month(year: int, month: int) -> list[dict[str, Any]]:
    out = []
    for ds, name, ftype in FESTIVALS_2026:
        d = parse_date(ds)
        if d.year == year and d.month == month:
            out.append({
                "date": ds, "day": d.day, "weekday": d.strftime("%A"),
                "name": name, "type": ftype,
            })
    return sorted(out, key=lambda x: parse_date(x["date"]))


def events_on(target: date) -> list[dict[str, str]]:
    ds = fmt_date(target)
    events: list[dict[str, str]] = []
    for date_str, tithi in PARV_TITHIS_2026:
        if date_str == ds:
            cat = "ashtami" if "Ashtami" in tithi else "chaturdashi"
            events.append({"type": "parv", "category": cat, "label": tithi, "detail": "Parv Tithi"})
    for date_str, tirthankar, types in KALYANAKS_2026:
        if date_str == ds:
            events.append({
                "type": "kalyanak", "category": "kalyanak",
                "label": f"{tirthankar} — {format_kalyanak(types)}",
                "detail": format_kalyanak(types),
            })
    for date_str, name, ftype in FESTIVALS_2026:
        if date_str == ds:
            events.append({"type": ftype, "category": "festival", "label": name, "detail": ftype.title()})
    return events


def build_calendar_grid(year: int, month: int) -> list[list[dict[str, Any]]]:
    cal = calendar.Calendar(firstweekday=6)
    weeks = cal.monthdayscalendar(year, month)
    today = date.today()
    grid = []
    for week in weeks:
        row = []
        for day in week:
            if day == 0:
                row.append({"day": 0, "empty": True, "events": []})
                continue
            d = date(year, month, day)
            ev = events_on(d)
            row.append({
                "day": day, "empty": False, "date_str": fmt_date(d),
                "events": ev, "is_today": d == today,
                "has_parv": any(e["type"] == "parv" for e in ev),
                "has_kalyanak": any(e["type"] == "kalyanak" for e in ev),
                "has_festival": any(e["type"] in ("festival", "vrat") for e in ev),
            })
        grid.append(row)
    return grid


def upcoming_alerts() -> list[dict[str, Any]]:
    subs = load_subscriptions()
    today = date.today()
    alerts: list[dict[str, Any]] = []
    if subs.get("ashtami") or subs.get("chaturdashi"):
        for ds, tithi in PARV_TITHIS_2026:
            d = parse_date(ds)
            if d < today:
                continue
            if "Ashtami" in tithi and subs.get("ashtami"):
                alerts.append({"date": ds, "day": d.day, "month": d.month,
                               "weekday": d.strftime("%A"), "label": tithi, "category": "ashtami"})
            elif "Chaturdashi" in tithi and subs.get("chaturdashi"):
                alerts.append({"date": ds, "day": d.day, "month": d.month,
                               "weekday": d.strftime("%A"), "label": tithi, "category": "chaturdashi"})
    if subs.get("kalyanak"):
        for ds, tirthankar, types in KALYANAKS_2026:
            d = parse_date(ds)
            if d < today:
                continue
            alerts.append({"date": ds, "day": d.day, "month": d.month,
                           "weekday": d.strftime("%A"),
                           "label": f"{tirthankar} — {format_kalyanak(types)}",
                           "category": "kalyanak"})
    if subs.get("festival"):
        for ds, name, _ftype in FESTIVALS_2026:
            d = parse_date(ds)
            if d < today:
                continue
            alerts.append({"date": ds, "day": d.day, "month": d.month,
                           "weekday": d.strftime("%A"), "label": name, "category": "festival"})
    alerts.sort(key=lambda a: parse_date(a["date"]))
    return alerts


def _base_today_ctx():
    today = date.today()
    today_str = fmt_date(today)
    sunrise, sunset = sun_times_for_date(today_str)
    return {
        "today": today,
        "today_str": today_str,
        "today_weekday": today.strftime("%A"),
        "today_tithi": tithi_for_date(today_str) or "—",
        "today_sunrise": sunrise or "—",
        "today_sunset": sunset or "—",
        "today_events": events_on(today),
    }


def jain_calendar_index(request):
    today = date.today()
    try:
        year = int(request.GET.get("year", SUPPORTED_YEAR))
        month = int(request.GET.get("month", today.month))
    except (TypeError, ValueError):
        year, month = SUPPORTED_YEAR, today.month

    if not (1 <= month <= 12):
        month = today.month
    if year != SUPPORTED_YEAR:
        year = SUPPORTED_YEAR

    prev_month, prev_year = (month - 1, year) if month > 1 else (12, year - 1)
    next_month, next_year = (month + 1, year) if month < 12 else (1, year + 1)

    ctx = _base_today_ctx()
    ctx.update({
        "year": year, "month": month, "month_name": MONTH_NAMES[month],
        "prev_month": prev_month, "prev_year": prev_year,
        "next_month": next_month, "next_year": next_year,
        "prev_month_name": MONTH_NAMES[prev_month],
        "next_month_name": MONTH_NAMES[next_month],
        "parv_tithis": parv_tithis_for_month(year, month),
        "kalyanaks": kalyanaks_for_month(year, month),
        "festivals": festivals_for_month(year, month),
        "calendar_grid": build_calendar_grid(year, month),
        "weekday_headers": ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
        "subscriptions": load_subscriptions(),
    })
    return render(request, 'jain_calendar.html', ctx)


def jain_reminders(request):
    subs = load_subscriptions()
    alerts = upcoming_alerts()
    active = sum(1 for v in subs.values() if v)
    ctx = _base_today_ctx()
    ctx.update({
        "subscriptions": subs, "alerts": alerts,
        "alerts_count": len(alerts), "active_count": active,
    })
    return render(request, 'jain_reminders.html', ctx)


def jain_save_reminders(request):
    if request.method == 'POST':
        subs = {
            "ashtami":     request.POST.get("ashtami") == "on",
            "chaturdashi": request.POST.get("chaturdashi") == "on",
            "kalyanak":    request.POST.get("kalyanak") == "on",
            "festival":    request.POST.get("festival") == "on",
        }
        save_subscriptions(subs)
    return redirect('jain-reminders')


def jain_notifications_today(request):
    today = date.today()
    today_str = fmt_date(today)
    evs = events_on(today)
    subs = load_subscriptions()
    matched = [e for e in evs if subs.get(e["category"], False)]
    sr, ss = sun_times_for_date(today_str)
    return JsonResponse({
        "today": today_str,
        "weekday": today.strftime("%A"),
        "tithi": tithi_for_date(today_str),
        "sunrise": sr, "sunset": ss,
        "events": evs, "subscribed": subs, "matched": matched,
    })


def jain_search(request):
    q = (request.GET.get("q") or "").strip().lower()
    results = []
    if q:
        for ds, tirthankar, types in KALYANAKS_2026:
            if q in tirthankar.lower() or any(q in t.lower() for t in types):
                d = parse_date(ds)
                results.append({
                    "date": ds, "weekday": d.strftime("%A"),
                    "name": tirthankar, "detail": format_kalyanak(types),
                    "category": "Kalyanak",
                })
        for ds, name, ftype in FESTIVALS_2026:
            if q in name.lower():
                d = parse_date(ds)
                results.append({
                    "date": ds, "weekday": d.strftime("%A"),
                    "name": name, "detail": ftype.title(), "category": ftype.title(),
                })
    results.sort(key=lambda r: parse_date(r["date"]))
    ctx = _base_today_ctx()
    ctx.update({"query": q, "results": results})
    return render(request, 'jain_search.html', ctx)
