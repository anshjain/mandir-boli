"""
Data migration — seeds the Janganna 2027 promotion so it appears immediately
on the home page without any manual admin entry.
"""
from django.db import migrations
from datetime import date


def seed_promotion(apps, schema_editor):
    Promotion = apps.get_model('mandir', 'Promotion')
    Mandir    = apps.get_model('mandir', 'Mandir')

    # Apply to every mandir in the database
    for mandir in Mandir.objects.all():
        Promotion.objects.get_or_create(
            mandir=mandir,
            title='जनगणना 2027 — जैन धर्म है, जाति नहीं',
            defaults=dict(
                promo_type='notice',
                body=(
                    "🙏 जय जिनेन्द्र\n\n"
                    "जनगणना 2027 का दूसरा चरण (Phase 2) — यानी Population Enumeration — "
                    "जल्द शुरू होने वाला है। इस चरण में घर-घर जाकर धर्म और जाति, दोनों "
                    "अलग-अलग पूछे जाएंगे।\n\n"
                    "याद रखिए — जैन एक धर्म है, जाति नहीं।\n\n"
                    "फॉर्म में:\n"
                    "✅ प्रश्न 9 (धर्म) में लिखें — जैन\n"
                    "✅ प्रश्न 10 (जाति) में लिखें — अपनी असली जाति\n\n"
                    "दोनों अलग सवाल हैं, इन्हें मिलाना नहीं है।\n\n"
                    "महावीर को धर्म से जोड़िये, जाति से नहीं। 🙏\n\n"
                    "📲 अभी शेयर कीजिए — अपने परिवार, ग्रुप में।"
                ),
                image='promotions/janganna_2027.jpeg',
                cta_label='Share Now',
                cta_url='https://wa.me/?text=जैन+धर्म+है,+जाति+नहीं+–+जनगणना+2027',
                start_date=date(2026, 9, 1),
                end_date=date(2027, 3, 31),
                priority=10,
                is_active=True,
            )
        )


def remove_promotion(apps, schema_editor):
    Promotion = apps.get_model('mandir', 'Promotion')
    Promotion.objects.filter(title='जनगणना 2027 — जैन धर्म है, जाति नहीं').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('mandir', '0022_promotion'),
    ]

    operations = [
        migrations.RunPython(seed_promotion, remove_promotion),
    ]
