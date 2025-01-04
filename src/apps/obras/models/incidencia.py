from django.db import models
from django.utils.timezone import now

from .obra import Obra


class Incidencia(models.Model):
    TIPOS_INCIDENCIA = [
        ('MATERIAL', 'Problema con el Material'),
        ('TECNICA', 'Problema Técnico en la Obra'),
        ('ACCESO', 'Problema de Acceso a la Obra'),
        ('COMUNICACIÓN', 'Problema de Comunicación con el Cliente'),
        ('OTRO', 'Otro'),
    ]

    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='incidencias')
    tipo_incidencia = models.CharField(
        max_length=20, choices=TIPOS_INCIDENCIA, verbose_name='Tipo de Incidencia'
    )
    descripcion = models.TextField(verbose_name='Descripción de la Incidencia')
    abierta_cerrada = models.BooleanField(default=True, verbose_name='Abierta/Cerrada')
    fecha_registro = models.DateTimeField(
        default=now, blank=True, null=True, verbose_name='Fecha de Registro'
    )

    def __str__(self):
        return f'{self.tipo_incidencia} - Obra: {self.obra}'
