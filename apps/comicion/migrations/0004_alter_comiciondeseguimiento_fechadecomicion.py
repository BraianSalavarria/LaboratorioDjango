# Generated by Django 4.2.5 on 2023-10-04 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comicion', '0003_remove_comiciondeseguimiento_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comiciondeseguimiento',
            name='fechaDeComicion',
            field=models.DateField(auto_now_add=True),
        ),
    ]
