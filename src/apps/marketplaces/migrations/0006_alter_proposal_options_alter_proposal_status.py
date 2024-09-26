# Generated by Django 5.1.1 on 2024-09-25 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplaces', '0005_proposal_customer_feedback'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proposal',
            options={'ordering': ('status', 'date_sent', 'id')},
        ),
        migrations.AlterField(
            model_name='proposal',
            name='status',
            field=models.CharField(choices=[('1', 'Negotiation'), ('2', 'Pending'), ('3', 'Succeeded'), ('4', 'Expired')], default='pending', max_length=32),
        ),
    ]
