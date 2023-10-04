# Generated by Django 4.2.5 on 2023-10-03 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0002_alter_alumno_options_alter_docente_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComicionDeSeguimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroResolucion', models.CharField(max_length=15, unique=True)),
                ('fechaDeComicion', models.DateField()),
                ('rol', models.CharField(choices=[('presidente', 'Presidente'), ('vocal_titular', 'Vocal Titular'), ('vocal_suplente', 'Vocal Suplente')], max_length=15)),
                ('docentes', models.ManyToManyField(to='usuario.docente')),
            ],
        ),
    ]
