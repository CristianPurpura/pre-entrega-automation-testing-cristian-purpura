import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import Locators, realizar_login

class TestSauceDemo:
    
    def test_automatizacion_login(self, driver):
        """Valida que el login con credenciales válidas redirija al inventario."""
        realizar_login(driver, "standard_user", "secret_sauce")
        
        # Validaciones
        assert "inventory.html" in driver.current_url, "Fallo: La URL no es la del inventario."
        assert driver.title == "Swag Labs", f"Fallo: El título esperado era 'Swag Labs', se obtuvo '{driver.title}'"

    def test_navegacion_y_verificacion_catalogo(self, driver):
        """Verifica elementos UI vitales y la presencia de productos."""
        realizar_login(driver, "standard_user", "secret_sauce")
        wait = WebDriverWait(driver, 10)
        
        # Validación de elementos UI importantes
        assert wait.until(EC.visibility_of_element_located(Locators.MENU_BTN)).is_displayed()
        assert wait.until(EC.visibility_of_element_located(Locators.FILTER_DROPDOWN)).is_displayed()
        
        # Validar presencia de productos
        productos = wait.until(EC.presence_of_all_elements_located(Locators.INVENTORY_ITEM))
        assert len(productos) > 0, "Fallo: No se renderizaron productos en la página."
        
        # Extraer data del primer producto y mostrarla (impreso en consola de Pytest con -s)
        primer_producto = productos[0]
        nombre = primer_producto.find_element(*Locators.ITEM_NAME).text
        precio = primer_producto.find_element(*Locators.ITEM_PRICE).text
        print(f"\n[INFO] Primer producto validado: {nombre} | Precio: {precio}")

    def test_interaccion_carrito(self, driver):
        """Agrega un producto al carrito y valida que los datos y contador coincidan."""
        realizar_login(driver, "standard_user", "secret_sauce")
        wait = WebDriverWait(driver, 10)
        
        # Tomar estado inicial del primer producto
        productos = wait.until(EC.presence_of_all_elements_located(Locators.INVENTORY_ITEM))
        primer_producto = productos[0]
        nombre_esperado = primer_producto.find_element(*Locators.ITEM_NAME).text
        
        # Interacción: Agregar al carrito
        primer_producto.find_element(*Locators.ADD_TO_CART_BTN).click()
        
        # Validar contador de badge
        contador_carrito = wait.until(EC.visibility_of_element_located(Locators.CART_BADGE)).text
        assert contador_carrito == "1", f"Fallo: El contador de carrito esperaba 1, se obtuvo {contador_carrito}"
        
        # Navegación al carrito
        driver.find_element(*Locators.CART_LINK).click()
        wait.until(EC.url_contains("/cart.html"))
        
        # Validar producto dentro del carrito
        item_en_carrito = wait.until(EC.visibility_of_element_located(Locators.CART_ITEM))
        nombre_en_carrito = item_en_carrito.find_element(*Locators.ITEM_NAME).text
        
        assert nombre_en_carrito == nombre_esperado, "Fallo: El producto en el carrito no es el que seleccionamos."