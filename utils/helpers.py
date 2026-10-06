from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Locators:
    """Centralización de selectores para facilitar el mantenimiento y escalabilidad."""
    
    # Pantalla de Login
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    
    # Pantalla de Inventario (Catálogo)
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.btn_inventory")
    
    # Componentes del Carrito
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEM = (By.CLASS_NAME, "cart_item")

def realizar_login(driver, username, password):
    """Acción repetitiva de login encapsulada con esperas explícitas."""
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)
    
    # Esperamos que el campo de usuario esté visible antes de intentar escribir
    user_input = wait.until(EC.visibility_of_element_located(Locators.USERNAME_INPUT))
    user_input.send_keys(username)
    
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_BTN).click()
    
    # Validamos que efectivamente hayamos entrado al inventario antes de devolver el control
    wait.until(EC.url_contains("/inventory.html"))