from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandir', '0020_auto_20220813_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='mandir',
            name='logo',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='logos/',
                verbose_name='Temple logo / Tirthankar idol',
                help_text='Square image of the Tirthankar idol; shown as the temple logo in the navigation.',
            ),
        ),
    ]
