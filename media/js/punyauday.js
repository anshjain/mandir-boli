/* ================================================================
   PunyaUday Fund — punyauday.js
   ================================================================ */

/* ── CAROUSEL ────────────────────────────────────────────────── */
var _si = 0, _st = null;

/* Hide ALL slides the moment this script is parsed — before first paint */
(function () {
    var s = document.getElementsByClassName('hero-slide');
    for (var i = 0; i < s.length; i++) {
        s[i].style.display = 'none';
        s[i].style.opacity = '0';
    }
})();

function carousel() {
    var slides = document.getElementsByClassName('hero-slide');
    if (!slides.length) return;

    /* hide all */
    for (var i = 0; i < slides.length; i++) {
        slides[i].style.display = 'none';
        slides[i].style.opacity = '0';
    }

    /* advance index */
    _si = (_si % slides.length) + 1;
    var cur = slides[_si - 1];

    /* show + fade in */
    cur.style.display = 'block';
    cur.style.opacity = '0';
    cur.style.transition = 'opacity 0.5s ease';
    /* force reflow so transition fires */
    void cur.offsetWidth;
    cur.style.opacity = '1';

    if (_st) clearTimeout(_st);
    _st = setTimeout(carousel, 4500);
}

/* ── MODALS ──────────────────────────────────────────────────── */
window.addEventListener('click', function (e) {
    var em = document.getElementById('EmailModal');
    var cm = document.getElementById('customConfirmation');
    var wa = document.getElementById('waModal');
    if (em && e.target === em) close_update();
    if (cm && e.target === cm) closeConfirmationModel();
    if (wa && e.target === wa) wa.classList.remove('open');
});

var running_total = 0, paid_ids = [];

function display_model(record_id, amount, date, partial, pan_card) {
    var modal = document.getElementById('EmailModal');
    if (!modal) return;
    document.getElementById('record_id').value = record_id;
    modal.classList.add('open');
    var partInput = document.getElementById('id_partial_payment');
    var amtSpan   = document.getElementById('amount_val');
    var orgSpan   = document.getElementById('org_amount_val');
    var dateSpan  = document.getElementById('boli_date');
    var phoneHid  = document.getElementById('phone_number');
    var pNum      = document.getElementById('pNumber');
    if (partial === 'PP') {
        if (partInput) { partInput.style.display = 'block'; partInput.required = true; }
        if (amtSpan) amtSpan.innerHTML = '0.00';
    } else {
        if (partInput) { partInput.style.display = 'none'; partInput.required = false; }
        if (amtSpan) amtSpan.innerHTML = amount + '.00';
    }
    if (orgSpan)  orgSpan.innerHTML  = amount + '.00';
    if (dateSpan) dateSpan.innerHTML = date;
    if (phoneHid && pNum) phoneHid.value = pNum.value;
    var panField = document.getElementById('id_pan_card');
    if (panField && pan_card !== 'None') { panField.value = '********'; panField.readOnly = true; }
}

function close_update() {
    var modal = document.getElementById('EmailModal');
    if (modal) modal.classList.remove('open');
    paid_ids = []; running_total = 0;
    document.querySelectorAll('input[type=checkbox]').forEach(function (c) { c.checked = false; });
    var t = document.getElementById('chk_total'); if (t) t.textContent = '₹0';
    var b = document.getElementById('chb_amt');   if (b) b.disabled = true;
}

function update(checkbox) {
    var b = document.getElementById('chb_amt');
    if (b) b.disabled = false;
    if (checkbox.checked) {
        running_total += parseInt(checkbox.value); paid_ids.push(checkbox.id);
    } else {
        running_total -= parseInt(checkbox.value);
        paid_ids = paid_ids.filter(function (id) { return id !== checkbox.id; });
        if (running_total === 0 && b) b.disabled = true;
    }
    var t = document.getElementById('chk_total'); if (t) t.textContent = '₹' + running_total;
    var s = document.getElementById('smtArrId');  if (s) s.value = paid_ids;
}

function openGooglePay(amount) {
    var amt = String(amount).replace('₹', '').trim();
    if (amt && amt !== '0') {
        window.open('upi://pay?pa=8799928255@mahb&pn=susdigamberjainmadir&am=' + amt + '&cu=INR', '_blank');
    } else { alert('Please select at least one record.'); }
}

function confirmationUserAction(amount) {
    var v = document.getElementById('confirm_val'); if (v) v.innerHTML = amount + '.00';
    var m = document.getElementById('customConfirmation'); if (m) m.classList.add('open');
}

function openModelBox(record_id, amount, date, partial, pan_card) {
    var m = document.getElementById('customConfirmation'); if (m) m.classList.remove('open');
    display_model(record_id, amount, date, partial, pan_card);
}

function closeConfirmationModel() {
    var m = document.getElementById('customConfirmation'); if (m) m.classList.remove('open');
    var c = document.getElementById('paid_chk'); if (c) c.checked = false;
}

function Openwhatsapp(phone) {
    window.open('https://api.whatsapp.com/send?phone=' + phone, '',
        'toolbar=no,status=no,menubar=no,scrollbars=no,resizable=no,height=500,width=657');
}

function get_description() {
    var phone = document.getElementById('id_phone_number');
    if (phone && phone.value.length >= 10 && typeof $ !== 'undefined') {
        $.get('/get/description/', { phone_number: phone.value }, function (data) {
            var d = document.getElementById('id_description');
            if (d && data.description) d.value = data.description;
        }, 'json');
    }
}

var pNum = document.getElementById('pNumber');
if (pNum) {
    pNum.addEventListener('keyup', function (e) {
        if (e.keyCode === 13) {
            window.open('/search/?phone_number=' + pNum.value + '#record', '_self');
        }
    });
}
