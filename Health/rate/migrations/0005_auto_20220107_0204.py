# Generated by Django 3.2.5 on 2022-01-07 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0004_auto_20220106_2313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='f_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='details',
            old_name='l_name',
            new_name='last_name',
        ),
    ]
