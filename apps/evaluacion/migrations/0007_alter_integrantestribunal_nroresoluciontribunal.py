# Generated by Django 4.2.5 on 2023-11-22 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0006_proyectotrabajofinal_tribunalevaluador_trabajo_final_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrantestribunal',
            name='nroResolucionTribunal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluacion.tribunalevaluador'),
        ),
    ]
