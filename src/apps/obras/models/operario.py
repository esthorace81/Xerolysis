from django.core.exceptions import ValidationError
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Operario(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = PhoneNumberField(unique=True)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    domicilio = models.CharField(max_length=255)
    fecha_ingreso = models.DateField()
    fecha_retiro = models.DateField(null=True, blank=True)
    operario_activo = models.BooleanField(default=True)
    notas = models.TextField(blank=True, null=True)

    def clean(self):
        if self.fecha_retiro and self.fecha_retiro < self.fecha_ingreso:
            raise ValidationError('La fecha de retiro no puede ser anterior a la fecha de ingreso')
        if self.fecha_retiro and self.operario_activo:
            raise ValidationError('Un operario con fecha de retiro no puede estar activo')
        if not self.fecha_retiro and not self.operario_activo:
            raise ValidationError('Un operario inactivo debe tener fecha de retiro')

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
