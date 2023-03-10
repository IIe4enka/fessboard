# Generated by Django 4.1.5 on 2023-01-16 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='???')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_foreign', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sphere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='???')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название типа компании')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='???')),
                ('logo', models.TextField(verbose_name='???')),
                ('status', models.CharField(choices=[(1, 'bachelor'), (2, 'master')], default='bachelor', max_length=15, verbose_name='Статус')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.region', verbose_name='???')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=255, verbose_name='???')),
                ('name', models.CharField(max_length=255, verbose_name='???')),
                ('midname', models.CharField(max_length=255, verbose_name='???')),
                ('bachelors_start_year', models.TextField(blank=True, null=True, verbose_name='???')),
                ('masters_start_year', models.TextField(blank=True, null=True, verbose_name='???')),
                ('is_banned', models.BooleanField(default=False, verbose_name='Забанен ли игрок')),
                ('groups', models.ManyToManyField(to='homepage.group', verbose_name='Группы')),
                ('university', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.university', verbose_name='???')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование компании')),
                ('website', models.TextField(verbose_name='Активный вебсайт компании')),
                ('sphere', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.sphere', verbose_name='Сфера работы компании')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.type', verbose_name='Тип компании')),
            ],
        ),
    ]
