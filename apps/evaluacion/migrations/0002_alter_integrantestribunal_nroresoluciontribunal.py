# Generated by Django 4.2.5 on 2023-10-31 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrantestribunal',
            name='nroResolucionTribunal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluacion.tribunalevaluador'),
        ),
    ]
