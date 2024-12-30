from django.core.validators import MinValueValidator
from django.db import models


class Material(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(verbose_name='Descripción del Material')
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    precio_unitario = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    fecha_actualizacion_precio = models.DateField(verbose_name='Fecha de Actualización de Precio')
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
