/* --------------------------------------------------------------------
   Digambar Jain Calendar — client-side script
   On each page load:
     1. Fetch /notifications/today
     2. If today matches any of the user's subscribed categories,
        fire a desktop notification + on-page banner.
-------------------------------------------------------------------- */
(function () {
    "use strict";

    const enableBtn = document.getElementById("enable-notif");
    const statusEl  = document.getElementById("notif-status");

    function setStatus(msg) { if (statusEl) statusEl.textContent = msg; }

    if (enableBtn) {
        if (!("Notification" in window)) {
            enableBtn.disabled = true;
            setStatus("Not supported in this browser.");
        } else if (Notification.permission === "granted") {
            setStatus("Notifications are enabled.");
        } else if (Notification.permission === "denied") {
            setStatus("Blocked — enable in browser settings.");
        }
        enableBtn.addEventListener("click", function () {
            Notification.requestPermission().then(function (p) {
                if (p === "granted") {
                    setStatus("Enabled — you'll get alerts on subscribed days.");
                    try {
                        new Notification("Jai Jinendra 🙏", {
                            body: "Notifications are now enabled for your Jain calendar.",
                        });
                    } catch (e) { /* silent */ }
                } else {
                    setStatus("Permission: " + p);
                }
            });
        });
    }

    function showBanner(html) {
        if (document.querySelector(".js-today-banner")) return;
        const bar = document.createElement("div");
        bar.className = "js-today-banner";
        bar.innerHTML =
            '<strong style="color:#991b1b;font-family:\'Cormorant Garamond\',serif;font-size:17px">🔔 Today on the Jain Calendar</strong>' +
            '<div style="margin-top:7px">' + html + "</div>" +
            '<button style="margin-top:10px;padding:6px 14px;border:0;' +
            'background:linear-gradient(135deg,#f4a535,#c96611);color:#fff;' +
            'border-radius:8px;cursor:pointer;font-weight:600" ' +
            'onclick="this.parentElement.remove()">Dismiss</button>';
        document.body.appendChild(bar);
    }

    function pushNotification(title, body) {
        if ("Notification" in window && Notification.permission === "granted") {
            try { new Notification(title, { body: body }); } catch (e) { /* silent */ }
        }
    }

    fetch("/notifications/today")
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (data) {
            if (!data) return;

            const matched = data.matched || [];
            // Only show banner if user has active subscriptions that matched
            if (!matched.length) return;

            const lines = matched.map(function (e) { return "• " + e.label; });

            showBanner(lines.join("<br>"));

            const summary = matched[0].label +
                (matched.length > 1 ? " (+" + (matched.length - 1) + " more)" : "");
            pushNotification("Jain Calendar — " + data.today, summary);
        })
        .catch(function () { /* non-fatal */ });
})();
