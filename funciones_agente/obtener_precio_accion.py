from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obtener_precio_accion(driver, consulta):
    # Forzamos a que la búsqueda sea muy específica para que salga el recuadro de finanzas
    driver.get(f"https://www.google.com/search?q=precio+accion+de+{consulta}")

    try:
        # 1. Espera explícita: Aguarda hasta 10 segundos a que el precio aparezca en pantalla
        # El precio suele tener el atributo jsname="vWLAgc" que es más estable que las clases
        wait = WebDriverWait(driver, 10)
        
        # Buscamos el precio (suele ser lo más fácil de identificar)
        elemento_precio = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[jsname='vWLAgc']")))
        precio = elemento_precio.text

        # 2. Intentamos buscar el nombre de la empresa usando un atributo de datos en lugar de clases
        # Google suele usar data-attrid="title" para el nombre principal del recuadro
        try:
            empresa = driver.find_element(By.CSS_SELECTOR, "[data-attrid='title']").text
        except:
            # Si falla, usamos un selector genérico de encabezado dentro del área de finanzas
            empresa = driver.find_element(By.CSS_SELECTOR, "div.PZPZlf").text

        # 3. Buscamos la divisa (ej. MXN o USD)
        divisa = driver.find_element(By.CSS_SELECTOR, "span.Kn70Te").text
        
        # 4. Buscamos el ticker (ej. NASDAQ: AAPL)
        ticker = driver.find_element(By.CSS_SELECTOR, "div.waO09e").text

        return f"{empresa} [{ticker}] ${precio} {divisa.upper()}."

    except Exception as e:
        # Si quieres ver qué está viendo el bot, puedes tomar una captura de pantalla:
        # driver.save_screenshot("error_google.png")
        return f"No se pudo obtener el dato. Google cambió el diseño o la búsqueda no fue clara."