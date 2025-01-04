import re

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now
from phonenumber_field.modelfields import PhoneNumberField


class Cliente(models.Model):
    PERSONA = 'P'
    EMPRESA = 'E'

    TIPO_CLIENTE_CHOICES = [(PERSONA, 'Persona'), (EMPRESA, 'Empresa')]

    tipo_cliente = models.CharField(max_length=1, choices=TIPO_CLIENTE_CHOICES, default=PERSONA)

    # Para personas
    nombres = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    apellidos = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    dni = models.CharField(max_length=8, blank=True, null=True, verbose_name='DNI')

    # Para empresas
    razon_social = models.CharField(max_length=200, blank=True, null=True, verbose_name='Razón Social', db_index=True)
    cuit = models.CharField(max_length=11, blank=True, null=True, verbose_name='CUIT')

    # Campos comunes
    telefono = PhoneNumberField(unique=True, verbose_name='Teléfono')
    email = models.EmailField(unique=True)
    domicilio = models.CharField(max_length=255, blank=True, null=True)
    fecha_registro = models.DateTimeField(default=now, blank=True, null=True, verbose_name='Fecha de Registro')
    notas = models.TextField(blank=True, null=True)

    @property
    def es_persona(self):
        return self.tipo_cliente == self.PERSONA

    @property
    def es_empresa(self):
        return self.tipo_cliente == self.EMPRESA

    # def _validar_nombre(self, texto: str) -> bool:
    #     """Valida nombres y apellidos según los criterios especificados."""
    #     if not texto or texto.strip() != texto:  # Verifica espacios al inicio/final
    #         return False

    #     # Verifica que no haya espacios o comillas dobles
    #     if '  ' in texto or "''" in texto:
    #         return False

    #     # Patrón para validar el formato:
    #     # - Caracteres alfabéticos Unicode (incluyendo acentos)
    #     # - Comilla simple entre letras
    #     # - Espacio simple entre letras
    #     patron = r'^[A-Za-zÀ-ÿ]+(?:\s[A-Za-zÀ-ÿ]+)*$|^[A-Za-zÀ-ÿ]+(?:\'[A-Za-zÀ-ÿ]+)*$'
    #     return bool(re.match(patron, texto))

    # def _validar_palabras(self, texto: str, max_palabras: int) -> bool:
    #     """Valida que el texto contenga solo letras y número máximo de palabras."""
    #     if not texto:
    #         return False
    #     palabras = texto.split()
    #     if len(palabras) > max_palabras:
    #         return False
    #     return all(palabra.isalpha() for palabra in palabras)

    # def _validar_razon_social(self, texto: str, max_palabras: int) -> bool:
    #     """Valida la razón social permitiendo letras y puntos como parte de una palabra, y comas como separadores."""
    #     if not texto:
    #         return False

    #     # Elimina comas para contar palabras
    #     texto_limpio = texto.replace(',', ' ')
    #     palabras = [p for p in texto_limpio.split() if p.strip()]

    #     if len(palabras) > max_palabras:
    #         return False

    #     # Verifica que solo contenga letras y puntos
    #     patron = r'^[A-Za-zÀ-ÿ\s\.]+$'
    #     return bool(re.match(patron, texto))

    # def _validar_dni(self, dni: str) -> bool:
    #     """Valida que el DNI tenga solo números y longitud correcta.

    #     Args:
    #         dni: Número de DNI a validar

    #     Returns:
    #         bool: True si el DNI es válido
    #     """
    #     if not dni:
    #         return False
    #     return dni.isdigit() and 6 <= len(dni) <= 8

    # def _validar_cuit(self, cuit: str) -> bool:
    #     """Valida que el CUIT tenga solo números y longitud correcta.

    #     Args:
    #         cuit: Número de CUIT a validar

    #     Returns:
    #         bool: True si el CUIT es válido
    #     """
    #     if not cuit:
    #         return False
    #     return cuit.isdigit() and len(cuit) == 11

    def clean(self):
        super().clean()
        if self.es_persona:
            if not self.nombres or self.nombres.strip() == '':
                raise ValidationError({'nombres': ['El campo "nombres" es obligatorio para clientes tipo Persona']})
            if not self.apellidos or self.apellidos.strip() == '':
                raise ValidationError({'apellidos': ['El campo "apellidos" es obligatorio para clientes tipo Persona']})
            if not self.dni:
                raise ValidationError({'dni': ['El campo "DNI" es obligatorio para clientes tipo Persona']})
        elif self.es_empresa:
            if not self.razon_social:
                raise ValidationError(
                    {'razon_social': ['El campo "Razón Social" es obligatorio para clientes tipo Empresa']}
                )
            if not self.cuit:
                raise ValidationError({'cuit': ['El campo "CUIT" es obligatorio para clientes tipo Empresa']})

    #         if not self._validar_palabras(texto=self.nombres, max_palabras=5):
    #             raise ValidationError("nombres"
    #                 'El campo "nombres" debe contener hasta 5 nombres y solo letras.'
    #             )

    #         if not self._validar_palabras(texto=self.apellidos, max_palabras=3):
    #             raise ValidationError(
    #                 'El campo "apellidos" debe contener hasta 3 apellidos y solo letras.'
    #             )
    #         if self.dni and not self._validar_dni(self.dni):
    #             raise ValidationError({'dni': ['El DNI debe tener entre 6 y 8 dígitos numéricos.']})
    #         if self.cuit:
    #             raise ValidationError(
    #                 {'cuit': ['El campo CUIT debe estar vacío para clientes tipo Persona.']}
    #             )

    #     if self.es_empresa:
    #         if not self.razon_social:
    #             raise ValidationError(
    #                 'Debe ingresar la Razón Social para clientes de tipo Empresa.'
    #             )
    #         if not self._validar_razon_social(texto=self.razon_social, max_palabras=7):
    #             raise ValidationError(
    #                 'La razón social debe contener hasta 7 palabras y solo letras, puntos y comas.'
    #             )
    #         if not self.cuit:
    #             raise ValidationError(
    #                 {'cuit': ['El campo CUIT es obligatorio para clientes tipo Empresa.']}
    #             )
    #         if not self._validar_cuit(self.cuit):
    #             raise ValidationError({'cuit': ['El CUIT debe tener 11 dígitos numéricos.']})

    def __str__(self):
        if self.es_persona:
            return f'{self.apellidos}, {self.nombres}'
        return self.razon_social
