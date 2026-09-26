from flask import Flask, render_template
import csv
import re
from collections import defaultdict

app = Flask(__name__)
archivo_historial = "historial_precios.csv"

def limpiar_precio(precio_texto):
    numero = re.sub(r"[^\d.]", "", precio_texto)
    try:
        return float(numero)
    except ValueError:
        return None

def leer_historial():
    datos_por_libro = defaultdict(list)
    try:
        with open(archivo_historial, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                datos_por_libro[fila["titulo"]].append({
                    "fecha": fila["fecha"],
                    "precio_texto": fila["precio"],
                    "precio_numero": limpiar_precio(fila["precio"])
                })
    except FileNotFoundError:
        pass
    return datos_por_libro

@app.route("/")
def home():
    datos_por_libro = leer_historial()
    return render_template("index.html", datos_por_libro=datos_por_libro)

if __name__ == "__main__":
    app.run(debug=True)