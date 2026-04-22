from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

from funciones_agente.obtener_clima import obtener_clima
from funciones_agente.obtener_precio_accion import obtener_precio_accion
from utils.sanitizar import sanitizar

# Configuración de Firefox (Headless para que no se abra la ventana)
# main.py

options = Options()
# options.add_argument("--headless") 
# Añade esta línea para parecer un usuario real:
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0")

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
def procesar_input(user_input):
    if "clima" in user_input or "temperatura" in user_input:
        return obtener_clima
    elif "precio" in user_input or "accion" in user_input or "valor" in user_input:
        return obtener_precio_accion
    return None

print("*** Chatbot v1.0.0 (Firefox Edition) ***")
print("Hola, soy tu asistente virtual. Puedo darte el clima o precios de acciones.")
print("Escribe 'salir' o 'adios' para terminar la sesión.")

try:
    while True:
        raw_input = input("---> ")
        user_input = sanitizar(raw_input)
        
        # Opción para salir del programa
        if user_input in ["salir", "adios", "quit", "exit"]:
            print(">>> ¡Hasta luego! Que tengas un buen día.")
            break
            
        funcion_agente = procesar_input(user_input)
        
        if funcion_agente is None:
            print(">>> No entendí tu solicitud. Prueba con algo como 'precio de Apple' o 'clima en Madrid'.")
        else:
            respuesta = funcion_agente(driver, user_input)
            print(f">>> {respuesta}")

finally:
    # Cerrar el navegador al terminar
    driver.quit()