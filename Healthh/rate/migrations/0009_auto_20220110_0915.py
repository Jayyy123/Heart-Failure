# Generated by Django 3.2.5 on 2022-01-10 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0008_auto_20220110_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='age',
        ),
        migrations.RemoveField(
            model_name='details',
            name='anaemia',
        ),
        migrations.RemoveField(
            model_name='details',
            name='creatinine_phosphokinase',
        ),
        migrations.RemoveField(
            model_name='details',
            name='diabetes',
        ),
        migrations.RemoveField(
            model_name='details',
            name='ejection_fraction',
        ),
        migrations.RemoveField(
            model_name='details',
            name='high_blood_pressure',
        ),
        migrations.RemoveField(
            model_name='details',
            name='platelets',
        ),
        migrations.RemoveField(
            model_name='details',
            name='serum_creatinine',
        ),
        migrations.RemoveField(
            model_name='details',
            name='serum_sodium',
        ),
        migrations.RemoveField(
            model_name='details',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='details',
            name='smoking',
        ),
        migrations.RemoveField(
            model_name='details',
            name='time',
        ),
    ]