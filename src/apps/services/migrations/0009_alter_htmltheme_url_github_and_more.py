# Generated by Django 5.1.1 on 2025-01-08 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_htmltheme_portfolio_html_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htmltheme',
            name='url_github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='htmltheme',
            name='url_themeforest',
            field=models.URLField(blank=True, null=True),
        ),
    ]
