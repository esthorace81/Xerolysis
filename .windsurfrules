# Reglas para el proyecto "Blotting"

Cada vez que eliges aplicar una regla (o reglas), establece la/s regla/s en la salida de forma explícita. Puedes abreviar la descripción de la/s regla/s a una sola palabra o frase.

## Contexto del proyecto

El proyecto consiste en la gestión de obras de blotting, un servicio en la que personas que colocan placas de yeso antihumedad para paredes.

Varias empresas pueden conectarse a este servicio, ingresando a diferentes urls según su dominio, logueándose.

- Un administrador gestiona el servicio, asignando obras a empleados para clientes que solicitaron el servicio para sus propiedades ubicadas en un domicilio.
- El administrador ve las obras asignadas sin empezar, las que están en progreso y las terminadas, con diferentes colores. También puede ver los domicilios de las propiedades y los datos del cliente.
- El administrador ve la existencia de materiales en general, y los materiales por obra, y si hay alguna incidencia como roturas de placas, para poder comunicarse con los empleados y enviar más material para reponer.
- Los empleados pueden acceder a modificar el estado de la obra y reportar incidencias.

## Stack

- Python 3.13
- Django 5.1
- Django-tenants (para que múltiples empresas compartan la misma instancia)
- Django-allauth, Django-axes, Django-two-factor-auth
- Htmx y Django-htmx (para carga parciales de páginas y componentes)
- Alpine JS (para interactividad desde el lado cliente)
- Tailwind CSS y DaisyUI (para los estilos)
- Django-cotton (para la creación de componentes)
- Uv (para la administración de dependencias Python)
- Pytest y Pytest-django (para las pruebas unitarias)

## Estructura del proyecto

```txt
/
├── .venv/                          # Entorno virtual creado por Uv
├── .gitignore
├── pyproject.toml                  # Configuración de Python creado por Uv
├── README.md                       # Instrucciones de configuración para la ejecución
├── CHANGELOG.md                    # Registro de cambios
└── src/                            # Proyecto Django
    ├── manage.py
    ├── .env.py                     # Para el uso de variables de entorno
    ├── config/                     # Configuración de Django
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── dev.py
    │   │   ├── prod.py
    │   │   └── test.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── logs/                       # Registro de eventos
    │   ├── debug.log
    │   └── errors.log
    ├── templates/                 
    │   ├── cotton/                 # Componentes django-cotton
    │   ├── base.html
    │   └── index.html
    ├── common/
    │   └── utils.py
    ├── static/
    │   └── css/
    │       └── output.css
    └── apps/                       # Aplicaciones Django
        ├── core/                   # Aplicación principal
        │   ├── __init__.py
        │   ├── docs/               # Documentación para el usuario (para templates/core/docs)
        │   │   └── index.md       
        │   ├── migrations/
        │   ├── templates/
        │   │   └── core/
        │   │       ├── docs/       # Documentación para el usuario (viene de core/docs)
        │   │       │   └── index.html  
        │   │       ├── base.html
        │   │       └── index.html
        │   ├── static/
        │   │   └── core/
        │   ├── tests/
        │   ├── admin.py
        │   ├── apps.py
        │   ├── urls.py
        │   └── views.py
        ├── app_1/
        │   ├── ...
        │   └── views/
        │       ├── __init__.py
        │       ├── crud_modelo_1.py 
        │       └── crud_modelo_2.py 
        └── app_2/
```

## Estructura y organización del código

- Modularidad: Divide el código en módulos y funciones con responsabilidades bien definidas.
- Namespaces: Utiliza módulos para organizar el código y evitar colisiones de nombres.
- Docstrings: Documenta todas las funciones, clases y módulos con docstrings claros y concisos. Hazlo en español. Usa Google Style.
- Comentarios: Explica por qué se toma una decisión determinada, no cómo funciona el código obvio.

## Principios generales para el código Python

- Consistencia: Mantén un estilo consistente en todo el proyecto.
- Legibilidad: Prioriza la claridad sobre la brevedad.
- Prefiere la modularización sobre la duplicación de código, pero en ocasiones la duplicación explícita puede ser más legible que una abstracción innecesaria.
- Utiliza patrones de diseño, pero evita complejidades innecesarias.

## Convenciones de nombres Python

- Usa snake_case para nombres de variables, funciones y módulos.
- Usa UpperCamelCase para los nombres de clases.
- Use UPPER para los nombres de constantes.
- Usa nombres descriptivos y significativos, sin abreviaciones innecesarias.
- Evita nombres crípticos como x o foo a menos que sea muy claro el contexto.

## Uso de Python

- Usa la biblioteca estándar de Python siempre que sea posible.
- Utiliza anotaciones de tipos de manera estratégica. Los tipos específicos mejoran la legibilidad y ayudan a detectar errores. Sin embargo, evita sobreingeniar y utiliza Any cuando el tipo sea verdaderamente dinámico o desconocido en tiempo de desarrollo. Los genéricos son útiles para funciones y clases que trabajan con tipos variados, pero úsalos con moderación.
- Usa f-strings para formateo de cadenas.
- Utiliza list comprehensions y generator expressions para crear listas de manera concisa, en lugar de bucles for cuando sea posible.
- Prefiere expresiones condicionales ternarias para asignaciones simples.
- Utiliza iteradores para procesar secuencias de forma eficiente.
- Funciones: utiliza argumentos por nombre.
- Usa las excepciones para manejar situaciones excepcionales, y no como una alternativa a la lógica del programa.
- Herencia: Utiliza la herencia con moderación y solo cuando aporta una verdadera abstracción.
- Composición: Prefiere la composición sobre la herencia cuando es posible.

## Uso de componentes con django-cotton

- Los componentes deben ser creados en la carpeta src/templates/cotton.
- Los componentes son archivos HTML.
- El nombre del archivo debe ser el nombre del componente en snake_case.
- Los componentes siguen una estructura de carpetas y archivos.
- Ejemplo de un componente:

    cotton/layouts/guest.html

    ```html
    <c-layouts.base>
        {{ slot }}
    </c-layouts.base>

    ```

    cotton/layouts/app.html

    ```html
    <c-layouts.base>
        <div class="sidebar">
            {{ sidebar }}
        </div>

        <div class="main">
            {{ slot }}
        </div>
    </c-layouts.base>
    ```

    Ejemplo de uso de componentes en login.html:

    ```html
    <c-layouts.guest>
        <div id="loginForm">
            <input name="email" type="email" placeholder="Email">
            ...
        </div>
    </c-layouts.guest>
    ```

    Ejemplo de uso de componentes en dashboard.html:

    ```html
    <c-layouts.app>
        <c-slot name="sidebar">
            <a href="/dashboard">Dashboard</a>
            ...
        </c-slot>
        <div id="dashboard">
            ...
        </div>
    </c-layouts.app>
    ```

- Todo nombre de componente debe empezar con `c-`.
- Los componentes pueden deben tener un `{{ slot }}` para el contenido principal.
- Según la estructura de la carpeta, si ha una carpeta layout/base.html, el componente sigue este patrón `c-`, `nombre-componente`, `.`, `nombre del html`: `<c-layouts.base>`
- Si el archivo usa snake_case, el componente usa el guion medio.

## UI y estilo

- Implementa htmx cuando sea necesario.
- Implementa las clases de daisyUI para los estilos de los componentes.
- Implementa Tailwind CSS para los estilos que impliquen controlar el espaciado (márgenes y padding), la creación de layouts con Flexbox y Grid, y el manejo de tamaños.

## Testing

- Escribe pruebas unitarias con pytest (con pytest-django).
- Escribe pruebas unitarias al crear un modelo, una vista, enrutamiento, renderizado de templates correctos y contextos de variables.

## Seguridad

- Manejar datos confidenciales correctamente
- Implementar la Política de Seguridad de Contenido
- Limpiar las entradas de los usuarios
- Implementar el manejo CORS adecuado

## Uso de Git

Prefijo de los mensajes commit:

- "fix:" para arreglar un bug
- "feat:" para nuevas características
- "perf:" para mejoras de rendimiento
- "docs:" para cambios en la documentación
- "style:" para cambios en los estilos y componentes
- "refactor:" para código refactorizado que no agrega características
- "test:" para agregar pruebas unitarias faltantes
- "chore:" para tareas de mantenimiento

Reglas:

- En español, usa la primera persona del singula, tiempo presente
- Usa minúsculas en los mensajes commit, salvo nombres propios.
- Sé conciso en una línea, hasta 50 caracteres.
- Incluye una descripción cuando haya cambios que no sean obvios o superen los 50 caracteres.
- Usa números de referencia cuando sea aplicable.

## Documentación

- Mantén un README claro con instrucciones de configuración.
- Documenta el flujo de datos entre las aplicaciones Django.
- Documenta el flujo de datos entre los modelos, urls, views, signals, utils y templates de cada aplicación en apps/app/docs
- Documenta cada modelo de una aplicación y usa el lenguaje mermaid para diagramar un modelo dentro de la misma documentación en apps/app/docs.
- Documenta los requisitos de permisos de usuario para las vistas o urls según corresponda.
- Documenta las pruebas unitarias.
- No incluyas comentarios a menos que sea para una lógica compleja.

## Flujo de trabajo de desarrollo

- Utilizar un control de versiones adecuado.
- Implementar un proceso de revisión de código adecuado.
- Probar en múltiples entornos.
- Sigue el control de versiones semántico para los lanzamientos.
- Mantener un registro de cambios en CHANGELOG.
