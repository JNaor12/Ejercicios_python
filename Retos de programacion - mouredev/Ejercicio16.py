
# MEDIO

#  * EJERCICIO:
#  * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
#  * creando una que sea capaz de encontrar y extraer todos los números
#  * de un texto.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea 3 expresiones regulares (a tu criterio) capaces de:
#  * - Validar un email.
#  * - Validar un número de teléfono.
#  * - Validar una url.

import re

# Función para encontrar y extraer todos los números de un texto
def extraer_numeros(texto):
    regex_numeros = r"\d+"  # Busca secuencias de uno o más dígitos
    return re.findall(regex_numeros, texto)

# Prueba de extraer números
texto = "El precio es 1234 y el código es 5678."
print("Números encontrados:", extraer_numeros(texto))

# Validar email
def validar_email(email):
    regex_email = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    return bool(re.match(regex_email, email))

print("Email válido:", validar_email("ejemplo@dominio.com"))

# Validar número de teléfono
def validar_telefono(telefono):
    regex_telefono = r"^\+?\d{1,4}?[-.\s]?(\d{1,3}[-.\s]?){1,4}\d{1,4}$"
    return bool(re.match(regex_telefono, telefono))

print("Teléfono válido:", validar_telefono("+1-123-456-7890"))

# Validar URL
def validar_url(url):
    regex_url = r"^(https?:\/\/)?([\w-]+\.)+[\w-]{2,}(\/[\w.-]*)*\/?$"
    return bool(re.match(regex_url, url))

print("URL válida:", validar_url("https://www.ejemplo.com/path"))
