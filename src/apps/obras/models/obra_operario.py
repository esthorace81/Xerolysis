from django.core.exceptions import ValidationError
from django.db import models

from .obra import Obra
from .operario import Operario


class OperarioObra(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='operarios')
    operario = models.ForeignKey(Operario, on_delete=models.PROTECT, related_name='obras')
    fecha_asignacion = models.DateField(auto_now_add=True)
    notas = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ['obra', 'operario']

    def clean(self):
        if not self.operario.operario_activo:
            raise ValidationError('No se puede asignar un operario inactivo')
        if self.obra.estado == 'TERMINADA':
            raise ValidationError('No se puede asignar operarios a una obra terminada')

    def __str__(self):
        return f'{self.operario} - {self.obra}'
