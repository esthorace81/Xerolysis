import json
import os
import re
import sys
from pathlib import Path

import pytest

# Obtener la ruta al directorio raíz del proyecto
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SRC_DIR = PROJECT_ROOT

# Configuración del proyecto Django
sys.path.insert(0, str(SRC_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.test'


class TestReportGenerator:
    def __init__(self, app_name: str):
        """
        Inicializa el generador de reportes para una app específica.

        Args:
            app_name: Nombre de la aplicación Django a procesar
        """
        self.src_dir = SRC_DIR
        self.app_dir = self.src_dir / 'apps' / app_name
        self.models_dir = self.app_dir / 'models'
        self.tests_dir = self.app_dir / 'tests'
        self.output_dir = self.tests_dir / 'reports'

        # Verificar que la app existe
        if not self.app_dir.exists():
            raise ValueError(f"La aplicación '{app_name}' no existe en {self.src_dir/'apps'}")

        # Crear directorio para reportes si no existe
        self.output_dir.mkdir(exist_ok=True, parents=True)

    @classmethod
    def list_available_apps(cls) -> list[str]:
        """Lista todas las aplicaciones disponibles en el directorio apps"""
        apps_dir = SRC_DIR / 'apps'
        return [d.name for d in apps_dir.iterdir() if d.is_dir() and (d / 'models').exists() and (d / 'tests').exists()]

    def get_model_files(self) -> list[Path]:
        """Obtiene todos los archivos .py del directorio models excepto __init__.py"""
        return [f for f in self.models_dir.glob('*.py') if f.name != '__init__.py']

    def get_test_file(self, model_file: Path) -> Path:
        """Obtiene el archivo de prueba correspondiente al modelo"""
        return self.tests_dir / f'test_{model_file.name}'

    def get_docstrings_from_test_file(self, test_file: Path) -> dict[str, str]:
        """Extrae los docstrings de las funciones de prueba"""
        docstrings: dict[str, str] = {}
        if not test_file.exists():
            return docstrings

        content = test_file.read_text()
        matches: list[tuple[str, str]] = re.findall(r'def\s+(test_\w+)\(.*?\):\s*"""(.*?)"""', content, re.DOTALL)
        return {match[0]: match[1].strip().replace('\n', ' ') for match in matches}

    def run_tests(self, test_file: Path) -> dict[str, bool]:
        """Ejecuta las pruebas para un archivo específico y retorna los resultados"""
        report_file = self.output_dir / 'temp_report.json'
        pytest.main(
            [
                str(test_file),
                '--tb=short',
                '--disable-warnings',
                '--quiet',
                '--json-report',
                f'--json-report-file={str(report_file)}',
            ]
        )

        if not report_file.exists():
            return {}

        report_data = json.loads(report_file.read_text())
        # Limpiar el archivo temporal
        report_file.unlink(missing_ok=True)

        return {test['nodeid'].split('::')[-1]: test['outcome'] == 'passed' for test in report_data['tests']}

    def generate_markdown(self, model_file: Path, test_results: dict[str, bool], docstrings: dict[str, str]) -> str:
        """Genera el contenido markdown para un modelo específico"""
        content = []
        content.append('# Pruebas de Calidad\n')
        content.append(f'## Modelo {model_file.stem}\n')

        for test_name, passed in test_results.items():
            estado = '[x]' if passed else '[ ]'
            docstring = docstrings.get(test_name, 'Falta docstring!')
            content.append(f'- {estado} {docstring} [{test_name}]\n')

        return '\n'.join(content)

    def process_model(self, model_file: Path):
        """Procesa un archivo de modelo específico"""
        test_file = self.get_test_file(model_file)
        if not test_file.exists():
            print(f'No se encontró archivo de prueba para {model_file.name}')
            return

        test_results = self.run_tests(test_file)
        docstrings = self.get_docstrings_from_test_file(test_file)

        markdown_content = self.generate_markdown(model_file, test_results, docstrings)
        output_file = self.output_dir / f'{model_file.stem}.md'
        output_file.write_text(markdown_content)
        print(f'Reporte generado: {output_file}')

    def run(self):
        """Ejecuta el generador de reportes para todos los modelos de la app"""
        model_files = self.get_model_files()
        if not model_files:
            print(f'No se encontraron archivos de modelo en {self.models_dir}')
            return

        print('\nProcesando modelos de la aplicación...')
        for model_file in model_files:
            print(f'\nProcesando {model_file.name}...')
            self.process_model(model_file)


def agregar_resultado(test_results, nombre_prueba, resultado):
    """Agrega el resultado de una prueba a la lista de resultados.

    Args:
        test_results (list): Lista de resultados de pruebas.
        nombre_prueba (str): Nombre de la prueba.
        resultado (bool): Resultado de la prueba (True si pasó, False si falló).
    """
    test_results.append((nombre_prueba, resultado))


def generar_markdown(test_results):
    """Genera un reporte en formato Markdown a partir de los resultados de las pruebas.

    Args:
        test_results (list): Lista de resultados de pruebas.

    Returns:
        str: Reporte en formato Markdown.
    """
    markdown = '# Resultados de las pruebas\n\n'
    for nombre_prueba, resultado in test_results:
        estado = '✔️' if resultado else '❌'
        markdown += f'- {estado} {nombre_prueba}\n'
    return markdown


def main():
    # Listar apps disponibles
    available_apps = TestReportGenerator.list_available_apps()

    if len(sys.argv) != 2:
        print('Uso: python generar_test_reports.py <nombre_app>')
        print('\nAplicaciones disponibles:')
        for app in available_apps:
            print(f'- {app}')
        sys.exit(1)

    app_name = sys.argv[1]
    if app_name not in available_apps:
        print(f"Error: La aplicación '{app_name}' no está disponible")
        print('\nAplicaciones disponibles:')
        for app in available_apps:
            print(f'- {app}')
        sys.exit(1)

    try:
        generator = TestReportGenerator(app_name)
        generator.run()
    except Exception as e:
        print(f'Error al procesar la aplicación: {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
