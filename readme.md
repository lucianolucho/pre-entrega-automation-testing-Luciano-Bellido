# 🧪 Proyecto de testing automatizado - SauceDemo

## 📌 Propósito del proyecto
El propósito de este proyecto es automatizar pruebas funcionales sobre la página https://www.saucedemo.com/, una plataforma demo utilizada para prácticas de testing automatizado.  

Las pruebas implementadas validan tres flujos principales del sitio:
- Login: Verifica la autenticación de usuarios válidos e inválidos.  
- Navegación del catálogo: Comprueba la visualización y acceso correcto a los productos.  
- Carrito de compras: Valida la adición del produto y el chequeo que del producto elegido  



## 🛠️ Tecnologías utilizadas

- Python
- Pytest → framework de testing automatizado  
- Selenium WebDriver → automatización del navegador  
- WebDriver Manager*→ gestión automática de drivers de Chrome/Firefox  

## ⚙️ Instalación de dependencias

pip install selenium
pip install pytest
pip install webdriver-manager
pip install pytest-html


## Como ejecutar las pruebas

pytest -v run_test.py