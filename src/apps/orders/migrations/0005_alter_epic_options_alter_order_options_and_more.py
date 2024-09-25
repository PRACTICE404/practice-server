# Generated by Django 5.1.1 on 2024-09-14 21:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_task_description_task_estimate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='epic',
            options={'verbose_name_plural': '(B) Epics'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': '(A) Orders'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name_plural': '(C) Tasks'},
        ),
        migrations.AlterField(
            model_name='epic',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='epics', to='orders.order'),
        ),
        migrations.AlterField(
            model_name='task',
            name='epic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='orders.epic'),
        ),
    ]
