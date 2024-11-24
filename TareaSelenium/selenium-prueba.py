from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.action_chains import ActionChains  
import time
import pytest
from selenium.webdriver.chrome.options import Options

# Funcion para usar time.sleep
def espera(tiempo):
    time.sleep(tiempo)
    return

# Historia 1
@pytest.mark.test_historia1
def test_historia1(browser):
    titulo_de_la_pagina = browser.title
    action = ActionChains(browser)
    # Aqui busca los campos de usuario y contrasena 
    usuario = browser.find_element(By.ID, 'user-name')
    contrasena = browser.find_element(By.ID, 'password')

    # Agrega por entrada los datos en los campos de inicio de sesion 
    action.move_to_element(usuario).click().send_keys('standard_user').perform()
    espera(2)
    action.move_to_element(contrasena).click().send_keys('secret_sauce').perform()
    espera(2)
    browser.save_screenshot("captura_de_pantalla.png")

    # Pulsa el boton de login para pasar a la pagina principal
    boton_enviar = browser.find_element(By.ID, 'login-button')
    action.move_to_element(boton_enviar).click().perform()

    espera(2)
    assert titulo_de_la_pagina in browser.title

# Historia 2
@pytest.mark.test_historia2
def test_historia2(browser):
    titulo_de_la_pagina = browser.title
    action = ActionChains(browser)
    # Agrega un objeto al carrito
    boton_agregar_mochila = browser.find_element(By.ID,'add-to-cart-sauce-labs-backpack')
    action.move_to_element(boton_agregar_mochila).click().perform()
    espera(2)

    # Agrega un objeto al carrito
    boton_agregar_polo = browser.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    action.move_to_element(boton_agregar_polo).click().perform()
    espera(2)
    browser.save_screenshot("captura_de_pantalla2.png")
    assert titulo_de_la_pagina in browser.title

# Historia 3
@pytest.mark.test_historia3
def test_historia3(browser):
    titulo_de_la_pagina = browser.title
    action = ActionChains(browser)
    # Abre el carrito 
    boton_carrito = browser.find_element(By.LINK_TEXT, "2")
    action.move_to_element(boton_carrito).click().perform()
    espera(2)
    browser.save_screenshot("captura_de_pantalla3.png")
    assert titulo_de_la_pagina in browser.title

# Historia 4
@pytest.mark.test_historia4
def test_historia4(browser):
    titulo_de_la_pagina = browser.title
    action = ActionChains(browser)
    # Abre la caja
    boton_caja = browser.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]")
    action.move_to_element(boton_caja).click().perform()
    espera(2)

    # Pulsa el campo de nombre e introduce el nombre
    facturacion_nombre = browser.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]")
    action.move_to_element(facturacion_nombre).click().send_keys("Jese").perform()
    espera(2)

    # Pulsa el campo de nombre e introduce el apellido
    facturacion_apellido = browser.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]")
    action.move_to_element(facturacion_apellido).click().send_keys("Hernandez").perform()
    espera(2)

    # Pulsa el campo de nombre e introduce el codigo postal
    facturacion_codigo_postal = browser.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]")
    action.move_to_element(facturacion_codigo_postal).click().send_keys('10114').perform()
    espera(2)
    browser.save_screenshot("captura_de_pantalla4.png")
    assert titulo_de_la_pagina in browser.title

# Historia 5
@pytest.mark.test_historia5
def test_historia5(browser):
    titulo_de_la_pagina = browser.title
    action = ActionChains(browser)
    # Pulsa el boton continuar para pasar a la facturacion
    continuar = browser.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]")
    action.move_to_element(continuar).click().perform()
    espera(2)
    browser.save_screenshot("captura_de_pantalla5.png")
    # Pulsa el boton de finalizar 
    boton_finalizar = browser.find_element(By.CSS_SELECTOR, "*[data-test=\"finish\"]")
    action.move_to_element(boton_finalizar).click().perform()
    espera(2)

# Función de finalización del test
def volver(browser):
    espera(2)
    # Vuelve a la pantalla inicial 
    barra = browser.find_element(By.ID, "react-burger-menu-btn")
    action = ActionChains(browser)
    action.move_to_element(barra).click().perform()
    espera(2)
    volver_inicio = browser.find_element(By.ID, "inventory_sidebar_link")
    action.move_to_element(volver_inicio).click().perform()
    espera(2)
    # Cuanto tiene la pagina activa
    espera(15)
    
@pytest.fixture(scope="module")
def browser():
    chrome_options = Options()
    
    
    driver = webdriver.Chrome(options=chrome_options)  # Inicializa el navegador (en mi caso, Chrome)
    driver.get('https://www.saucedemo.com/')  # Abre la pagina web
    yield driver  #Mantiene el chrome abierto hasta que se ejecute toda la prueba
    driver.quit()  #Se cierra el chrome solo después de todas las pruebas


#pytest selenium-prueba.py --html=reporte.html