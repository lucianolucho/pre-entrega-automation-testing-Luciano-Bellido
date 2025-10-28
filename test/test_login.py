from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import pytest

#funcion de prueba para el login exitoso 
def test_login_validacion(login_in_driver):
   
    try:
       driver = login_in_driver

       assert "/inventory.html" in driver.current_url , "no se dirigio al inventario"

       print("login exitoso")

    except Exception as e:
        print(f"error en test_login:  {e}")
        raise
    finally:
         driver.quit()