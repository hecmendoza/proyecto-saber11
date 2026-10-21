# Hoja de ruta: predicción del puntaje global Saber 11

## 1. Objetivo y alcance

**Pregunta de investigación:** ¿en qué medida las condiciones socioeconómicas y las características del colegio explican el puntaje global del Saber 11?

**Entregables:**

1. Modelo de regresión que estima el puntaje global a partir de variables de contexto.
2. Análisis de la importancia de las variables y de las brechas por región y estrato.
3. Aplicación web interactiva que recibe las características de un estudiante y devuelve el puntaje estimado.
4. Repositorio documentado y reproducible.

**Restricción metodológica:** el puntaje global se calcula a partir de los puntajes por materia, por lo que estos se excluyen como variables de entrada para evitar fuga de datos. El modelo utiliza únicamente variables de contexto (estrato, educación de los padres, tipo de colegio, departamento, acceso a internet, entre otras). La lista definitiva se establece al documentar las variables del dataset.

## 2. Datos

| Aspecto | Detalle |
|---|---|
| Fuente | Resultados únicos Saber 11, datos.gov.co (ID `kgxf-xxbe`), publicado por ICFES |
| Cobertura | Descarga de 2010-1 a 2022-4 (23 periodos). El modelado usa 2014-2 a 2022-4 (14 periodos), los únicos con puntaje global |
| Estrategia de muestreo | Hasta 15.000 filas por periodo en la descarga, para garantizar representación de todos los años |
| Tamaño de la muestra | 338.674 filas descargadas; 203.674 con puntaje global; 187.501 tras eliminar duplicados |
| Ubicación | `data/raw/` (sin modificar) y `data/processed/` (datos limpios) |

## 3. Tecnologías

| Componente | Herramienta |
|---|---|
| Lenguaje | Python 3.11 o superior |
| Manipulación de datos | pandas, numpy |
| Visualización | matplotlib, seaborn |
| Modelado | scikit-learn (Pipeline, ColumnTransformer, GridSearchCV) |
| Persistencia del modelo | joblib (el modelo final se incluye en el repositorio para el despliegue) |
| Interpretación | Importancia por permutación (variables más influyentes en el desempeño del modelo); SHAP como complemento opcional (explicación de predicciones individuales) |
| Aplicación web | Streamlit |
| Control de versiones | Git y GitHub |

## 4. Estructura del repositorio

```
proyecto_saber11/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   ├── ROADMAP.md
├── notebooks/
│   ├── 01_exploracion.ipynb
│   ├── 02_limpieza.ipynb
│   ├── 03_modelos.ipynb
│   └── 04_interpretacion.ipynb
├── src/
│   ├── descargar_datos.py
│   ├── limpieza.py
│   ├── entrenar.py
│   └── predecir.py
├── models/
├── reports/
│   └── figures/
├── app/
│   └── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 5. Fases

| Fase | Descripción | Entregable | Estado |
|---|---|---|---|
| 0. Configuración | Estructura del repositorio y control de versiones | Repositorio inicial en GitHub | Pendiente |
| 1. Adquisición de datos | Muestra estratificada por periodo y documentación de variables | Dataset en `data/raw/` y diccionario de variables | En curso (descarga completada; falta el diccionario de variables) |
| 2. Análisis exploratorio | Distribución del puntaje global y su relación con estrato, región y tipo de colegio | Notebook 01 con hallazgos | Pendiente |
| 3. Limpieza y preparación | Eliminación de duplicados y de periodos sin puntaje global, tratamiento de nulos, unificación de categorías y exclusión de variables con fuga | Dataset en `data/processed/` | Pendiente |
| 4. Modelo de referencia | Partición train/test; modelo que predice la media y regresión lineal como líneas base | Métricas de referencia | Pendiente |
| 5. Comparación y ajuste | Ridge, Random Forest y HistGradientBoosting con validación cruzada y búsqueda de hiperparámetros | Tabla comparativa de modelos | Pendiente |
| 6. Interpretación | Importancia de variables y análisis de errores | Notebook 04 y conclusiones | Pendiente |
| 7. Aplicación web | Persistencia del modelo e interfaz en Streamlit | Aplicación funcional | Pendiente |
| 8. Documentación y cierre | README, figuras finales y depuración del repositorio | Proyecto publicable | Pendiente |

Duración estimada: entre 5 y 7 semanas (estimación inicial, sujeta a ajuste).

## 6. Criterios de éxito

- Los modelos superan a la línea base (media) en R² y MAE sobre el conjunto de prueba.
- Ninguna variable de entrada contiene información derivada del puntaje global.
- Los resultados son reproducibles a partir del repositorio.
- La aplicación utiliza el mismo Pipeline del entrenamiento.
- Las limitaciones del modelo quedan documentadas en el README.

## 7. Estrategia de validación

- **Comparación principal:** partición aleatoria 80/20 con `random_state=42` y validación cruzada sobre el conjunto de entrenamiento. El conjunto de prueba se usa una sola vez, al final.
- **Experimento adicional:** entrenamiento con 2014-2 a 2018 y evaluación con 2019 a 2022, para medir la estabilidad del modelo en el tiempo.
- **Métricas:** R² y MAE (error en puntos del puntaje global).

## 8. Riesgos

| Riesgo | Mitigación |
|---|---|
| Fuga de datos por variables derivadas del puntaje global (puntajes por materia, percentiles, niveles de desempeño) | Clasificar cada columna como "disponible antes del examen" o "resultado del examen" en la Fase 3 y conservar solo las primeras |
| Muestra sesgada hacia ciertos periodos | Muestreo con cantidad fija por periodo; tras eliminar duplicados el tamaño por periodo deja de ser uniforme y debe revisarse |
| Registros duplicados en la fuente (concentrados en 2018-1, 2019-4 y 2022-4) | Eliminar duplicados exactos en la Fase 3, antes de dividir en entrenamiento y prueba, para que un mismo estudiante no aparezca en ambos conjuntos |
| Variable objetivo ausente en los periodos anteriores a 2014-2 | Excluir esos periodos del modelado |
| Nombres o categorías de columnas distintos entre años | Homologación documentada en `limpieza.py` |
| Proporción alta de valores nulos en variables clave | Evaluar imputación frente a exclusión y registrar la decisión |
| Tiempos de entrenamiento elevados | Trabajar con muestra y priorizar HistGradientBoosting |

## 9. Convenciones del proyecto

- Los notebooks se destinan a exploración y experimentación; el código reutilizable reside en `src/`.
- Las transformaciones se encapsulan en el Pipeline de scikit-learn.
- El directorio `data/` se excluye del control de versiones; el README describe cómo regenerarlo con `src/descargar_datos.py`.
- En `models/` se excluyen los modelos de experimentación; el modelo final se mantiene en el repositorio, ya que la aplicación lo necesita para el despliegue.
- Los commits son pequeños y con mensajes descriptivos.

## 10. Extensiones opcionales

1. Planteamiento como problema de clasificación (nivel de desempeño bajo, medio y alto).
2. Análisis de brechas por región y por estrato.
3. Despliegue público de la aplicación en Streamlit Community Cloud.
4. Explicaciones individuales de predicciones con SHAP.

## 11. Consideraciones éticas

El modelo describe patrones estadísticos y no está diseñado para evaluar a estudiantes individuales. Las variables socioeconómicas reflejan desigualdad estructural, no capacidad. Los resultados no deben interpretarse como relaciones causales.
