# Generated by Django 4.2.5 on 2023-10-19 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=90)),
                ('dni', models.CharField(max_length=8, unique=True)),
                ('matricula', models.CharField(unique=True)),
                ('correoElectronico', models.EmailField(max_length=256)),
            ],
            options={
                'ordering': ['nombre', 'apellido'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ascesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=90)),
                ('cuil', models.CharField(max_length=11, unique=True)),
                ('curriculum', models.FileField(upload_to='', verbose_name='Files/CurriculumAscesor/')),
            ],
            options={
                'ordering': ['nombre', 'apellido'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=90)),
                ('cuil', models.CharField(max_length=11, unique=True)),
            ],
            options={
                'ordering': ['nombre', 'apellido'],
                'abstract': False,
            },
        ),
    ]
