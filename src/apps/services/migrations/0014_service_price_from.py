# Generated by Django 5.1.1 on 2025-02-04 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_alter_service_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='price_from',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
