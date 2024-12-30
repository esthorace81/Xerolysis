from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .cliente import Cliente


class Obra(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROGRESO', 'En Progreso'),
        ('TERMINADA', 'Terminada'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='obras')
    domicilio = models.CharField(max_length=255)
    descripcion_obra = models.TextField(verbose_name='Descripción de la Obra')
    presupuesto = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    telefono_contacto = PhoneNumberField(blank=True, null=True, verbose_name='Teléfono de Contacto')
    email_contacto = models.EmailField(blank=True, null=True, verbose_name='Email de Contacto')
    fecha_inicio = models.DateField(verbose_name='Fecha de Inicio')
    fecha_fin_estimado = models.DateField(verbose_name='Fecha de Fin Estimado')
    fecha_fin_real = models.DateField(null=True, blank=True, verbose_name='Fecha de Fin Real')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    notas = models.TextField(blank=True, null=True)

    def clean(self):
        if self.fecha_fin_estimado < self.fecha_inicio:
            raise ValidationError(
                'La fecha de fin estimada no puede ser anterior a la fecha de inicio'
            )
        if self.fecha_fin_real and self.fecha_fin_real < self.fecha_inicio:
            raise ValidationError('La fecha de fin real no puede ser anterior a la fecha de inicio')
        if self.estado == 'TERMINADA' and not self.fecha_fin_real:
            raise ValidationError('Una obra terminada debe tener fecha de fin real')

    def __str__(self):
        return f'Obra en {self.domicilio} - {self.cliente}'
