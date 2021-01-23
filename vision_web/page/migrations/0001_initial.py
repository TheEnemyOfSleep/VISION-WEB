# Generated by Django 3.1.5 on 2021-01-23 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ButtonElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attrs', models.TextField(blank=True)),
                ('style', models.TextField(blank=True)),
                ('script', models.TextField(blank=True)),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LabelElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attrs', models.TextField(blank=True)),
                ('style', models.TextField(blank=True)),
                ('script', models.TextField(blank=True)),
                ('label', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElementsRel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_type', models.CharField(choices=[('button_elem', 'Button'), ('label_elem', 'Label')], default='button_elem', max_length=15)),
                ('sorting', models.PositiveIntegerField(default=0)),
                ('button_elem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elements', to='page.buttonelement')),
                ('label_elem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elements', to='page.labelelement')),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('sorting', models.PositiveIntegerField(default=0)),
                ('content', models.TextField()),
                ('elements', models.ManyToManyField(blank=True, to='page.ElementsRel')),
                ('sub_component', models.ManyToManyField(blank=True, related_name='root', to='page.Component')),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('sorting', models.PositiveIntegerField(default=0)),
                ('id_attr', models.CharField(blank=True, max_length=100)),
                ('classes', models.CharField(blank=True, max_length=200)),
                ('extra_attrs', models.TextField(blank=True)),
                ('style', models.TextField(blank=True)),
                ('note', models.CharField(blank=True, max_length=150)),
                ('components', models.ManyToManyField(blank=True, to='page.Component')),
                ('elements', models.ManyToManyField(blank=True, to='page.ElementsRel')),
                ('sub_block', models.ManyToManyField(blank=True, related_name='root', to='page.Block')),
            ],
            options={
                'verbose_name': 'block',
                'verbose_name_plural': 'block',
                'ordering': ['-sorting'],
            },
        ),
    ]
