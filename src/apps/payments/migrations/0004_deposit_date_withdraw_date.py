# Generated by Django 5.1.1 on 2024-10-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_depositdistribution_deposit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='withdraw',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
