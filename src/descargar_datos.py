import io
import os

import pandas as pd
import requests

# Dataset "Resultados únicos Saber 11" de datos.gov.co
url = "https://www.datos.gov.co/resource/kgxf-xxbe.csv"
filas_por_periodo = 15000

# 1. Ver qué periodos tiene el dataset
respuesta = requests.get(url, params={"$select": "periodo", "$group": "periodo", "$limit": 100})
periodos = pd.read_csv(io.StringIO(respuesta.text))["periodo"].astype(str).tolist()
periodos.sort()
print("Periodos encontrados:", periodos)

# 2. Descargar algunas filas de cada periodo
tablas = []
for periodo in periodos:
    pedido = {"$where": f"periodo='{periodo}'", "$limit": filas_por_periodo}
    respuesta = requests.get(url, params=pedido, timeout=120)
    tabla = pd.read_csv(io.StringIO(respuesta.text), low_memory=False)
    print(periodo, "->", len(tabla), "filas")
    tablas.append(tabla)

# 3. Unir todo y guardarlo en data/raw
datos = pd.concat(tablas, ignore_index=True)
os.makedirs("data/raw", exist_ok=True)
datos.to_csv("data/raw/saber11_muestra.csv", index=False)

# 4. Un primer vistazo a los datos
print("\nTamaño:", datos.shape)
print("\nColumnas:", list(datos.columns))
print("\nPrimeras filas:")
print(datos.head())
print("\nNulos por columna:")
print(datos.isna().sum().sort_values(ascending=False).head(15))
