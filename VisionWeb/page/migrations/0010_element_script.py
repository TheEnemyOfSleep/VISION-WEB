# Generated by Django 3.1.5 on 2021-01-19 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0009_auto_20210119_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='script',
            field=models.TextField(blank=True),
        ),
    ]
