# Generated by Django 5.1.1 on 2025-02-04 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_rename_clients_stats_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultation_price', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
