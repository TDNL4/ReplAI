import unicodedata

def sanitizar(text):
    # Convertir a minúsculas
    text = text.lower()
    # Eliminar tildes, ñ y otros caracteres especiales
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore').decode("utf-8")
    return text.strip()