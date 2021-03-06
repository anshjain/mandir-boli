import csv

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from datetime import date, timedelta

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.mail import EmailMessage
from django.template.loader import get_template

from mandir.models import Record, Mandir


class Command(BaseCommand):
    help = 'Generate records CSV file !!'

    def handle(self, *args, **options):
        mandirs = Mandir.objects.filter(status=True)
        for mandir in mandirs:
            self.create_records_csv(mandir)

    def create_records_csv(self, mandir):
        """
        This method will create a CSV file for last month and send it over to mandir contact email address
        will try to send a notification whtsapp contact number as well.
        :param mandir_id:
        """
        prev = date.today().replace(day=1) - timedelta(days=1)
        records = Record.objects.filter(mandir=mandir, paid=True,
                                        payment_date__month=7, payment_date__year=prev.year)
        csvfile = StringIO()
        csvwriter = csv.writer(csvfile)

        if records:
            csvwriter.writerow(["Phone Number", "Name", "Amount", "Boli Date", "Payment Date", "Transaction Id"])
            for record in records:
                description = record.account.description
                if not description:
                    description = record.description
                name = description.split('\n')[0]
                csvwriter.writerow([record.account.phone_number, name, record.amount, record.boli_date, record.payment_date, record.transaction_id])
            month = 'July' #prev.strftime("%B")
            subject_line = "{},{} paid records".format(month, prev.year)
            email_add = [mandir.email]
            email_add.extend(settings.ADMIN_EMAILS)
            template = get_template('report_template.txt')
            content = template.render({'month': month})
            message = EmailMessage(
                subject_line, content, mandir.name, email_add,
            )
            file_name = '{}-{}-records.csv'.format(mandir.name, month)
            message.attach(file_name, csvfile.getvalue(), 'text/csv')
            message.send()

        # delete all records
        # records.delete()
        print("End cron job")