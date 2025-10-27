from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import pytest


def test_navegacion_catalogo(login_in_driver):  

    try:
        driver = login_in_driver

        #verificar la seccion del titulo 
        titulo = driver.find_element(By.CSS_SELECTOR,'div .header_secondary_container .title').text
        print(f'el valor d ela variable es  {titulo}')
        assert titulo == 'Products', "el titulo no es el esperado"
        
        #contar productos visibles
        productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
        print(f'Se encontraron {len(productos)} productos.')

        assert len(productos)> 0, "no se muestran productos "
        
        time.sleep(2)

        #Validar que elementos importantes de la interfaz estén presentes (menú,filtros, etc.)
        #valida la presencia del menú
        menu = driver.find_element(By.ID,'react-burger-menu-btn')
 
        assert menu.is_displayed() , "el menú no se esta mostrando"
        
        #valida lapresencia del filtro  


    except Exception as e:
        print(f"error en test_login:  {e}")
        raise
    finally:
         driver.quit()




     