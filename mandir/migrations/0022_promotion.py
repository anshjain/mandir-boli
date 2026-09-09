# Generated migration for Promotion model

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mandir', '0021_mandir_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo_type', models.CharField(
                    choices=[
                        ('notice',   'Notice / Announcement'),
                        ('event',    'Event'),
                        ('donation', 'Donation Appeal'),
                        ('festival', 'Festival'),
                        ('other',    'Other'),
                    ],
                    default='notice', max_length=20, verbose_name='Type'
                )),
                ('title',      models.CharField(max_length=200, verbose_name='Title')),
                ('body',       models.TextField(verbose_name='Body', help_text='Main text shown on the card.')),
                ('image',      models.ImageField(blank=True, null=True, upload_to='promotions/', verbose_name='Banner image')),
                ('cta_label',  models.CharField(blank=True, max_length=60, null=True, verbose_name='Button label')),
                ('cta_url',    models.URLField(blank=True, null=True, verbose_name='Button URL')),
                ('start_date', models.DateField(verbose_name='Show from')),
                ('end_date',   models.DateField(verbose_name='Show until')),
                ('priority',   models.PositiveSmallIntegerField(default=0, verbose_name='Priority')),
                ('is_active',  models.BooleanField(default=True, verbose_name='Active')),
                ('created',    models.DateTimeField(auto_now_add=True)),
                ('mandir', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='promotions',
                    to='mandir.mandir',
                    verbose_name='mandir'
                )),
            ],
            options={
                'verbose_name':        'Promotion',
                'verbose_name_plural': 'Promotions',
                'ordering':            ['-priority', '-start_date'],
            },
        ),
    ]
