# Generated by Django 2.2.12 on 2020-06-04 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0007_addonreviewerflags_notified_about_auto_approval_delay'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='addoncategory',
            name='feature_addon_idx',
        ),
        migrations.RemoveField(
            model_name='addoncategory',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='addoncategory',
            name='feature_locales',
        ),
    ]
