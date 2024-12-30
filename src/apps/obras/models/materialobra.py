from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from .material import Material
from .obra import Obra


class MaterialObra(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='materiales')
    material = models.ForeignKey(Material, on_delete=models.PROTECT, related_name='obras')
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    fecha_instalacion = models.DateField()

    def clean(self):
        if self.cantidad > self.material.stock:
            raise ValidationError('No hay suficiente stock disponible')
        if self.fecha_instalacion < self.obra.fecha_inicio:
            raise ValidationError(
                'La fecha de instalación no puede ser anterior a la fecha de inicio de la obra'
            )
        if self.obra.fecha_fin_real and self.fecha_instalacion > self.obra.fecha_fin_real:
            raise ValidationError(
                'No se puede instalar material después de la fecha de finalización de la obra'
            )

    def __str__(self):
        return f'{self.material} ({self.cantidad}) - {self.obra}'
