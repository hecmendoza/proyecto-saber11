# Diccionario de variables

Variables del dataset [Resultados únicos Saber 11](https://www.datos.gov.co/Educaci-n/Resultados-nicos-Saber-11/kgxf-xxbe) (datos.gov.co, ICFES). La descripción proviene de los metadatos del portal; las columnas *Uso previsto* y *Nota* son la clasificación del proyecto y es **provisional**: se confirma en la Fase 3.

En el portal todas las columnas figuran con tipo `text`, incluidos los puntajes. El tipo numérico se verifica en la limpieza.

Los conteos de nulos corresponden a la tabla descargada completa (338.674 filas), antes de filtrar periodos.

## Variable objetivo

| Columna | Descripción (portal) | Uso previsto | Nota |
|---|---|---|---|
| `punt_global` | Puntaje Global | Objetivo | Disponible desde 2014-2. |

## Fuga de datos: resultados del examen

| Columna | Descripción (portal) | Uso previsto | Nota |
|---|---|---|---|
| `punt_ingles` | Puntaje Inglés | Excluir | Resultado del examen. |
| `punt_matematicas` | Puntaje Matemáticas | Excluir | Resultado del examen. |
| `punt_sociales_ciudadanas` | Puntaje Sociales y Ciudadanas | Excluir | Resultado del examen. |
| `punt_c_naturales` | Puntaje Ciencias Naturales | Excluir | Resultado del examen. |
| `punt_lectura_critica` | Puntaje Lectura crítica | Excluir | Resultado del examen. |
| `desemp_ingles` | Desempeño Inglés | Excluir | Se presume derivado del puntaje de inglés; no confirmado. |

## Familia

| Columna | Descripción (portal) | Uso previsto | Nota |
|---|---|---|---|
| `fami_estratovivienda` | Estrato del examinando | Entrada candidata | 11.451 nulos en la tabla descargada. |
| `fami_educacionmadre` | Nivel de estudios de la madre | Entrada candidata | 11.925 nulos en la tabla descargada. |
| `fami_educacionpadre` | Nivel de estudios de la padre | Entrada candidata | 11.913 nulos en la tabla descargada. |
| `fami_tieneinternet` | ¿Tiene internet? | Entrada candidata | 11.114 nulos en la tabla descargada. |
| `fami_tienecomputador` | ¿Tiene computador? | Entrada candidata | 9.628 nulos en la tabla descargada. |
| `fami_tieneautomovil` | ¿Tiene automóvil? | Entrada candidata | 8.889 nulos en la tabla descargada. |
| `fami_tienelavadora` | ¿Tiene lavadora? | Entrada candidata | 8.638 nulos en la tabla descargada. |
| `fami_personashogar` | ¿Con cuantas personas vive? | Entrada candidata | 8.724 nulos en la tabla descargada. |
| `fami_cuartoshogar` | ¿Cuántos cuartos tiene su hogar? | Entrada candidata | 8.689 nulos en la tabla descargada. |

## Colegio

| Columna | Descripción (portal) | Uso previsto | Nota |
|---|---|---|---|
| `cole_naturaleza` | Naturaleza del establecimiento | Entrada candidata |  |
| `cole_area_ubicacion` | Ubicación de la Sede | Entrada candidata |  |
| `cole_calendario` | Calendario del Establecimiento | Entrada candidata |  |
| `cole_caracter` | Carácter del establecimiento | Entrada candidata | 7.666 nulos en la tabla descargada. |
| `cole_jornada` | Jornada de la Sede | Entrada candidata |  |
| `cole_genero` | Genero del Establecimiento | Entrada candidata |  |
| `cole_bilingue` | ¿Es colegio bilingüe? | Entrada candidata | 42.478 nulos en la tabla descargada; revisar tras filtrar periodos. |
| `cole_sede_principal` | ¿Es la sede Principal? | A evaluar |  |
| `cole_depto_ubicacion` | Departamento de la sede | Entrada candidata |  |

## Estudiante

| Columna | Descripción (portal) | Uso previsto | Nota |
|---|---|---|---|
| `estu_depto_reside` | Departamento de residencia del examinando | Entrada candidata |  |
| `estu_estudiante` | S si es estudiante o N si es individual | Excluir | Constante en los datos de trabajo (todos los registros son `ESTUDIANTE`); el portal describe valores S y N que no aparecen. |
| `estu_genero` | Genero del examinando | A evaluar | Atributo sensible; 85 nulos en los datos de trabajo. Se propone usarlo solo para analizar resultados. |
| `estu_fechanacimiento` | Fecha de nacimiento del examinando | A evaluar | No usar la fecha exacta; evaluar derivar la edad. |
| `estu_depto_presentacion` | Departamento de Presentación del examen. | A evaluar | Posible redundancia con el departamento de residencia. |
| `estu_nacionalidad` | Nacionalidad del examinando | A evaluar | Probable baja variabilidad. |
| `estu_pais_reside` | País de residencia del examinando | A evaluar | Probable baja variabilidad. |

## Consentimiento y datos sensibles

| Columna | Descripción (portal) | Uso previsto | Nota |
|---|---|---|---|
| `estu_estadoinvestigacion` | ¿Permite usar sus datos para Investigaciones? | Filtro | La descripción del portal no coincide con los valores observados (`PUBLICAR` y tres estados de validación). Se conservan solo los registros con `PUBLICAR`. |
| `estu_privado_libertad` | ¿Es privado de la libertad? | Excluir | Dato sensible de población vulnerable; 44 registros con `S` en los datos de trabajo. |

## Ubicación de alta cardinalidad

| Columna | Descripción (portal) | Uso previsto | Nota |
|---|---|---|---|
| `cole_mcpio_ubicacion` | Municipio de la sede | Excluir en la primera versión | Muchas categorías. |
| `estu_mcpio_reside` | Municipio de residencia del examinando | Excluir en la primera versión | Muchas categorías. |
| `estu_mcpio_presentacion` | Municipio de Presentación del examen. | Excluir en la primera versión | Muchas categorías. |

## Identificadores y códigos

| Columna | Descripción (portal) | Uso previsto | Nota |
|---|---|---|---|
| `estu_consecutivo` | Identificador del examinando | Auxiliar | Se usa solo para detectar duplicados. |
| `periodo` | Periodo de los resultados | Auxiliar | Se usa para la validación temporal, no como entrada. |
| `estu_tipodocumento` | Tipo de documento | Excluir | Identificador administrativo. |
| `cole_nombre_establecimiento` | Nombre del Establecimiento | Excluir | Identificador con muchas categorías. |
| `cole_nombre_sede` | Nombre de la sede | Excluir | Identificador con muchas categorías. |
| `cole_codigo_icfes` | Código ICFES del Establecimiento | Excluir | Código identificador. |
| `cole_cod_dane_establecimiento` | Código DANE del Establecimiento | Excluir | Código identificador. |
| `cole_cod_dane_sede` | Código DANE de la Sede | Excluir | Código identificador. |
| `cole_cod_depto_ubicacion` | Departamento de la sede | Excluir | Código; duplica cole_depto_ubicacion. |
| `cole_cod_mcpio_ubicacion` | Código Municipio de la sede | Excluir | Código; duplica el municipio. |
| `estu_cod_depto_presentacion` | Código del Departamento de Presentación del examen. | Excluir | Código; duplica el nombre. |
| `estu_cod_mcpio_presentacion` | Código del Municipio de Presentación del examen. | Excluir | Código; duplica el nombre. |
| `estu_cod_reside_depto` | Código del Departamento de residencia del examinando | Excluir | Código; duplica el nombre. |
| `estu_cod_reside_mcpio` | Código del municipio de residencia del examinando | Excluir | Código; duplica el nombre. |
