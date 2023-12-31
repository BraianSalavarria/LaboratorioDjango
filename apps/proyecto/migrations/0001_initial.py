# Generated by Django 4.2.5 on 2023-10-24 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProyectoTrabajoFinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40, unique=True)),
                ('fechaPresentacion', models.DateField()),
                ('descripcion', models.TextField(max_length=500)),
                ('NroResolucionTribunal', models.CharField(max_length=15)),
                ('archivosAdjuntos', models.FileField(default=None, upload_to='Files/ArchivosDePTF/')),
                ('ascesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.ascesor')),
                ('coDirector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codirector', to='persona.docente')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director', to='persona.docente')),
            ],
            options={
                'ordering': ['fechaPresentacion'],
            },
        ),
        migrations.CreateModel(
            name='MovimientosPTF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movimiento', models.CharField(choices=[('PROYECTO_PRESENTADO', 'Proyecto Presentado - Esperando Evaluacion por CSTF'), ('PROYECTO_EVALUADO_POR_CSTF', 'Proyectado Evaluado por la CSTF'), ('PROYECTO_EN_EVALUACION_POR_EL_TRIBUNAL', 'Proyecto en Evaluacion por el Tribunal'), ('PROYECTO_EVALUADO_POR_EL_TRIBUNAL', 'Proyecto Evaluado por el Tribunal'), ('PROYECTO_APROBADO', 'Proyecto Aprobado')], max_length=51)),
                ('fechaDeMovimiento', models.DateField()),
                ('archivosAdjuntoOpcional', models.FileField(blank=True, upload_to='Files/ArchivosDeMovimientos/')),
                ('proyectoTrabajoFinal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.proyectotrabajofinal')),
            ],
            options={
                'ordering': ['fechaDeMovimiento'],
            },
        ),
        migrations.CreateModel(
            name='IntegrantesPTF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaAlta', models.DateField()),
                ('integrante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.alumno')),
                ('proyectoTrabajoFinal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.proyectotrabajofinal')),
            ],
        ),
    ]
