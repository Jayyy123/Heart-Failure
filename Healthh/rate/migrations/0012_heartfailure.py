# Generated by Django 3.2.5 on 2022-02-11 14:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0011_auto_20220119_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeartFailure',
            fields=[
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=50)),
                ('result', models.IntegerField()),
                ('stamp', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
