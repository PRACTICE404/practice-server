# Generated by Django 5.1.1 on 2025-02-04 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialnetworkaccount',
            name='title',
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
    ]
