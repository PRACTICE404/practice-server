# Generated by Django 5.1.1 on 2024-09-25 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_technology_options_alter_portfolio_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='technologies',
            field=models.ManyToManyField(blank=True, to='services.technology'),
        ),
    ]
