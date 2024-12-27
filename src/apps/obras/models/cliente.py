from django.core.exceptions import ValidationError
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Cliente(models.Model):
    PERSONA = 'P'
    EMPRESA = 'E'

    TIPO_CLIENTE_CHOICES = [(PERSONA, 'Persona'), (EMPRESA, 'Empresa')]

    tipo_cliente = models.CharField(max_length=1, choices=TIPO_CLIENTE_CHOICES, default=PERSONA)

    # Para personas
    nombres = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    apellidos = models.CharField(max_length=100, blank=True, null=True, db_index=True)

    # Para empresas
    razon_social = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='razón social', db_index=True
    )

    # Campos comunes
    telefono = PhoneNumberField(unique=True, verbose_name='teléfono')
    email = models.EmailField(unique=True)
    domicilio = models.CharField(max_length=255, blank=True, null=True)
    notas = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.tipo_cliente == self.PERSONA and (not self.nombres or not self.apellidos):
            raise ValidationError(
                'Debe ingresar nombres y apellidos para clientes de tipo Persona.'
            )

        if self.tipo_cliente == self.EMPRESA and not self.razon_social:
            raise ValidationError('Debe ingresar la razón social para clientes de tipo Empresa.')

    def __str__(self):
        if self.tipo_cliente == self.PERSONA:
            return f'{self.nombres} {self.apellidos}'
        return self.razon_social
