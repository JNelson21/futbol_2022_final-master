# Generated by Django 4.1.1 on 2022-11-13 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appPartido', '0010_encuentro_equipo_local_encuentro_equipo_visita_and_more'),
        ('appEquipo', '0007_remove_alineacion_equipo_detalle_encuentro_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='alineacion_equipo',
            name='encuentro_id',
            field=models.ForeignKey(db_column='encuentro_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='appPartido.encuentro'),
            preserve_default=False,
        ),
    ]
