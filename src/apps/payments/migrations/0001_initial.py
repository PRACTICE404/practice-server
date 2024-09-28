# Generated by Django 5.1.1 on 2024-09-28 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=12)),
                ('code', models.CharField(max_length=8)),
            ],
            options={
                'verbose_name_plural': '(C) Currencies',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=48)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.currency')),
            ],
            options={
                'verbose_name_plural': '(A) Accounts',
            },
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('value', models.PositiveIntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.account')),
            ],
            options={
                'verbose_name_plural': '(B.A) Deposit',
            },
        ),
        migrations.CreateModel(
            name='DepositDistribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('value', models.PositiveIntegerField()),
                ('deposit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.deposit')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Swap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('value_from', models.PositiveIntegerField()),
                ('value_to', models.PositiveIntegerField()),
                ('account_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swap_from', to='payments.account')),
                ('account_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swap_to', to='payments.account')),
            ],
            options={
                'verbose_name_plural': '(B.C) Swap',
            },
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('value', models.PositiveIntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.account')),
            ],
            options={
                'verbose_name_plural': '(B.B) Withdraw',
            },
        ),
    ]
