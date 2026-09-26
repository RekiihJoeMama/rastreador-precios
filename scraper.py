import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os

archivo_historial = "historial_precios.csv"

# Lista de libros a rastrear — podés agregar más productos acá
libros = [
    {"url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"},
    {"url": "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"},
    {"url": "https://books.toscrape.com/catalogue/soumission_998/index.html"},
]

def obtener_datos(url):
    respuesta = requests.get(url)
    soup = BeautifulSoup(respuesta.text, "html.parser")
    titulo = soup.find("h1").text
    precio = soup.find("p", class_="price_color").text.encode("latin1").decode("utf-8")
    return titulo, precio

def guardar_en_historial(titulo, precio):
    existe = os.path.isfile(archivo_historial)
    with open(archivo_historial, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        if not existe:
            escritor.writerow(["fecha", "titulo", "precio"])
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        escritor.writerow([fecha_actual, titulo, precio])

for libro in libros:
    titulo, precio = obtener_datos(libro["url"])
    guardar_en_historial(titulo, precio)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Guardado: {titulo} - {precio}")