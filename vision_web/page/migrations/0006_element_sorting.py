# Generated by Django 3.1.5 on 2021-01-19 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_auto_20210118_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='sorting',
            field=models.IntegerField(default=0),
        ),
    ]