"""
Digambar Jain Calendar data for 2026 A.D.

Sources
-------
All tithi, Kalyanak and sunrise/sunset data has been read directly from
the monthly Jain Panchang pages published by Online Jain Pathshala
(https://onlinejainpathshala.com/jain-dharshan/jain-panchang) — the
"Tirthankar Vardhman" calendar in the Vidyasagar Ji tradition.
Every date here has been cross-checked against the scanned panchang
image for that month.

Corrections in this revision
----------------------------
- Shukla Ashtami May: 23 May (not 24)
- Shukla Chaturdashi June: 28 June (not 29)
- Shukla Ashtami August: 20 August (not 19)

Kalyanak types
--------------
Garbh  : conception (soul enters mother's womb)
Janma  : birth
Tap    : diksha / renunciation
Gyan   : kevalgnan / omniscience
Moksha : nirvana / liberation
"""

# =============================================================
# 1. Tirthankar Kalyanaks
# =============================================================
# (date "DD-MM-YYYY", Tirthankar, [types])
KALYANAKS_2026 = [
    # ---------------- January ----------------
    ("02-01-2026", "Shree Abhinandan Bhagwan",   ["Gyan"]),
    ("03-01-2026", "Shree Dharmanath Bhagwan",   ["Gyan"]),
    ("08-01-2026", "Shree Padmaprabh Bhagwan",   ["Garbh"]),
    ("15-01-2026", "Shree Shitalnath Bhagwan",   ["Janma", "Tap"]),
    ("17-01-2026", "Shree Rushabhdev Bhagwan",   ["Moksha"]),
    ("18-01-2026", "Shree Shreyansnath Bhagwan", ["Gyan"]),
    ("20-01-2026", "Shree Vasupujya Bhagwan",    ["Gyan"]),
    ("22-01-2026", "Shree Vimalnath Bhagwan",    ["Janma", "Tap"]),
    ("24-01-2026", "Shree Vimalnath Bhagwan",    ["Gyan"]),
    ("27-01-2026", "Shree Ajitnath Bhagwan",     ["Tap"]),
    ("28-01-2026", "Shree Ajitnath Bhagwan",     ["Janma"]),
    ("30-01-2026", "Shree Abhinandan Bhagwan",   ["Janma", "Tap"]),
    ("30-01-2026", "Shree Dharmanath Bhagwan",   ["Janma", "Tap"]),
    # ---------------- February ----------------
    ("05-02-2026", "Shree Padmaprabh Bhagwan",   ["Moksha"]),
    ("07-02-2026", "Shree Suparshvanath Bhagwan", ["Gyan"]),
    ("08-02-2026", "Shree Suparshvanath Bhagwan", ["Moksha"]),
    ("08-02-2026", "Shree Chandraprabh Bhagwan", ["Gyan", "Moksha"]),
    ("10-02-2026", "Shree Pushpadant Bhagwan",   ["Garbh"]),
    ("13-02-2026", "Shree Rushabhdev Bhagwan",   ["Gyan"]),
    ("13-02-2026", "Shree Shreyansnath Bhagwan", ["Janma", "Tap"]),
    ("14-02-2026", "Shree Munisuvrat Bhagwan",   ["Moksha"]),
    ("16-02-2026", "Shree Vasupujya Bhagwan",    ["Janma", "Tap"]),
    ("20-02-2026", "Shree Arahnath Bhagwan",     ["Garbh"]),
    ("22-02-2026", "Shree Mallinath Bhagwan",    ["Moksha"]),
    ("23-02-2026", "Shree Chandraprabh Bhagwan", ["Moksha"]),
    ("24-02-2026", "Shree Sambhavnath Bhagwan",  ["Garbh"]),
    # ---------------- March ----------------
    ("07-03-2026", "Shree Parshvanath Bhagwan",  ["Gyan"]),
    ("08-03-2026", "Shree Chandraprabh Bhagwan", ["Garbh"]),
    ("11-03-2026", "Shree Shitalnath Bhagwan",   ["Garbh"]),
    ("12-03-2026", "Shree Rushabhdev Bhagwan",   ["Janma", "Tap"]),
    ("18-03-2026", "Shree Anantnath Bhagwan",    ["Gyan", "Moksha"]),
    ("18-03-2026", "Shree Arahnath Bhagwan",     ["Moksha"]),
    ("19-03-2026", "Shree Mallinath Bhagwan",    ["Garbh"]),
    ("21-03-2026", "Shree Kunthunath Bhagwan",   ["Gyan"]),
    ("23-03-2026", "Shree Ajitnath Bhagwan",     ["Moksha"]),
    ("24-03-2026", "Shree Sambhavnath Bhagwan",  ["Moksha"]),
    ("28-03-2026", "Shree Sumatinath Bhagwan",   ["Janma", "Gyan", "Moksha"]),
    ("30-03-2026", "Shree Mahavir Bhagwan",      ["Janma"]),
    # ---------------- April ----------------
    ("01-04-2026", "Shree Padmaprabh Bhagwan",   ["Gyan"]),
    ("04-04-2026", "Shree Parshvanath Bhagwan",  ["Garbh"]),
    ("11-04-2026", "Shree Munisuvrat Bhagwan",   ["Gyan"]),
    ("12-04-2026", "Shree Munisuvrat Bhagwan",   ["Janma", "Tap"]),
    ("15-04-2026", "Shree Dharmanath Bhagwan",   ["Garbh"]),
    ("16-04-2026", "Shree Naminath Bhagwan",     ["Moksha"]),
    ("18-04-2026", "Shree Kunthunath Bhagwan",   ["Janma", "Tap", "Moksha"]),
    ("22-04-2026", "Shree Abhinandan Bhagwan",   ["Garbh", "Moksha"]),
    ("25-04-2026", "Shree Sumatinath Bhagwan",   ["Tap"]),
    ("26-04-2026", "Shree Mahavir Bhagwan",      ["Gyan"]),
    # ---------------- May ----------------
    ("08-05-2026", "Shree Shreyansnath Bhagwan", ["Garbh"]),
    ("12-05-2026", "Shree Vimalnath Bhagwan",    ["Garbh"]),
    ("14-05-2026", "Shree Anantnath Bhagwan",    ["Janma", "Tap"]),
    ("15-05-2026", "Shree Shantinath Bhagwan",   ["Janma", "Tap", "Moksha"]),
    ("16-05-2026", "Shree Ajitnath Bhagwan",     ["Garbh"]),
    # ---------------- June ----------------
    ("18-06-2026", "Shree Dharmanath Bhagwan",   ["Moksha"]),
    ("26-06-2026", "Shree Suparshvanath Bhagwan", ["Janma", "Tap"]),
    # ---------------- July ----------------
    ("02-07-2026", "Shree Rushabhdev Bhagwan",   ["Garbh"]),
    ("06-07-2026", "Shree Vasupujya Bhagwan",    ["Garbh"]),
    ("08-07-2026", "Shree Vimalnath Bhagwan",    ["Moksha"]),
    ("09-07-2026", "Shree Naminath Bhagwan",     ["Janma", "Tap"]),
    ("19-07-2026", "Shree Mahavir Bhagwan",      ["Garbh"]),
    ("20-07-2026", "Shree Neminath Bhagwan",     ["Moksha"]),
    ("31-07-2026", "Shree Munisuvrat Bhagwan",   ["Garbh"]),
    # ---------------- August ----------------
    ("08-08-2026", "Shree Kunthunath Bhagwan",   ["Garbh"]),
    ("14-08-2026", "Shree Sumatinath Bhagwan",   ["Garbh"]),
    ("18-08-2026", "Shree Neminath Bhagwan",     ["Janma", "Tap"]),
    ("19-08-2026", "Shree Parshvanath Bhagwan",  ["Moksha"]),
    ("28-08-2026", "Shree Shreyansnath Bhagwan", ["Moksha"]),
    # ---------------- September ----------------
    ("03-09-2026", "Shree Shantinath Bhagwan",   ["Garbh"]),
    ("17-09-2026", "Shree Suparshvanath Bhagwan", ["Garbh"]),
    ("19-09-2026", "Shree Pushpadant Bhagwan",   ["Moksha"]),
    ("25-09-2026", "Shree Vasupujya Bhagwan",    ["Moksha"]),
    ("28-09-2026", "Shree Naminath Bhagwan",     ["Garbh"]),
    # ---------------- October ----------------
    ("11-10-2026", "Shree Neminath Bhagwan",     ["Gyan"]),
    ("19-10-2026", "Shree Shitalnath Bhagwan",   ["Moksha"]),
    ("26-10-2026", "Shree Anantnath Bhagwan",    ["Garbh"]),
    ("29-10-2026", "Shree Sambhavnath Bhagwan",  ["Gyan"]),
    # ---------------- November ----------------
    ("07-11-2026", "Shree Padmaprabh Bhagwan",   ["Janma", "Tap"]),
    ("09-11-2026", "Shree Mahavir Bhagwan",      ["Moksha"]),
    ("11-11-2026", "Shree Pushpadant Bhagwan",   ["Gyan"]),
    ("15-11-2026", "Shree Neminath Bhagwan",     ["Garbh"]),
    ("21-11-2026", "Shree Arahnath Bhagwan",     ["Gyan"]),
    ("24-11-2026", "Shree Sambhavnath Bhagwan",  ["Janma"]),
    # ---------------- December ----------------
    ("03-12-2026", "Shree Mahavir Bhagwan",      ["Tap"]),
    ("09-12-2026", "Shree Pushpadant Bhagwan",   ["Janma", "Tap"]),
    ("19-12-2026", "Shree Arahnath Bhagwan",     ["Tap"]),
    ("20-12-2026", "Shree Mallinath Bhagwan",    ["Janma", "Tap"]),
    ("20-12-2026", "Shree Naminath Bhagwan",     ["Gyan"]),
    ("23-12-2026", "Shree Arahnath Bhagwan",     ["Janma"]),
    ("23-12-2026", "Shree Sambhavnath Bhagwan",  ["Tap"]),
    ("25-12-2026", "Shree Mallinath Bhagwan",    ["Gyan"]),
]


# =============================================================
# 2. Jain festivals and vrats
# =============================================================
FESTIVALS_2026 = [
    # ----- January -----
    ("01-01-2026", "Rohini Vrat", "vrat"),
    ("02-01-2026", "Shodashkaran Vrat Prarambh", "vrat"),
    ("14-01-2026", "Devdarshan Divas", "festival"),
    ("17-01-2026", "Shree Adinath Bhagwan Moksha Divas", "festival"),
    ("19-01-2026", "Labdhi Vidhan Vrat Prarambh", "vrat"),
    ("21-01-2026", "Labdhi Vidhan Vrat Purn", "vrat"),
    ("22-01-2026", "Das Lakshan Vrat Prarambh", "vrat"),
    ("23-01-2026", "Pushpanjali Vrat Prarambh", "vrat"),
    ("27-01-2026", "Pushpanjali Vrat Purn", "vrat"),
    ("29-01-2026", "Rohini Vrat", "vrat"),
    ("30-01-2026", "Ratnatray Vrat Prarambh", "vrat"),
    ("31-01-2026", "Das Lakshan Vrat Purn", "vrat"),
    # ----- February -----
    ("02-02-2026", "Shodashkaran Vrat Purn", "vrat"),
    ("25-02-2026", "Rohini Vrat", "vrat"),
    # ----- March -----
    ("02-03-2026", "Shodashkaran Vrat Prarambh", "vrat"),
    ("03-03-2026", "Ashtanika Vrat Purn", "vrat"),
    ("12-03-2026", "Tirthankar Divas", "festival"),
    ("19-03-2026", "Labdhi Vidhan Vrat Prarambh", "vrat"),
    ("21-03-2026", "Labdhi Vidhan Vrat Purn", "vrat"),
    ("22-03-2026", "Das Lakshan Vrat Prarambh", "vrat"),
    ("23-03-2026", "Pushpanjali Vrat Prarambh", "vrat"),
    ("24-03-2026", "Rohini Vrat", "vrat"),
    ("27-03-2026", "Pushpanjali Vrat Purn", "vrat"),
    ("30-03-2026", "Ratnatray Vrat Prarambh", "vrat"),
    ("30-03-2026", "Mahavir Jayanti (Janma Divas)", "festival"),
    ("31-03-2026", "Das Lakshan Vrat Purn", "vrat"),
    # ----- April -----
    ("01-04-2026", "Ratnatray Vrat Purn", "vrat"),
    ("02-04-2026", "Shodashkaran Vrat Purn", "vrat"),
    ("19-04-2026", "Akshay Tritiya (Rushabhdev Bhagwan Aahar din)", "festival"),
    ("20-04-2026", "Rohini Vrat", "vrat"),
    # ----- May -----
    ("15-05-2026", "Shanti Dhara Divas", "festival"),
    ("17-05-2026", "Adhik Maas Prarambh", "festival"),
    ("18-05-2026", "Rohini Vrat", "vrat"),
    # ----- June -----
    ("14-06-2026", "Rohini Vrat", "vrat"),
    ("15-06-2026", "Adhik Maas Samapt", "festival"),
    ("19-06-2026", "Shrut Panchami (Jinvani Divas)", "festival"),
    # ----- July -----
    ("12-07-2026", "Rohini Vrat", "vrat"),
    ("18-07-2026", "Rishi Panchami", "festival"),
    ("20-07-2026", "Namokar Paintisi Vrat Prarambh", "vrat"),
    ("21-07-2026", "Ashtanika Vrat Prarambh", "vrat"),
    ("26-07-2026", "Ravi Vrat", "vrat"),
    ("28-07-2026", "Chaturmaas Prarambh (Kalash Sthapna)", "festival"),
    ("28-07-2026", "Karma Nirjara Vrat", "vrat"),
    ("29-07-2026", "Ashtanika Vrat Purn", "vrat"),
    ("30-07-2026", "Veer Shasan Jayanti / Yug Parivartan Divas", "festival"),
    ("31-07-2026", "Ratnavali / Ekavali / Dwikavali Vrat", "vrat"),
    # ----- August -----
    ("09-08-2026", "Rohini Vrat", "vrat"),
    ("28-08-2026", "Raksha Bandhan (Vishnukumar Muni)", "festival"),
    # ----- September -----
    ("04-09-2026", "Janmashtami", "festival"),
    ("06-09-2026", "Rohini Vrat", "vrat"),
    ("13-09-2026", "Sola Kaaran Vrat Prarambh", "vrat"),
    ("14-09-2026", "Labdhi Vidhan Vrat Prarambh", "vrat"),
    ("15-09-2026", "Das Lakshan Paryushan Prarambh (Uttam Kshama)", "festival"),
    ("21-09-2026", "Sugandh Dashami Vrat", "vrat"),
    ("22-09-2026", "Ratnatray Vrat Prarambh", "vrat"),
    ("24-09-2026", "Anant Vrat Prarambh", "vrat"),
    ("25-09-2026", "Anant Chaturdashi (Das Lakshan Samapt)", "festival"),
    ("26-09-2026", "Kshama-vani Parva / Ratnatray Vrat Purn", "festival"),
    # ----- October -----
    ("01-10-2026", "Rohini Vrat", "vrat"),
    ("21-10-2026", "Vijayadashami (Dussehra)", "festival"),
    # ----- November -----
    ("08-11-2026", "Dhanteras (Mahavir Nirvana Laghu Divas)", "festival"),
    ("09-11-2026", "Deepavali / Mahavir Nirvana / Gautam Swami Kevalgnan", "festival"),
    ("10-11-2026", "Govardhan Puja / Nutan Varsh (Veer Nirvana Samvat 2553)", "festival"),
    ("11-11-2026", "Bhai Dooj", "festival"),
    ("14-11-2026", "Gyan Panchami", "festival"),
    ("24-11-2026", "Kartik Purnima", "festival"),
    ("25-11-2026", "Rohini Vrat", "vrat"),
    # ----- December -----
    ("04-12-2026", "Mukta-vali Vrat", "vrat"),
    ("12-12-2026", "Mukta-vali Vrat", "vrat"),
    ("23-12-2026", "Rohini Vrat", "vrat"),
]


# =============================================================
# 3. Parv Tithis (Ashtami & Chaturdashi) — CORRECTED
# =============================================================
PARV_TITHIS_2026 = [
    # ----- January -----
    ("02-01-2026", "Shukla Chaturdashi"),
    ("11-01-2026", "Krishna Ashtami"),
    ("17-01-2026", "Krishna Chaturdashi"),
    ("26-01-2026", "Shukla Ashtami"),
    ("31-01-2026", "Shukla Chaturdashi"),
    # ----- February -----
    ("09-02-2026", "Krishna Ashtami"),
    ("16-02-2026", "Krishna Chaturdashi"),
    ("24-02-2026", "Shukla Ashtami"),
    # ----- March -----
    ("02-03-2026", "Shukla Chaturdashi"),
    ("11-03-2026", "Krishna Ashtami"),
    ("18-03-2026", "Krishna Chaturdashi"),
    ("26-03-2026", "Shukla Ashtami"),
    ("31-03-2026", "Shukla Chaturdashi"),
    # ----- April -----
    ("10-04-2026", "Krishna Ashtami"),
    ("16-04-2026", "Krishna Chaturdashi"),
    ("24-04-2026", "Shukla Ashtami"),
    ("30-04-2026", "Shukla Chaturdashi"),
    # ----- May (CORRECTED: 23 not 24) -----
    ("10-05-2026", "Krishna Ashtami"),
    ("15-05-2026", "Krishna Chaturdashi"),
    ("23-05-2026", "Shukla Ashtami"),       # was 24, corrected
    ("30-05-2026", "Shukla Chaturdashi"),
    # ----- June (CORRECTED: 28 not 29) -----
    ("08-06-2026", "Krishna Ashtami"),
    ("14-06-2026", "Krishna Chaturdashi"),
    ("22-06-2026", "Shukla Ashtami"),
    ("28-06-2026", "Shukla Chaturdashi"),   # was 29, corrected
    # ----- July -----
    ("08-07-2026", "Krishna Ashtami"),
    ("13-07-2026", "Krishna Chaturdashi"),
    ("21-07-2026", "Shukla Ashtami"),
    ("28-07-2026", "Shukla Chaturdashi"),
    # ----- August (CORRECTED: 20 not 19) -----
    ("06-08-2026", "Krishna Ashtami"),
    ("11-08-2026", "Krishna Chaturdashi"),
    ("20-08-2026", "Shukla Ashtami"),       # was 19, corrected
    ("27-08-2026", "Shukla Chaturdashi"),
    # ----- September -----
    ("04-09-2026", "Krishna Ashtami"),
    ("10-09-2026", "Krishna Chaturdashi"),
    ("19-09-2026", "Shukla Ashtami"),
    ("25-09-2026", "Shukla Chaturdashi"),
    # ----- October -----
    ("03-10-2026", "Krishna Ashtami"),
    ("09-10-2026", "Krishna Chaturdashi"),
    ("19-10-2026", "Shukla Ashtami"),
    ("25-10-2026", "Shukla Chaturdashi"),
    # ----- November -----
    ("02-11-2026", "Krishna Ashtami"),
    ("08-11-2026", "Krishna Chaturdashi"),
    ("17-11-2026", "Shukla Ashtami"),
    ("23-11-2026", "Shukla Chaturdashi"),
    # ----- December -----
    ("01-12-2026", "Krishna Ashtami"),
    ("07-12-2026", "Krishna Chaturdashi"),
    ("17-12-2026", "Shukla Ashtami"),
    ("23-12-2026", "Shukla Chaturdashi"),
    ("31-12-2026", "Krishna Ashtami"),
]


# =============================================================
# 4. 24 Tirthankar reference
# =============================================================
TIRTHANKARS_INFO = {
    "Shree Rushabhdev Bhagwan":   {"number": 1,  "symbol": "Bull"},
    "Shree Ajitnath Bhagwan":     {"number": 2,  "symbol": "Elephant"},
    "Shree Sambhavnath Bhagwan":  {"number": 3,  "symbol": "Horse"},
    "Shree Abhinandan Bhagwan":   {"number": 4,  "symbol": "Monkey"},
    "Shree Sumatinath Bhagwan":   {"number": 5,  "symbol": "Red Goose"},
    "Shree Padmaprabh Bhagwan":   {"number": 6,  "symbol": "Red Lotus"},
    "Shree Suparshvanath Bhagwan": {"number": 7, "symbol": "Swastika"},
    "Shree Chandraprabh Bhagwan": {"number": 8,  "symbol": "Moon"},
    "Shree Pushpadant Bhagwan":   {"number": 9,  "symbol": "Crocodile"},
    "Shree Shitalnath Bhagwan":   {"number": 10, "symbol": "Wishing Tree"},
    "Shree Shreyansnath Bhagwan": {"number": 11, "symbol": "Rhinoceros"},
    "Shree Vasupujya Bhagwan":    {"number": 12, "symbol": "Buffalo"},
    "Shree Vimalnath Bhagwan":    {"number": 13, "symbol": "Boar"},
    "Shree Anantnath Bhagwan":    {"number": 14, "symbol": "Hawk"},
    "Shree Dharmanath Bhagwan":   {"number": 15, "symbol": "Vajra"},
    "Shree Shantinath Bhagwan":   {"number": 16, "symbol": "Deer"},
    "Shree Kunthunath Bhagwan":   {"number": 17, "symbol": "Goat"},
    "Shree Arahnath Bhagwan":     {"number": 18, "symbol": "Fish"},
    "Shree Mallinath Bhagwan":    {"number": 19, "symbol": "Water-jar"},
    "Shree Munisuvrat Bhagwan":   {"number": 20, "symbol": "Tortoise"},
    "Shree Naminath Bhagwan":     {"number": 21, "symbol": "Blue Lotus"},
    "Shree Neminath Bhagwan":     {"number": 22, "symbol": "Conch"},
    "Shree Parshvanath Bhagwan":  {"number": 23, "symbol": "Serpent"},
    "Shree Mahavir Bhagwan":      {"number": 24, "symbol": "Lion"},
}

KALYANAK_SUFFIX = "Kalyanak"


def format_kalyanak(types_list):
    return " + ".join(types_list) + " " + KALYANAK_SUFFIX


# =============================================================
# 5. Daily tithi names for 2026 (for the header display)
# =============================================================
# Key format: "DD-MM-YYYY" -> "Krishna/Shukla + tithi ordinal"
# Derived from panchang by mapping each day to the tithi printed in its cell.
# Lunar month is included as a prefix (e.g., "Magh Krishna Pratipada").
TITHI_NAMES = {
    1: "Pratipada", 2: "Dwitiya", 3: "Tritiya", 4: "Chaturthi",
    5: "Panchami", 6: "Shashthi", 7: "Saptami", 8: "Ashtami",
    9: "Navami",   10: "Dashami", 11: "Ekadashi", 12: "Dwadashi",
    13: "Trayodashi", 14: "Chaturdashi", 15: "Purnima/Amavasya",
    30: "Amavasya",
}

# Daily tithi table — (date, paksha, tithi_num, lunar_month).
# Compiled from the panchang scans.  Lunar month shown for context.
DAILY_TITHIS_2026 = {
    # ---- January (Paush Shukla 13 … Magh Shukla 14)
    "01-01-2026": ("Shukla", 13, "Paush"),
    "02-01-2026": ("Shukla", 14, "Paush"),
    "03-01-2026": ("Shukla", 15, "Paush"),
    "04-01-2026": ("Krishna", 1, "Magh"),
    "05-01-2026": ("Krishna", 2, "Magh"),  # 2-3
    "06-01-2026": ("Krishna", 4, "Magh"),
    "07-01-2026": ("Krishna", 5, "Magh"),
    "08-01-2026": ("Krishna", 6, "Magh"),
    "09-01-2026": ("Krishna", 7, "Magh"),
    "10-01-2026": ("Krishna", 7, "Magh"),
    "11-01-2026": ("Krishna", 8, "Magh"),
    "12-01-2026": ("Krishna", 9, "Magh"),
    "13-01-2026": ("Krishna", 10, "Magh"),
    "14-01-2026": ("Krishna", 11, "Magh"),
    "15-01-2026": ("Krishna", 12, "Magh"),
    "16-01-2026": ("Krishna", 13, "Magh"),
    "17-01-2026": ("Krishna", 14, "Magh"),
    "18-01-2026": ("Krishna", 30, "Magh"),
    "19-01-2026": ("Shukla", 1, "Magh"),
    "20-01-2026": ("Shukla", 2, "Magh"),
    "21-01-2026": ("Shukla", 3, "Magh"),
    "22-01-2026": ("Shukla", 4, "Magh"),
    "23-01-2026": ("Shukla", 5, "Magh"),
    "24-01-2026": ("Shukla", 6, "Magh"),
    "25-01-2026": ("Shukla", 7, "Magh"),
    "26-01-2026": ("Shukla", 8, "Magh"),
    "27-01-2026": ("Shukla", 9, "Magh"),
    "28-01-2026": ("Shukla", 10, "Magh"),
    "29-01-2026": ("Shukla", 11, "Magh"),
    "30-01-2026": ("Shukla", 12, "Magh"),
    "31-01-2026": ("Shukla", 14, "Magh"),
    # ---- February ----
    "01-02-2026": ("Shukla", 15, "Magh"),
    "02-02-2026": ("Krishna", 1, "Falgun"),
    "03-02-2026": ("Krishna", 2, "Falgun"),
    "04-02-2026": ("Krishna", 3, "Falgun"),
    "05-02-2026": ("Krishna", 4, "Falgun"),
    "06-02-2026": ("Krishna", 5, "Falgun"),
    "07-02-2026": ("Krishna", 6, "Falgun"),
    "08-02-2026": ("Krishna", 7, "Falgun"),
    "09-02-2026": ("Krishna", 8, "Falgun"),
    "10-02-2026": ("Krishna", 9, "Falgun"),
    "11-02-2026": ("Krishna", 9, "Falgun"),
    "12-02-2026": ("Krishna", 10, "Falgun"),
    "13-02-2026": ("Krishna", 11, "Falgun"),
    "14-02-2026": ("Krishna", 12, "Falgun"),
    "15-02-2026": ("Krishna", 13, "Falgun"),
    "16-02-2026": ("Krishna", 14, "Falgun"),
    "17-02-2026": ("Krishna", 30, "Falgun"),
    "18-02-2026": ("Shukla", 1, "Falgun"),
    "19-02-2026": ("Shukla", 2, "Falgun"),
    "20-02-2026": ("Shukla", 3, "Falgun"),
    "21-02-2026": ("Shukla", 4, "Falgun"),
    "22-02-2026": ("Shukla", 5, "Falgun"),
    "23-02-2026": ("Shukla", 6, "Falgun"),
    "24-02-2026": ("Shukla", 8, "Falgun"),
    "25-02-2026": ("Shukla", 9, "Falgun"),
    "26-02-2026": ("Shukla", 10, "Falgun"),
    "27-02-2026": ("Shukla", 11, "Falgun"),
    "28-02-2026": ("Shukla", 12, "Falgun"),
    # ---- March ----
    "01-03-2026": ("Shukla", 13, "Falgun"),
    "02-03-2026": ("Shukla", 14, "Falgun"),
    "03-03-2026": ("Shukla", 15, "Falgun"),
    "04-03-2026": ("Krishna", 1, "Chaitra"),
    "05-03-2026": ("Krishna", 2, "Chaitra"),
    "06-03-2026": ("Krishna", 3, "Chaitra"),
    "07-03-2026": ("Krishna", 4, "Chaitra"),
    "08-03-2026": ("Krishna", 5, "Chaitra"),
    "09-03-2026": ("Krishna", 6, "Chaitra"),
    "10-03-2026": ("Krishna", 7, "Chaitra"),
    "11-03-2026": ("Krishna", 8, "Chaitra"),
    "12-03-2026": ("Krishna", 9, "Chaitra"),
    "13-03-2026": ("Krishna", 10, "Chaitra"),
    "14-03-2026": ("Krishna", 10, "Chaitra"),
    "15-03-2026": ("Krishna", 11, "Chaitra"),
    "16-03-2026": ("Krishna", 12, "Chaitra"),
    "17-03-2026": ("Krishna", 13, "Chaitra"),
    "18-03-2026": ("Krishna", 14, "Chaitra"),
    "19-03-2026": ("Shukla", 1, "Chaitra"),
    "20-03-2026": ("Shukla", 2, "Chaitra"),
    "21-03-2026": ("Shukla", 3, "Chaitra"),
    "22-03-2026": ("Shukla", 4, "Chaitra"),
    "23-03-2026": ("Shukla", 5, "Chaitra"),
    "24-03-2026": ("Shukla", 6, "Chaitra"),
    "25-03-2026": ("Shukla", 7, "Chaitra"),
    "26-03-2026": ("Shukla", 8, "Chaitra"),
    "27-03-2026": ("Shukla", 9, "Chaitra"),
    "28-03-2026": ("Shukla", 10, "Chaitra"),
    "29-03-2026": ("Shukla", 12, "Chaitra"),
    "30-03-2026": ("Shukla", 13, "Chaitra"),
    "31-03-2026": ("Shukla", 14, "Chaitra"),
    # ---- April ----
    "01-04-2026": ("Shukla", 15, "Chaitra"),
    "02-04-2026": ("Krishna", 1, "Vaishakh"),
    "03-04-2026": ("Krishna", 2, "Vaishakh"),
    "04-04-2026": ("Krishna", 2, "Vaishakh"),
    "05-04-2026": ("Krishna", 3, "Vaishakh"),
    "06-04-2026": ("Krishna", 4, "Vaishakh"),
    "07-04-2026": ("Krishna", 5, "Vaishakh"),
    "08-04-2026": ("Krishna", 6, "Vaishakh"),
    "09-04-2026": ("Krishna", 7, "Vaishakh"),
    "10-04-2026": ("Krishna", 8, "Vaishakh"),
    "11-04-2026": ("Krishna", 9, "Vaishakh"),
    "12-04-2026": ("Krishna", 10, "Vaishakh"),
    "13-04-2026": ("Krishna", 11, "Vaishakh"),
    "14-04-2026": ("Krishna", 12, "Vaishakh"),
    "15-04-2026": ("Krishna", 13, "Vaishakh"),
    "16-04-2026": ("Krishna", 14, "Vaishakh"),
    "17-04-2026": ("Krishna", 30, "Vaishakh"),
    "18-04-2026": ("Shukla", 1, "Vaishakh"),
    "19-04-2026": ("Shukla", 2, "Vaishakh"),
    "20-04-2026": ("Shukla", 4, "Vaishakh"),
    "21-04-2026": ("Shukla", 5, "Vaishakh"),
    "22-04-2026": ("Shukla", 6, "Vaishakh"),
    "23-04-2026": ("Shukla", 7, "Vaishakh"),
    "24-04-2026": ("Shukla", 8, "Vaishakh"),
    "25-04-2026": ("Shukla", 9, "Vaishakh"),
    "26-04-2026": ("Shukla", 10, "Vaishakh"),
    "27-04-2026": ("Shukla", 11, "Vaishakh"),
    "28-04-2026": ("Shukla", 12, "Vaishakh"),
    "29-04-2026": ("Shukla", 13, "Vaishakh"),
    "30-04-2026": ("Shukla", 14, "Vaishakh"),
    # ---- May (Adhik month: Pratham Jyeshtha) ----
    "01-05-2026": ("Shukla", 15, "Vaishakh"),
    "02-05-2026": ("Krishna", 1, "Jyeshtha"),
    "03-05-2026": ("Krishna", 2, "Jyeshtha"),
    "04-05-2026": ("Krishna", 3, "Jyeshtha"),
    "05-05-2026": ("Krishna", 4, "Jyeshtha"),
    "06-05-2026": ("Krishna", 4, "Jyeshtha"),
    "07-05-2026": ("Krishna", 5, "Jyeshtha"),
    "08-05-2026": ("Krishna", 6, "Jyeshtha"),
    "09-05-2026": ("Krishna", 7, "Jyeshtha"),
    "10-05-2026": ("Krishna", 8, "Jyeshtha"),
    "11-05-2026": ("Krishna", 9, "Jyeshtha"),
    "12-05-2026": ("Krishna", 10, "Jyeshtha"),
    "13-05-2026": ("Krishna", 11, "Jyeshtha"),
    "14-05-2026": ("Krishna", 12, "Jyeshtha"),
    "15-05-2026": ("Krishna", 14, "Jyeshtha"),
    "16-05-2026": ("Krishna", 30, "Jyeshtha"),
    "17-05-2026": ("Shukla", 1, "Jyeshtha"),
    "18-05-2026": ("Shukla", 2, "Jyeshtha"),
    "19-05-2026": ("Shukla", 3, "Jyeshtha"),
    "20-05-2026": ("Shukla", 4, "Jyeshtha"),
    "21-05-2026": ("Shukla", 5, "Jyeshtha"),
    "22-05-2026": ("Shukla", 7, "Jyeshtha"),
    "23-05-2026": ("Shukla", 8, "Jyeshtha"),
    "24-05-2026": ("Shukla", 9, "Jyeshtha"),
    "25-05-2026": ("Shukla", 10, "Jyeshtha"),
    "26-05-2026": ("Shukla", 11, "Jyeshtha"),
    "27-05-2026": ("Shukla", 12, "Jyeshtha"),
    "28-05-2026": ("Shukla", 13, "Jyeshtha"),
    "29-05-2026": ("Shukla", 13, "Jyeshtha"),
    "30-05-2026": ("Shukla", 14, "Jyeshtha"),
    "31-05-2026": ("Shukla", 15, "Jyeshtha"),
    # ---- June (Dwitiya Jyeshtha) ----
    "01-06-2026": ("Krishna", 1, "Jyeshtha"),
    "02-06-2026": ("Krishna", 2, "Jyeshtha"),
    "03-06-2026": ("Krishna", 3, "Jyeshtha"),
    "04-06-2026": ("Krishna", 4, "Jyeshtha"),
    "05-06-2026": ("Krishna", 5, "Jyeshtha"),
    "06-06-2026": ("Krishna", 6, "Jyeshtha"),
    "07-06-2026": ("Krishna", 7, "Jyeshtha"),
    "08-06-2026": ("Krishna", 8, "Jyeshtha"),
    "09-06-2026": ("Krishna", 9, "Jyeshtha"),
    "10-06-2026": ("Krishna", 10, "Jyeshtha"),
    "11-06-2026": ("Krishna", 11, "Jyeshtha"),
    "12-06-2026": ("Krishna", 12, "Jyeshtha"),
    "13-06-2026": ("Krishna", 13, "Jyeshtha"),
    "14-06-2026": ("Krishna", 14, "Jyeshtha"),
    "15-06-2026": ("Krishna", 30, "Jyeshtha"),
    "16-06-2026": ("Shukla", 2, "Jyeshtha"),
    "17-06-2026": ("Shukla", 3, "Jyeshtha"),
    "18-06-2026": ("Shukla", 4, "Jyeshtha"),
    "19-06-2026": ("Shukla", 5, "Jyeshtha"),
    "20-06-2026": ("Shukla", 6, "Jyeshtha"),
    "21-06-2026": ("Shukla", 7, "Jyeshtha"),
    "22-06-2026": ("Shukla", 8, "Jyeshtha"),
    "23-06-2026": ("Shukla", 9, "Jyeshtha"),
    "24-06-2026": ("Shukla", 10, "Jyeshtha"),
    "25-06-2026": ("Shukla", 11, "Jyeshtha"),
    "26-06-2026": ("Shukla", 12, "Jyeshtha"),
    "27-06-2026": ("Shukla", 13, "Jyeshtha"),
    "28-06-2026": ("Shukla", 14, "Jyeshtha"),
    "29-06-2026": ("Shukla", 15, "Jyeshtha"),
    "30-06-2026": ("Krishna", 1, "Ashadh"),
    # ---- July ----
    "01-07-2026": ("Krishna", 1, "Ashadh"),
    "02-07-2026": ("Krishna", 2, "Ashadh"),
    "03-07-2026": ("Krishna", 3, "Ashadh"),
    "04-07-2026": ("Krishna", 4, "Ashadh"),
    "05-07-2026": ("Krishna", 5, "Ashadh"),
    "06-07-2026": ("Krishna", 6, "Ashadh"),
    "07-07-2026": ("Krishna", 7, "Ashadh"),
    "08-07-2026": ("Krishna", 8, "Ashadh"),
    "09-07-2026": ("Krishna", 9, "Ashadh"),
    "10-07-2026": ("Krishna", 10, "Ashadh"),
    "11-07-2026": ("Krishna", 12, "Ashadh"),
    "12-07-2026": ("Krishna", 13, "Ashadh"),
    "13-07-2026": ("Krishna", 14, "Ashadh"),
    "14-07-2026": ("Krishna", 30, "Ashadh"),
    "15-07-2026": ("Shukla", 1, "Ashadh"),
    "16-07-2026": ("Shukla", 2, "Ashadh"),
    "17-07-2026": ("Shukla", 4, "Ashadh"),
    "18-07-2026": ("Shukla", 5, "Ashadh"),
    "19-07-2026": ("Shukla", 6, "Ashadh"),
    "20-07-2026": ("Shukla", 7, "Ashadh"),
    "21-07-2026": ("Shukla", 8, "Ashadh"),
    "22-07-2026": ("Shukla", 9, "Ashadh"),
    "23-07-2026": ("Shukla", 10, "Ashadh"),
    "24-07-2026": ("Shukla", 11, "Ashadh"),
    "25-07-2026": ("Shukla", 12, "Ashadh"),
    "26-07-2026": ("Shukla", 13, "Ashadh"),
    "27-07-2026": ("Shukla", 13, "Ashadh"),
    "28-07-2026": ("Shukla", 14, "Ashadh"),
    "29-07-2026": ("Shukla", 15, "Ashadh"),
    "30-07-2026": ("Krishna", 1, "Shravan"),
    "31-07-2026": ("Krishna", 2, "Shravan"),
    # ---- August ----
    "01-08-2026": ("Krishna", 3, "Shravan"),
    "02-08-2026": ("Krishna", 4, "Shravan"),
    "03-08-2026": ("Krishna", 5, "Shravan"),
    "04-08-2026": ("Krishna", 6, "Shravan"),
    "05-08-2026": ("Krishna", 7, "Shravan"),
    "06-08-2026": ("Krishna", 8, "Shravan"),
    "07-08-2026": ("Krishna", 9, "Shravan"),
    "08-08-2026": ("Krishna", 10, "Shravan"),
    "09-08-2026": ("Krishna", 11, "Shravan"),
    "10-08-2026": ("Krishna", 13, "Shravan"),
    "11-08-2026": ("Krishna", 14, "Shravan"),
    "12-08-2026": ("Krishna", 30, "Shravan"),
    "13-08-2026": ("Shukla", 1, "Shravan"),
    "14-08-2026": ("Shukla", 2, "Shravan"),
    "15-08-2026": ("Shukla", 3, "Shravan"),
    "16-08-2026": ("Shukla", 4, "Shravan"),
    "17-08-2026": ("Shukla", 5, "Shravan"),
    "18-08-2026": ("Shukla", 6, "Shravan"),
    "19-08-2026": ("Shukla", 7, "Shravan"),
    "20-08-2026": ("Shukla", 8, "Shravan"),
    "21-08-2026": ("Shukla", 9, "Shravan"),
    "22-08-2026": ("Shukla", 10, "Shravan"),
    "23-08-2026": ("Shukla", 11, "Shravan"),
    "24-08-2026": ("Shukla", 12, "Shravan"),
    "25-08-2026": ("Shukla", 13, "Shravan"),
    "26-08-2026": ("Shukla", 13, "Shravan"),
    "27-08-2026": ("Shukla", 14, "Shravan"),
    "28-08-2026": ("Shukla", 15, "Shravan"),
    "29-08-2026": ("Krishna", 1, "Bhadrapad"),
    "30-08-2026": ("Krishna", 2, "Bhadrapad"),
    "31-08-2026": ("Krishna", 3, "Bhadrapad"),
    # ---- September ----
    "01-09-2026": ("Krishna", 5, "Bhadrapad"),
    "02-09-2026": ("Krishna", 6, "Bhadrapad"),
    "03-09-2026": ("Krishna", 7, "Bhadrapad"),
    "04-09-2026": ("Krishna", 8, "Bhadrapad"),
    "05-09-2026": ("Krishna", 9, "Bhadrapad"),
    "06-09-2026": ("Krishna", 10, "Bhadrapad"),
    "07-09-2026": ("Krishna", 11, "Bhadrapad"),
    "08-09-2026": ("Krishna", 12, "Bhadrapad"),
    "09-09-2026": ("Krishna", 13, "Bhadrapad"),
    "10-09-2026": ("Krishna", 14, "Bhadrapad"),
    "11-09-2026": ("Krishna", 30, "Bhadrapad"),
    "12-09-2026": ("Shukla", 2, "Bhadrapad"),
    "13-09-2026": ("Shukla", 3, "Bhadrapad"),
    "14-09-2026": ("Shukla", 4, "Bhadrapad"),
    "15-09-2026": ("Shukla", 4, "Bhadrapad"),
    "16-09-2026": ("Shukla", 5, "Bhadrapad"),
    "17-09-2026": ("Shukla", 6, "Bhadrapad"),
    "18-09-2026": ("Shukla", 7, "Bhadrapad"),
    "19-09-2026": ("Shukla", 8, "Bhadrapad"),
    "20-09-2026": ("Shukla", 9, "Bhadrapad"),
    "21-09-2026": ("Shukla", 10, "Bhadrapad"),
    "22-09-2026": ("Shukla", 11, "Bhadrapad"),
    "23-09-2026": ("Shukla", 12, "Bhadrapad"),
    "24-09-2026": ("Shukla", 13, "Bhadrapad"),
    "25-09-2026": ("Shukla", 14, "Bhadrapad"),
    "26-09-2026": ("Shukla", 15, "Bhadrapad"),
    "27-09-2026": ("Krishna", 1, "Ashwin"),
    "28-09-2026": ("Krishna", 2, "Ashwin"),
    "29-09-2026": ("Krishna", 3, "Ashwin"),
    "30-09-2026": ("Krishna", 4, "Ashwin"),
    # ---- October ----
    "01-10-2026": ("Krishna", 5, "Ashwin"),
    "02-10-2026": ("Krishna", 6, "Ashwin"),
    "03-10-2026": ("Krishna", 8, "Ashwin"),
    "04-10-2026": ("Krishna", 9, "Ashwin"),
    "05-10-2026": ("Krishna", 10, "Ashwin"),
    "06-10-2026": ("Krishna", 11, "Ashwin"),
    "07-10-2026": ("Krishna", 12, "Ashwin"),
    "08-10-2026": ("Krishna", 13, "Ashwin"),
    "09-10-2026": ("Krishna", 14, "Ashwin"),
    "10-10-2026": ("Krishna", 30, "Ashwin"),
    "11-10-2026": ("Shukla", 1, "Ashwin"),
    "12-10-2026": ("Shukla", 2, "Ashwin"),
    "13-10-2026": ("Shukla", 3, "Ashwin"),
    "14-10-2026": ("Shukla", 4, "Ashwin"),
    "15-10-2026": ("Shukla", 5, "Ashwin"),
    "16-10-2026": ("Shukla", 6, "Ashwin"),
    "17-10-2026": ("Shukla", 7, "Ashwin"),
    "18-10-2026": ("Shukla", 7, "Ashwin"),
    "19-10-2026": ("Shukla", 8, "Ashwin"),
    "20-10-2026": ("Shukla", 9, "Ashwin"),
    "21-10-2026": ("Shukla", 10, "Ashwin"),
    "22-10-2026": ("Shukla", 11, "Ashwin"),
    "23-10-2026": ("Shukla", 12, "Ashwin"),
    "24-10-2026": ("Shukla", 13, "Ashwin"),
    "25-10-2026": ("Shukla", 14, "Ashwin"),
    "26-10-2026": ("Shukla", 15, "Ashwin"),
    "27-10-2026": ("Krishna", 2, "Kartik"),
    "28-10-2026": ("Krishna", 3, "Kartik"),
    "29-10-2026": ("Krishna", 4, "Kartik"),
    "30-10-2026": ("Krishna", 5, "Kartik"),
    "31-10-2026": ("Krishna", 6, "Kartik"),
    # ---- November ----
    "01-11-2026": ("Krishna", 7, "Kartik"),
    "02-11-2026": ("Krishna", 8, "Kartik"),
    "03-11-2026": ("Krishna", 9, "Kartik"),
    "04-11-2026": ("Krishna", 10, "Kartik"),
    "05-11-2026": ("Krishna", 11, "Kartik"),
    "06-11-2026": ("Krishna", 12, "Kartik"),
    "07-11-2026": ("Krishna", 13, "Kartik"),
    "08-11-2026": ("Krishna", 14, "Kartik"),
    "09-11-2026": ("Krishna", 30, "Kartik"),
    "10-11-2026": ("Shukla", 1, "Kartik"),
    "11-11-2026": ("Shukla", 2, "Kartik"),
    "12-11-2026": ("Shukla", 3, "Kartik"),
    "13-11-2026": ("Shukla", 4, "Kartik"),
    "14-11-2026": ("Shukla", 5, "Kartik"),
    "15-11-2026": ("Shukla", 6, "Kartik"),
    "16-11-2026": ("Shukla", 7, "Kartik"),
    "17-11-2026": ("Shukla", 8, "Kartik"),
    "18-11-2026": ("Shukla", 8, "Kartik"),
    "19-11-2026": ("Shukla", 9, "Kartik"),
    "20-11-2026": ("Shukla", 11, "Kartik"),
    "21-11-2026": ("Shukla", 12, "Kartik"),
    "22-11-2026": ("Shukla", 13, "Kartik"),
    "23-11-2026": ("Shukla", 14, "Kartik"),
    "24-11-2026": ("Shukla", 15, "Kartik"),
    "25-11-2026": ("Krishna", 1, "Margshirsh"),
    "26-11-2026": ("Krishna", 2, "Margshirsh"),
    "27-11-2026": ("Krishna", 3, "Margshirsh"),
    "28-11-2026": ("Krishna", 5, "Margshirsh"),
    "29-11-2026": ("Krishna", 6, "Margshirsh"),
    "30-11-2026": ("Krishna", 7, "Margshirsh"),
    # ---- December ----
    "01-12-2026": ("Krishna", 8, "Margshirsh"),
    "02-12-2026": ("Krishna", 9, "Margshirsh"),
    "03-12-2026": ("Krishna", 9, "Margshirsh"),
    "04-12-2026": ("Krishna", 11, "Margshirsh"),
    "05-12-2026": ("Krishna", 12, "Margshirsh"),
    "06-12-2026": ("Krishna", 13, "Margshirsh"),
    "07-12-2026": ("Krishna", 14, "Margshirsh"),
    "08-12-2026": ("Krishna", 30, "Margshirsh"),
    "09-12-2026": ("Shukla", 1, "Margshirsh"),
    "10-12-2026": ("Shukla", 2, "Margshirsh"),
    "11-12-2026": ("Shukla", 2, "Margshirsh"),
    "12-12-2026": ("Shukla", 3, "Margshirsh"),
    "13-12-2026": ("Shukla", 4, "Margshirsh"),
    "14-12-2026": ("Shukla", 5, "Margshirsh"),
    "15-12-2026": ("Shukla", 6, "Margshirsh"),
    "16-12-2026": ("Shukla", 7, "Margshirsh"),
    "17-12-2026": ("Shukla", 8, "Margshirsh"),
    "18-12-2026": ("Shukla", 9, "Margshirsh"),
    "19-12-2026": ("Shukla", 10, "Margshirsh"),
    "20-12-2026": ("Shukla", 11, "Margshirsh"),
    "21-12-2026": ("Shukla", 12, "Margshirsh"),
    "22-12-2026": ("Shukla", 13, "Margshirsh"),
    "23-12-2026": ("Shukla", 14, "Margshirsh"),
    "24-12-2026": ("Krishna", 1, "Paush"),
    "25-12-2026": ("Krishna", 2, "Paush"),
    "26-12-2026": ("Krishna", 3, "Paush"),
    "27-12-2026": ("Krishna", 4, "Paush"),
    "28-12-2026": ("Krishna", 5, "Paush"),
    "29-12-2026": ("Krishna", 6, "Paush"),
    "30-12-2026": ("Krishna", 7, "Paush"),
    "31-12-2026": ("Krishna", 8, "Paush"),
}


def tithi_for_date(date_str):
    """Return a human-readable tithi string for a given 'DD-MM-YYYY' date."""
    info = DAILY_TITHIS_2026.get(date_str)
    if not info:
        return None
    paksha, num, month = info
    name = TITHI_NAMES.get(num, f"Tithi {num}")
    # Special case: Shukla 15 = Purnima, Krishna 15/30 = Amavasya
    if paksha == "Shukla" and num == 15:
        name = "Purnima"
    elif paksha == "Krishna" and num in (15, 30):
        name = "Amavasya"
    return f"{month} {paksha} {name}"


# =============================================================
# 6. Sunrise / sunset table (Indore, India — published on panchang)
# =============================================================
# Reference dates from each month's सूर्योदय / सूर्यास्त box.
# Values are (HH:MM, HH:MM) — local Indian Standard Time.
SUN_REFERENCE_2026 = [
    # ---- January ----
    ("01-01-2026", "07:07", "17:53"),
    ("06-01-2026", "07:08", "17:57"),
    ("11-01-2026", "07:09", "18:00"),
    ("16-01-2026", "07:09", "18:04"),
    ("21-01-2026", "07:09", "18:07"),
    ("26-01-2026", "07:08", "18:11"),
    ("31-01-2026", "07:06", "18:14"),
    # ---- February ----
    ("05-02-2026", "07:04", "18:17"),
    ("10-02-2026", "07:02", "18:20"),
    ("15-02-2026", "06:59", "18:23"),
    ("20-02-2026", "06:55", "18:26"),
    ("25-02-2026", "06:52", "18:28"),
    # ---- March ----
    ("03-03-2026", "06:47", "18:31"),
    ("08-03-2026", "06:43", "18:33"),
    ("12-03-2026", "06:38", "18:35"),
    ("17-03-2026", "06:34", "18:36"),
    ("22-03-2026", "06:29", "18:38"),
    ("27-03-2026", "06:24", "18:40"),
    # ---- April ----
    ("01-04-2026", "06:19", "18:42"),
    ("06-04-2026", "06:15", "18:44"),
    ("11-04-2026", "06:10", "18:46"),
    ("16-04-2026", "06:06", "18:47"),
    ("21-04-2026", "06:02", "18:49"),
    ("26-04-2026", "05:58", "18:51"),
    ("30-04-2026", "05:55", "18:53"),
    # ---- May ----
    ("01-05-2026", "05:54", "18:54"),
    ("06-05-2026", "05:51", "18:56"),
    ("11-05-2026", "05:48", "18:58"),
    ("16-05-2026", "05:46", "19:00"),
    ("21-05-2026", "05:44", "19:03"),
    ("26-05-2026", "05:43", "19:05"),
    ("31-05-2026", "05:42", "19:07"),
    # ---- June ----
    ("05-06-2026", "05:41", "19:09"),
    ("10-06-2026", "05:41", "19:11"),
    ("15-06-2026", "05:42", "19:13"),
    ("20-06-2026", "05:42", "19:14"),
    ("25-06-2026", "05:44", "19:15"),
    ("30-06-2026", "05:45", "19:16"),
    # ---- July ----
    ("05-07-2026", "05:47", "19:16"),
    ("10-07-2026", "05:49", "19:15"),
    ("15-07-2026", "05:51", "19:15"),
    ("20-07-2026", "05:53", "19:13"),
    ("25-07-2026", "05:55", "19:11"),
    ("30-07-2026", "05:57", "19:09"),
    # ---- August ----
    ("04-08-2026", "05:59", "19:06"),
    ("09-08-2026", "06:01", "19:03"),
    ("14-08-2026", "06:03", "18:59"),
    ("19-08-2026", "06:05", "18:56"),
    ("24-08-2026", "06:06", "18:51"),
    ("29-08-2026", "06:08", "18:47"),
    # ---- September ----
    ("03-09-2026", "06:10", "18:42"),
    ("08-09-2026", "06:11", "18:37"),
    ("13-09-2026", "06:13", "18:32"),
    ("18-09-2026", "06:14", "18:27"),
    ("23-09-2026", "06:16", "18:22"),
    ("28-09-2026", "06:17", "18:17"),
    ("30-09-2026", "06:18", "18:15"),
    # ---- October ----
    ("03-10-2026", "06:19", "18:12"),
    ("08-10-2026", "06:20", "18:08"),
    ("13-10-2026", "06:22", "18:03"),
    ("18-10-2026", "06:24", "17:59"),
    ("23-10-2026", "06:27", "17:55"),
    ("28-10-2026", "06:29", "17:52"),
    # ---- November ----
    ("02-11-2026", "06:32", "17:48"),
    ("07-11-2026", "06:34", "17:46"),
    ("12-11-2026", "06:38", "17:44"),
    ("17-11-2026", "06:41", "17:42"),
    ("22-11-2026", "06:44", "17:41"),
    ("27-11-2026", "06:47", "17:41"),
    # ---- December ----
    ("02-12-2026", "06:51", "17:41"),
    ("07-12-2026", "06:54", "17:42"),
    ("12-12-2026", "06:57", "17:43"),
    ("17-12-2026", "07:00", "17:45"),
    ("22-12-2026", "07:03", "17:48"),
    ("27-12-2026", "07:05", "17:50"),
    ("30-12-2026", "07:06", "17:52"),
]


def _hhmm_to_minutes(s):
    h, m = s.split(":")
    return int(h) * 60 + int(m)


def _minutes_to_hhmm(mins):
    mins = int(round(mins))
    return f"{mins // 60:02d}:{mins % 60:02d}"


def sun_times_for_date(date_str):
    """Return (sunrise, sunset) as 'HH:MM' strings for a given date.
    Uses linear interpolation between reference dates in SUN_REFERENCE_2026.
    """
    from datetime import datetime
    try:
        target = datetime.strptime(date_str, "%d-%m-%Y").date()
    except ValueError:
        return (None, None)

    # Turn reference list into sorted (date, rise, set)
    refs = []
    for ds, r, s in SUN_REFERENCE_2026:
        d = datetime.strptime(ds, "%d-%m-%Y").date()
        refs.append((d, _hhmm_to_minutes(r), _hhmm_to_minutes(s)))

    # Before the first ref or after the last: clamp
    if target <= refs[0][0]:
        return (_minutes_to_hhmm(refs[0][1]), _minutes_to_hhmm(refs[0][2]))
    if target >= refs[-1][0]:
        return (_minutes_to_hhmm(refs[-1][1]), _minutes_to_hhmm(refs[-1][2]))

    # Find surrounding pair
    for i in range(len(refs) - 1):
        d0, r0, s0 = refs[i]
        d1, r1, s1 = refs[i + 1]
        if d0 <= target <= d1:
            total = (d1 - d0).days or 1
            frac = (target - d0).days / total
            rise = r0 + (r1 - r0) * frac
            set_ = s0 + (s1 - s0) * frac
            return (_minutes_to_hhmm(rise), _minutes_to_hhmm(set_))

    return (None, None)
