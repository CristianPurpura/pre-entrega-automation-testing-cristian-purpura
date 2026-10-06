# 🧪 SauceDemo E2E Automation Testing

## 🎯 Propósito del Proyecto
Este proyecto es una suite de automatización de pruebas End-to-End (E2E) para la aplicación web demo [SauceDemo](https://www.saucedemo.com/). El objetivo principal es validar mediante scripts automatizados los flujos críticos de negocio (Core Business), asegurando que un usuario pueda autenticarse correctamente, visualizar el catálogo de productos y operar el carrito de compras sin fricciones. 

La arquitectura del proyecto implementa una variación del **Page Object Model (POM)** centralizando localizadores y acciones, lo que garantiza que el framework sea mantenible y escalable.

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3
- **Framework de Testing:** Pytest
- **Herramienta de Automatización:** Selenium WebDriver
- **Patrones de Diseño:** Page Object Model (POM) aplicado a UI Locators.
- **Reportes:** Pytest-HTML
- **Control de Versiones:** Git & GitHub

## 🧪 Casos de Prueba Implementados

La suite cuenta con 3 pruebas automatizadas independientes que cubren las exigencias del proyecto:

1. **Automatización de Login (`test_automatizacion_login`)**
   - Inyecta credenciales válidas.
   - Verifica la redirección correcta a la ruta `/inventory.html`.
   - Valida que el título de la página sea el esperado ("Swag Labs").

2. **Verificación del Catálogo (`test_navegacion_y_verificacion_catalogo`)**
   - Comprueba la visibilidad de elementos vitales de la UI (menú principal y filtros).
   - Valida que el backend haya renderizado los productos en la grilla.
   - Extrae dinámicamente y lista por consola el nombre y precio del primer producto.

3. **Interacción con el Carrito (`test_interaccion_carrito`)**
   - Captura el nombre del primer producto del catálogo.
   - Interactúa con el botón "Add to cart".
   - Verifica que el contador (badge) del carrito se incremente a "1".
   - Navega a la vista del carrito y valida que el producto añadido coincida exactamente con el seleccionado.

## ⚙️ Instrucciones de Instalación Local

Para levantar este proyecto en un entorno local, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/CristianPurpura/pre-entrega-automation-testing-cristian-purpura.git
   cd pre-entrega-automation-testing-cristian-purpura
   ```

2. **Crear y activar el entorno virtual (Recomendado):**
   - En Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - En Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instalar las dependencias requeridas:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Ejecución de las Pruebas y Reportes

Los tests están diseñados para ser totalmente independientes gracias al uso de fixtures en `conftest.py`. Para ejecutar la suite completa y generar el reporte, asegúrate de tener el entorno virtual activado y ejecuta el siguiente comando en la raíz del proyecto:

```bash
pytest tests/test_saucedemo.py -v -s --html=reports/reporte.html --self-contained-html
```

**Explicación de los parámetros:**
- `-v`: Modo verbose, muestra más detalles de la ejecución de Pytest.
- `-s`: Permite visualizar las salidas de consola (prints) en tiempo real (vital para ver los datos extraídos del catálogo).
- `--html=reports/reporte.html --self-contained-html`: Genera un reporte dinámico en formato HTML en la carpeta `reports`, incrustando todos los estilos para que sea portable.

Una vez finalizado, puedes abrir el archivo `reports/reporte.html` en cualquier navegador web para ver la evidencia de la ejecución exitosa.