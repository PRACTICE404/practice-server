# Generated by Django 5.1.1 on 2024-09-26 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_postbranch_options_remove_post_branch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='posttag',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.postbranch'),
        ),
    ]
