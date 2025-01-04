import pytest
from django.core.exceptions import ValidationError

from ..models import Cliente


@pytest.mark.django_db
class TestCliente:
    @pytest.fixture
    def datos_persona_valida(self):
        """Fixture que retorna datos válidos para un cliente tipo Persona."""
        return {
            'tipo_cliente': Cliente.PERSONA,
            'nombres': 'Juan Antonio',
            'apellidos': 'Pérez González',
            'dni': '12345678',
            'telefono': '+542613337751',
            'email': 'juan.perez@example.com',
            'domicilio': 'Av. Siempreviva 742',
        }

    def test_nombres_no_puede_estar_vacio(self, datos_persona_valida: dict[str, str]):
        """Si el tipo de cliente es Persona, el campo 'nombres' no puede estar vacío."""
        cliente = Cliente(**datos_persona_valida)
        assert cliente.tipo_cliente == Cliente.PERSONA
        cliente.nombres = ''
        with pytest.raises(ValidationError):
            cliente.full_clean()

    def test_apellidos_no_puede_estar_vacio(self, datos_persona_valida: dict[str, str]):
        """Si el tipo de cliente es Persona, el campo 'apellidos' no puede estar vacío."""
        cliente = Cliente(**datos_persona_valida)
        assert cliente.tipo_cliente == Cliente.PERSONA
        cliente.apellidos = ''
        with pytest.raises(ValidationError):
            cliente.full_clean()
