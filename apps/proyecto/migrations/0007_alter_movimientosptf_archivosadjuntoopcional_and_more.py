# Generated by Django 4.2.5 on 2023-11-01 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0006_alter_integrantesptf_fechabaja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimientosptf',
            name='archivosAdjuntoOpcional',
            field=models.FileField(blank=True, null=True, upload_to='Files/ArchivosDeMovimientos/'),
        ),
        migrations.AlterField(
            model_name='movimientosptf',
            name='fechaDeMovimiento',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='movimientosptf',
            name='fechaVencimientoMovimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]