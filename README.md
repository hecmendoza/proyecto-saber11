# Predicción del puntaje global Saber 11

Proyecto de aprendizaje automático con scikit-learn que estima el puntaje global de la prueba Saber 11 a partir de variables socioeconómicas y características del colegio, usando datos abiertos del ICFES.

**Estado del proyecto:** en desarrollo (Fase 4: modelo de referencia). El plan completo está en [`docs/ROADMAP.md`](docs/ROADMAP.md).

## Pregunta de investigación

¿En qué medida las condiciones socioeconómicas y las características del colegio explican el puntaje global del Saber 11?

## Datos

- **Fuente:** [Resultados únicos Saber 11](https://www.datos.gov.co/Educaci-n/Resultados-nicos-Saber-11/kgxf-xxbe), datos.gov.co, publicado por ICFES.
- **Muestreo:** hasta 15.000 filas por periodo, para que todos los años estén representados.
- **Cobertura utilizable:** el puntaje global solo existe desde 2014-2, por lo que el modelado usa 14 periodos (2014-2 a 2022-4). De 338.674 filas descargadas quedan 145.647 tras la limpieza.
- **Variables de entrada:** únicamente variables disponibles antes del examen. Los puntajes por materia y cualquier columna derivada del puntaje global se excluyen para evitar fuga de datos. La descripción de cada variable está en [`docs/diccionario_variables.md`](docs/diccionario_variables.md).

Los datos no se incluyen en el repositorio. Se descargan con `src/descargar_datos.py`.

## Exploración de los datos

El puntaje global promedio sube de forma clara con las condiciones del hogar y del colegio:

- **Estrato:** de 237,1 puntos en el estrato 1 a 339,4 en el estrato 6.
- **Educación de la madre:** de 218,7 (sin estudios) a 341,8 (postgrado).
- **Colegio bilingüe:** 342,4 puntos en promedio frente a 270,3 en los no bilingües.

Estos promedios se calcularon sobre los 186.950 registros previos a eliminar los datos vacíos. Son asociaciones y no causas, porque estas variables se relacionan entre sí. Las gráficas están en [`reports/figures/`](reports/figures/).

## Tecnologías

Python 3.11, pandas, numpy, scikit-learn, matplotlib, seaborn, joblib y Streamlit.

## Estructura del repositorio

```
proyecto-saber11/
├── data/           # datos crudos y procesados (no versionados)
├── docs/           # hoja de ruta, comandos y diccionario de variables
├── notebooks/      # exploración y experimentos
├── src/            # código reutilizable
├── models/         # modelo final
├── reports/        # figuras y resultados
├── app/            # aplicación web (Streamlit)
├── requirements.txt
└── requirements-dev.txt
```

## Reproducción

1. Clonar el repositorio y crear un entorno con Python 3.11.
2. Instalar las dependencias: `pip install -r requirements.txt` (o `requirements-dev.txt` para trabajar con notebooks).
3. Descargar los datos desde la raíz del proyecto: `python src/descargar_datos.py`.
4. Limpiar los datos: `python src/limpieza.py`. Genera `data/processed/saber11_limpio.csv`.

Los pasos de entrenamiento y ejecución de la aplicación se documentarán a medida que avance el proyecto.

## Resultados

Pendiente.

## Limitaciones y consideraciones éticas

Limitaciones conocidas hasta ahora:

- Se eliminaron los registros con datos vacíos en alguna variable de entrada, cerca del 20 % de la base de trabajo. Esos registros puntúan en promedio menos (262,1 frente a 283,1 en los que se conservan, medido antes de las correcciones finales), por lo que el modelo puede quedar inclinado hacia puntajes altos.
- Se eliminó cerca del 3 % de los registros restantes por fechas de nacimiento imposibles.
- La descarga toma hasta 15.000 registros por periodo. En los periodos más grandes no se verificó que esa muestra sea representativa.

El modelo describe patrones estadísticos y no está diseñado para evaluar a estudiantes individuales. Las variables socioeconómicas reflejan desigualdad estructural, no capacidad, y los resultados no deben interpretarse como relaciones causales.

## Fuente de los datos

Los datos pertenecen al ICFES y se publican en el portal de datos abiertos del Gobierno de Colombia. Consulta los términos de uso en la página del dataset.
