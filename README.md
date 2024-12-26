# Xerolysis: Servicio de Blotting

## Configuración de reglas para IA

    /.windsurfrules
    /.cursorrules
    /github/copilot-instructions.md

## Modificación para entornos de producción y desarrollo

    /src/config/manage.py
    /src/config/wsgi.py
    /src/config/settings/base.py
    /src/config/settings/dev.py
    /src/config/settings/prod.py
    /src/config/settings/test.py

## Uso de TailwindCSS

    npx tailwindcss -i ./src/static/css/input.css -o ./src/static/css/main.css --watch
