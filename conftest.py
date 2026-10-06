import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    """Fixture que inicializa y cierra el WebDriver para cada test."""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    yield driver
    
    # Teardown: Se ejecuta al finalizar cada test, pase o falle.
    driver.quit()