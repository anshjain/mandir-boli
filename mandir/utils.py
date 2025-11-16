import urllib
import simplejson as json
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from mandir.constants import SMS_API_KEY, GENERIC_MSG, SMS_URL


def send_normal_sms(numbers, message=GENERIC_MSG, sender='TXTLCL'):
    """Will send an sms to end user. """
    return True


def redirect_to_record(phone_number):
    url = reverse('record-list') + f"?phone_number={phone_number}#record"
    return HttpResponseRedirect(url)


def build_payment_detail(mode, detail):
    if not detail:
        return ""
    mapping = {
        "Online": f"Transaction Id: {detail}",
        "Cheque": f"Cheque Number: {detail}",
    }
    return mapping.get(mode, "")


def build_email_recipients(send_to, mandir_email):
    recipients = list(filter(None, send_to))
    recipients.append(mandir_email)
    recipients.extend(settings.ADMIN_EMAILS)
    return recipients


def compute_paid_amount(records, partial_payment):
    """Handle logic for partial and full payment."""
    if len(records) > 1:
        return sum(record.amount if not record.remaining_amt
                   else record.remaining_amt
                   for record in records)

    # partial payment overrides everything
    if partial_payment:
        return int(partial_payment)

    # otherwise use remaining_amt or full amount
    return records[0].remaining_amt or records[0].amount


def update_records(records, paid_amount, partial_payment, payment_date, transaction_id, email_content):

    for record in records:
        if partial_payment:
            # Initialize remaining_amt properly
            if record.remaining_amt == 0 and not record.paid:
                record.remaining_amt = record.amount

            partial_string = f"Date: {payment_date.date()} Amount: {paid_amount}<br />"

            # Avoid overpayment
            if paid_amount > record.remaining_amt:
                raise ValueError("Partial payment exceeds remaining amount.")

            # Deduct amount
            record.remaining_amt -= paid_amount

            # Update description
            if not record.description:
                record.description = "Payment breakdown:<br>"
            record.description += partial_string

            # Mark as fully paid if completed
            if record.remaining_amt == 0:
                record.paid = True

        else:
            # full payment
            record.paid = True
            record.remaining_amt = 0
            record.description = email_content

        record.transaction_id = transaction_id or 'Cash'
        record.payment_date = payment_date
        record.save()


def update_pan_card(records, pan_card):
    """Update PAN for the account if it is not masked."""
    if pan_card and "*" not in pan_card:
        account = records[0].account
        account.pan_card = pan_card
        account.save()


def send_payment_email(sender_name, content, recipients):

    email = EmailMessage(
        "Thanks for the Payment",
        content,
        sender_name,
        recipients,
    )
    email.content_subtype = "html"
    email.send()
