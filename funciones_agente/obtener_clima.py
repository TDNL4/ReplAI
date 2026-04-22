from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obtener_clima(driver, consulta):
    # Forzamos la búsqueda para que Google muestre el widget del clima
    driver.get(f"https://www.google.com/search?q=clima+actual+en+{consulta}")

    try:
        # Esperar hasta 10 segundos a que el ID 'wob_tm' (la temperatura) aparezca
        wait = WebDriverWait(driver, 10)
        
        # Localizar la temperatura
        elemento_temp = wait.until(EC.presence_of_element_located((By.ID, "wob_tm")))
        temperatura = elemento_temp.text
        
        # Localizar otros datos usando selectores más específicos
        unidad = driver.find_element(By.CSS_SELECTOR, "div.vk_bk.wob-unit > span.wob_t").text
        ubicacion = driver.find_element(By.ID, "wob_loc").text
        estado = driver.find_element(By.ID, "wob_dc").text
        
        return f"En {ubicacion}, la temperatura es de {temperatura}{unidad} con estado {estado.lower()}."
        
    except Exception as e:
        # Si falla, devolvemos un mensaje amigable o el error para depurar
        return "No pude encontrar el clima. Asegúrate de escribir bien la ciudad o intenta de nuevo."