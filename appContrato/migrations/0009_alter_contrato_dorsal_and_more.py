# Generated by Django 4.1.1 on 2022-11-12 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appContrato', '0008_alter_contrato_fecha_fin_alter_contrato_fecha_inicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='dorsal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='posicion_jugador',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]