// Carousel
var myIndex = 0;
function carousel() {
    var x = document.getElementsByClassName("hero-slide");
    if (!x.length) return;
    for (var i = 0; i < x.length; i++) x[i].style.display = "none";
    myIndex++;
    if (myIndex > x.length) myIndex = 1;
    x[myIndex - 1].style.display = "block";
    setTimeout(carousel, 4000);
}

// Close modals on backdrop click
window.addEventListener('click', function(e) {
    var em = document.getElementById('EmailModal');
    var cm = document.getElementById('customConfirmation');
    if (em && e.target === em) close_update();
    if (cm && e.target === cm) closeConfirmationModel();
});

var running_total = 0, paid_ids = [];
var _modal_original_amount = 0;  // tracked for partial-payment math

function display_model(record_id, amount, date, partial, pan_card) {
    var modal = document.getElementById('EmailModal');
    if (!modal) return;
    document.getElementById('record_id').value = record_id;
    modal.classList.add('open');

    var ffPartial = document.getElementById('ff_partial_payment');
    var partInput = document.getElementById('id_partial_payment');
    var amtSpan   = document.getElementById('amount_val');
    var orgSpan   = document.getElementById('org_amount_val');
    var dateSpan  = document.getElementById('boli_date');
    var phoneHid  = document.getElementById('phone_number');
    var pNum      = document.getElementById('pNumber');

    var amtNum = parseFloat(amount) || 0;
    _modal_original_amount = amtNum;

    if (partial === 'PP') {
        // Partial payment: show input, start "amount paid" at 0
        if (ffPartial) ffPartial.style.display = 'block';
        if (partInput) { partInput.required = true; partInput.value = ''; }
        if (amtSpan)   amtSpan.innerHTML = '0.00';
    } else {
        // Full payment: hide partial input, show full amount as paid
        if (ffPartial) ffPartial.style.display = 'none';
        if (partInput) { partInput.required = false; partInput.value = ''; }
        if (amtSpan)   amtSpan.innerHTML = amtNum.toFixed(2);
    }
    if (orgSpan)  orgSpan.innerHTML  = amtNum.toFixed(2);
    if (dateSpan) dateSpan.innerHTML = date;
    if (phoneHid && pNum) phoneHid.value = pNum.value;

    // Reset payment mode UI to default (Cash → hide transaction id)
    var modeSel = document.getElementById('id_payment_mode');
    if (modeSel) modeSel.value = 'Cash';
    var ffId = document.getElementById('ff_id_details');
    if (ffId) ffId.style.display = 'none';

    var panField = document.getElementById('id_pan_card');
    if (panField && pan_card && pan_card !== 'None' && pan_card !== '') {
        panField.value = '********'; panField.readOnly = true;
    } else if (panField) {
        panField.value = ''; panField.readOnly = false;
    }
}

// Toggle transaction-id field based on selected payment mode
function payment_md() {
    var modeSel = document.getElementById('id_payment_mode');
    var ffId    = document.getElementById('ff_id_details');
    if (!modeSel || !ffId) return;
    if (modeSel.value === 'Cash') {
        ffId.style.display = 'none';
    } else {
        ffId.style.display = 'block';
    }
}

// Recalculate "Amount Paid" display as the user types into the partial-payment input
function payment_cal() {
    var partInput = document.getElementById('id_partial_payment');
    var amtSpan   = document.getElementById('amount_val');
    if (!partInput || !amtSpan) return;
    var v = parseFloat(partInput.value);
    if (isNaN(v) || v < 0) v = 0;
    if (v > _modal_original_amount) {
        // Don't let user pay more than the outstanding amount
        v = _modal_original_amount;
        partInput.value = v;
    }
    amtSpan.innerHTML = v.toFixed(2);
}

function close_update() {
    var modal = document.getElementById('EmailModal');
    if (modal) modal.classList.remove('open');
    paid_ids = []; running_total = 0;
    document.querySelectorAll('input[type=checkbox]').forEach(function(c){ c.checked = false; });
    var t = document.getElementById('chk_total'); if (t) t.textContent = '₹0';
    var b = document.getElementById('chb_amt');   if (b) b.disabled = true;
}

function update(checkbox) {
    var b = document.getElementById('chb_amt');
    if (b) b.disabled = false;
    if (checkbox.checked) { running_total += parseInt(checkbox.value); paid_ids.push(checkbox.id); }
    else {
        running_total -= parseInt(checkbox.value);
        paid_ids = paid_ids.filter(function(id){ return id !== checkbox.id; });
        if (running_total === 0 && b) b.disabled = true;
    }
    var t = document.getElementById('chk_total'); if (t) t.textContent = '₹' + running_total;
    var s = document.getElementById('smtArrId');  if (s) s.value = paid_ids;
}

function openGooglePay(amount) {
    var amt = String(amount).replace('₹','').trim();
    if (amt && amt !== '0') window.open('upi://pay?pa=8799928255@mahb&pn=susdigamberjainmadir&am=' + amt + '&cu=INR','_blank');
    else alert('Please select at least one record.');
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
    window.open('https://api.whatsapp.com/send?phone=' + phone, '', 'toolbar=no,status=no,menubar=no,scrollbars=no,resizable=no,height=500,width=657');
}

function get_description() {
    var phone = document.getElementById('id_phone_number');
    if (phone && phone.value.length >= 10 && typeof $ !== 'undefined') {
        $.get('/get/description/', {phone_number: phone.value}, function(data) {
            var d = document.getElementById('id_description');
            if (d && data.description) d.value = data.description;
        }, 'json');
    }
}

var pNum = document.getElementById('pNumber');
if (pNum) {
    pNum.addEventListener('keyup', function(e) {
        if (e.keyCode === 13) window.open('/search/?phone_number=' + pNum.value + '#record', '_self');
    });
}
