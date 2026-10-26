import os

import pandas as pd

ruta_entrada = "data/raw/saber11_muestra.csv"
ruta_salida = "data/processed/saber11_limpio.csv"

columnas = [
    "cole_area_ubicacion", "cole_bilingue", "cole_caracter",
    "cole_depto_ubicacion", "cole_genero", "cole_jornada",
    "cole_naturaleza", "estu_fechanacimiento", "estu_depto_reside",
    "fami_educacionmadre", "fami_educacionpadre", "fami_estratovivienda",
    "fami_personashogar", "fami_cuartoshogar", "fami_tieneinternet",
    "fami_tienecomputador", "fami_tieneautomovil", "fami_tienelavadora",
    "punt_global", "periodo",
]

# Límites de edad (se eliminan las fechas de nacimiento imposibles)
edad_min, edad_max = 12, 60


def limpiar(datos):
    # 1. Conservar solo registros con puntaje global
    trabajo = datos[datos["punt_global"].notna()]
    print("Con puntaje global:", len(trabajo))

    # 2. Eliminar registros duplicados
    trabajo = trabajo.drop_duplicates()
    print("Sin duplicados:", len(trabajo))

    # 3. Conservar registros con estado PUBLICAR
    trabajo = trabajo[trabajo["estu_estadoinvestigacion"] == "PUBLICAR"]
    print("Estado PUBLICAR:", len(trabajo))

    # 4. Eliminar puntajes iguales a cero
    trabajo = trabajo[trabajo["punt_global"] > 0]
    print("Puntaje mayor que 0:", len(trabajo))

    # 5. Seleccionar las columnas a usar y eliminar filas con datos vacíos
    completo = trabajo.dropna(subset=columnas)[columnas].copy()
    print("Sin datos vacíos:", len(completo))

    # 6. Unificar BOGOTA y BOGOTÁ
    completo["cole_depto_ubicacion"] = completo["cole_depto_ubicacion"].replace({"BOGOTA": "BOGOTÁ"})

    # 7. Unificar el formato de personas en el hogar
    # Antes de 2017 vienen como palabras y después como rangos; todo pasa a rangos
    completo["fami_personashogar"] = completo["fami_personashogar"].replace({
        "Una": "1 a 2", "Dos": "1 a 2", "Tres": "3 a 4", "Cuatro": "3 a 4",
        "Cinco": "5 a 6", "Seis": "5 a 6", "Siete": "7 a 8", "Ocho": "7 a 8",
        "Nueve": "9 o más", "Diez": "9 o más", "Once": "9 o más", "Doce o más": "9 o más",
    })

    # 8. Agrupar los valores altos de cuartos del hogar en "Seis o más"
    completo["fami_cuartoshogar"] = completo["fami_cuartoshogar"].replace({
        "Seis": "Seis o más", "Seis o mas": "Seis o más", "Siete": "Seis o más",
        "Ocho": "Seis o más", "Nueve": "Seis o más", "Diez o más": "Seis o más",
    })

    # 9. Eliminar "NO APLICA" en carácter del colegio y el único estudiante extranjero
    completo = completo[completo["cole_caracter"] != "NO APLICA"]
    completo = completo[completo["estu_depto_reside"] != "EXTRANJERO"]
    print("Tras las correcciones:", len(completo))

    # 10. Calcular la edad aproximada: año del examen menos año de nacimiento
    anio_examen = completo["periodo"] // 10
    anio_nacimiento = pd.to_numeric(completo["estu_fechanacimiento"].str[-4:], errors="coerce")
    completo["edad"] = anio_examen - anio_nacimiento

    # 11. Eliminar edades imposibles y la fecha de nacimiento
    completo = completo[completo["edad"].between(edad_min, edad_max)].copy()
    completo["edad"] = completo["edad"].astype(int)
    completo = completo.drop(columns="estu_fechanacimiento")
    print("Con edad válida:", len(completo))

    return completo


if __name__ == "__main__":
    datos = pd.read_csv(ruta_entrada, low_memory=False)
    print("Descarga completa:", len(datos))

    completo = limpiar(datos)

    os.makedirs("data/processed", exist_ok=True)
    completo.to_csv(ruta_salida, index=False)
    print("\nGuardado en", ruta_salida)
    print("Filas:", len(completo), "| Columnas:", len(completo.columns))