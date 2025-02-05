# Generated by Django 5.1.1 on 2025-02-04 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_websitesettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitesettings',
            name='location',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='websitesettings',
            name='slogan',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
