# Generated by Django 3.2.5 on 2022-01-07 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0005_auto_20220107_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
