# Comandos del proyecto

Referencia rápida para el trabajo diario. Los comandos están pensados para PowerShell en Windows y se ejecutan desde la raíz del proyecto, salvo que se indique lo contrario.

## Entorno

| Tarea | Comando |
|---|---|
| Activar el entorno | `conda activate saber11` |
| Salir del entorno | `conda deactivate` |
| Ver los entornos disponibles | `conda env list` |
| Verificar la versión de Python | `python --version` |
| Verificar librerías clave | `python -c "import pandas, sklearn; print(pandas.__version__, sklearn.__version__)"` |
| Instalar dependencias del proyecto | `pip install -r requirements.txt` |
| Instalar dependencias de desarrollo (incluye Jupyter) | `pip install -r requirements-dev.txt` |
| Registrar el entorno como kernel de Jupyter | `python -m ipykernel install --user --name saber11 --display-name "Python (saber11)"` |

**Importante:** `requirements.txt` se mantiene manualmente con las librerías directas del proyecto. No se debe regenerar con `pip freeze`, porque sobrescribiría la lista depurada con todas las dependencias del entorno. Al agregar una librería nueva, se añade su línea con la versión instalada (`pip show nombre` muestra la versión).

## Ejecución del proyecto

| Fase | Tarea | Comando |
|---|---|---|
| 1 | Descargar la muestra de datos | `python src/descargar_datos.py` |
| 3 | Limpiar y preparar los datos | `python src/limpieza.py` (pendiente) |
| 5 | Entrenar y guardar el modelo | `python src/entrenar.py` (pendiente) |
| 7 | Ejecutar la aplicación web | `streamlit run app/app.py` (pendiente) |

## Git

| Tarea | Comando |
|---|---|
| Ver el estado del repositorio | `git status` |
| Preparar todos los cambios | `git add .` |
| Preparar un archivo concreto | `git add ruta/archivo` |
| Guardar los cambios | `git commit -m "mensaje descriptivo"` |
| Subir a GitHub | `git push` |
| Traer cambios de GitHub | `git pull` |
| Ver el historial resumido | `git log --oneline` |
| Ver qué cambió antes de guardar | `git diff` |

Flujo habitual al terminar una tarea:

```powershell
git status
git add .
git commit -m "describe lo que hiciste"
git push
```

## Archivos de apoyo

- `README.md`: estado del proyecto y pasos para reproducirlo.
- `docs/ROADMAP.md`: planificación por fases.
