# Generated by Django 3.2.5 on 2022-01-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0010_alter_details_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='details',
            name='anaemia',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='details',
            name='creatinine_phosphokinase',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='details',
            name='diabetes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='details',
            name='ejection_fraction',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='details',
            name='high_blood_pressure',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='details',
            name='nick_name',
            field=models.CharField(default='user', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='platelets',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='details',
            name='serum_creatinine',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='details',
            name='serum_sodium',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='details',
            name='sex',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='details',
            name='smoking',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='details',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]