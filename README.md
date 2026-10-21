# Predicción del puntaje global Saber 11

Proyecto de aprendizaje automático con scikit-learn que estima el puntaje global de la prueba Saber 11 a partir de variables socioeconómicas y características del colegio, usando datos abiertos del ICFES.

**Estado del proyecto:** en desarrollo (Fase 1: adquisición de datos). El plan completo está en [`docs/ROADMAP.md`](docs/ROADMAP.md).

## Pregunta de investigación

¿En qué medida las condiciones socioeconómicas y las características del colegio explican el puntaje global del Saber 11?

## Datos

- **Fuente:** [Resultados únicos Saber 11](https://www.datos.gov.co/Educaci-n/Resultados-nicos-Saber-11/kgxf-xxbe), datos.gov.co, publicado por ICFES.
- **Muestreo:** cantidad fija de filas por periodo, para que todos los años estén representados.
- **Cobertura utilizable:** el puntaje global solo existe desde 2014-2, por lo que el modelado usa 14 periodos (2014-2 a 2022-4) y 187.501 registros tras eliminar duplicados.
- **Variables de entrada:** únicamente variables disponibles antes del examen. Los puntajes por materia y cualquier columna derivada del puntaje global se excluyen para evitar fuga de datos.

Los datos no se incluyen en el repositorio. Se descargan con `src/descargar_datos.py`.

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

Los pasos de limpieza, entrenamiento y ejecución de la aplicación se documentarán a medida que avance el proyecto.

## Resultados

Pendiente.

## Limitaciones y consideraciones éticas

El modelo describe patrones estadísticos y no está diseñado para evaluar a estudiantes individuales. Las variables socioeconómicas reflejan desigualdad estructural, no capacidad, y los resultados no deben interpretarse como relaciones causales.

## Fuente de los datos y licencia

Los datos pertenecen al ICFES y se publican en el portal de datos abiertos del Gobierno de Colombia. Consulta los términos de uso en la página del dataset.
