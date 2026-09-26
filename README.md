🎶 Rastreador de Precios

Aplicación que rastrea precios de productos mediante web scraping, guarda un historial con fecha/hora, y lo muestra en un panel web con gráficos.

Funcionalidades
Extracción de título y precio desde páginas web reales (web scraping con BeautifulSoup)
Seguimiento de múltiples productos en simultáneo
Historial persistente guardado en CSV
Panel web con gráfico de evolución de precios por producto (Chart.js)
Diseño visual propio, con tema turquesa/rosa
Tecnologías usadas
Python — lógica del scraper y backend
BeautifulSoup — extracción y parseo de HTML
Flask — framework web
Chart.js — gráficos de evolución de precios
CSV — almacenamiento del historial
Cómo correrlo localmente
Cloná el repositorio:

git clone https://github.com/RekiihJoeMama/rastreador-precios.git
cd rastreador-precios

Instalá las dependencias:

pip install requests beautifulsoup4 flask

Corré el scraper para generar el historial de precios:

python scraper.py

Corré la aplicación web:

python app.py

Abrí http://127.0.0.1:5000 en tu navegador.
Nota

El scraper apunta actualmente a books.toscrape.com, un sitio educativo pensado para practicar técnicas de web scraping sin restricciones. La lógica está lista para adaptarse a cualquier tienda real con solo ajustar los selectores HTML según su estructura.

Autor

RekiihJoeMama