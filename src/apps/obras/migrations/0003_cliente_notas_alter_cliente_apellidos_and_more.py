# Generated by Django 5.1.4 on 2024-12-30 21:47

import django.utils.timezone
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0002_alter_cliente_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='notas',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellidos',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_registro',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombres',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='razon_social',
            field=models.CharField(blank=True, db_index=True, max_length=200, null=True, verbose_name='razón social'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='teléfono'),
        ),
    ]