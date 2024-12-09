# Generated by Django 5.1.1 on 2024-11-10 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance_manager', '0001_initial'),
        ('payments', '0004_deposit_date_withdraw_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DepositSummary',
        ),
        migrations.CreateModel(
            name='DepositSummaryByDays',
            fields=[
            ],
            options={
                'verbose_name_plural': ' Deposit summary (by days)',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('payments.deposit',),
        ),
        migrations.CreateModel(
            name='DepositSummaryByMonths',
            fields=[
            ],
            options={
                'verbose_name_plural': ' Deposit summary (by months)',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('payments.deposit',),
        ),
    ]
