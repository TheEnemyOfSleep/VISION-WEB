# Generated by Django 3.1.5 on 2021-01-18 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_auto_20210118_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='element',
            name='extra_attrs',
        ),
        migrations.AlterField(
            model_name='block',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='sorting',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='element',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]