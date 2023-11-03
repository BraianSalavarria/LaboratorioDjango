# Generated by Django 4.2.5 on 2023-11-01 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0005_remove_informeevaluacionptf_proyectotrabajofinal_and_more'),
        ('proyecto', '0007_alter_movimientosptf_archivosadjuntoopcional_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectotrabajofinal',
            name='NroResolucionTribunal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluacion.tribunalevaluador'),
        ),
        migrations.CreateModel(
            name='InformeEvaluacionPTF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.TextField(max_length=500)),
                ('fechaInforme', models.DateField()),
                ('estado', models.CharField(choices=[('ACEPTADO', 'Aceptado'), ('RECHAZADO', 'Rechazado'), ('OBSERVADO', 'Observado')], max_length=10)),
                ('archivosAdjuntos', models.FileField(default=None, upload_to='Files/ArchivosDeInformes/')),
                ('proyectoTrabajoFinal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.proyectotrabajofinal')),
            ],
            options={
                'ordering': ['fechaInforme'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InformeEvaluacionFormalPTF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.TextField(max_length=500)),
                ('fechaInforme', models.DateField()),
                ('estado', models.CharField(choices=[('ACEPTADO', 'Aceptado'), ('RECHAZADO', 'Rechazado'), ('OBSERVADO', 'Observado')], max_length=10)),
                ('plazoObservacion', models.DateField(blank=True, null=True)),
                ('comicionSeguimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluacion.comiciondeseguimiento')),
                ('proyectoTrabajoFinal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.proyectotrabajofinal')),
            ],
            options={
                'ordering': ['fechaInforme'],
                'abstract': False,
            },
        ),
    ]