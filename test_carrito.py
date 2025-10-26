from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import pytest

def test_carrito(login_in_driver):
    try:
          driver = login_in_driver

          #Obtengo los productos de la página

          productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
          print(f'Se encontraron {len(productos)} productos.')

          #Añadir un producto al carrito haciendo clic en el botón correspondiente


          nombre_producto = productos[0].find_element(By.CLASS_NAME, 'inventory_item_name ').text
          productos[0].find_element(By.TAG_NAME, 'button').click()

          print(nombre_producto)
     

          #Verificar que el contador del carrito se incremente correctamente

          carrito = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge")))
  
          contador = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
      
                
          assert contador == '1' , "contador incorrecto"
          print("El contador se incrementó correctamnete")

          #Navegar al carrito de compras
          driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

          time.sleep(2)                    #Comprobar que el producto añadido aparezca correctamente en el carrito


    except Exception as e:
        print(f"Error en testa_login: {e}")
        raise
    finally:
         driver.quit()
#-----------------------------------------------------------------------------------------------