# Generated by Django 5.2.1 on 2025-05-09 18:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft_production_app', '0003_alter_aircraft_options_alter_workorder_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Hazır'), ('RECYCLED', 'Geri dönüştürüldü'), ('SOLD', 'Satıldı'), ('MAINTENANCE', 'Bakımda')], default='AVAILABLE', max_length=20, verbose_name='Uçak Durumu'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='avionics',
            field=models.OneToOneField(blank=True, limit_choices_to={'part_type__category': 'AVIONICS'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aircraft_as_avionics', to='aircraft_production_app.part', verbose_name='Aviyonik Sistem (Parça SN)'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='fuselage',
            field=models.OneToOneField(blank=True, limit_choices_to={'part_type__category': 'FUSELAGE'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aircraft_as_fuselage', to='aircraft_production_app.part', verbose_name='Gövde (Parça SN)'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='tail',
            field=models.OneToOneField(blank=True, limit_choices_to={'part_type__category': 'TAIL'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aircraft_as_tail', to='aircraft_production_app.part', verbose_name='Kuyruk (Parça SN)'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='wing',
            field=models.OneToOneField(blank=True, limit_choices_to={'part_type__category': 'WING'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aircraft_as_wing', to='aircraft_production_app.part', verbose_name='Kanat (Parça SN)'),
        ),
    ]
