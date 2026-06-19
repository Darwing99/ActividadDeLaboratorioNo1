# Análisis de Salarios Tecnológicos

Análisis exploratorio de salarios del sector tecnológico en Latinoamérica y otros países, usando Python y Pandas sobre un dataset de 5,000 registros.

---

## Estructura del Proyecto

```
ProyectoPrueba/
├── data/
│   ├── raw/                  # Datos originales (no modificar)
│   ├── processed/            # Datos limpios generados por el análisis
│   └── external/             # Datos de fuentes externas
├── notebooks/
│   └── 01_eda.ipynb          # Análisis exploratorio principal
├── src/
│   ├── data/
│   │   ├── loader.py         # Carga y guardado de datos
│   │   └── cleaner.py        # Validación y limpieza
│   ├── features/
│   │   └── engineering.py    # Creación de nuevas variables
│   ├── visualization/
│   │   └── plots.py          # Funciones de gráficas
│   └── utils/
│       └── helpers.py        # Funciones de apoyo
├── models/                   # Modelos entrenados y artefactos
├── reports/
│   └── figures/              # Gráficas generadas automáticamente
├── config/
│   └── config.yaml           # Parámetros y rutas centralizadas
├── tests/
│   ├── test_data.py          # Tests de calidad de datos
│   └── test_model.py         # Tests de features
├── requirements.txt
├── .gitignore
└── Dockerfile
```

---

## Requisitos

- Python 3.11+
- Jupyter Notebook o VS Code con extensión de notebooks

---

## Pasos para ejecutar

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Verificar que el dataset existe

Confirmar que el archivo está en su lugar:

```
data/raw/analisis_salarios_tecnologicos_5000.xlsx
```

### 3. Ejecutar los tests de calidad de datos

Antes de analizar, validar que los datos están correctos:

```bash
python tests/test_data.py
```

Salida esperada:
```
OK - Carga de datos
OK - Columnas requeridas presentes
OK - Sin valores nulos
OK - Salarios positivos

Todos los tests pasaron.
```

### 4. Ejecutar los tests de features

```bash
python tests/test_model.py
```

Salida esperada:
```
OK - Feature Rango_Salarial
OK - Feature Salario_ZScore

Todos los tests de features pasaron.
```

### 5. Abrir y ejecutar el notebook

```bash
jupyter notebook notebooks/01_eda.ipynb
```

Ejecutar las celdas **en orden**, de arriba hacia abajo:

| Paso | Descripción |
|------|-------------|
| 01 | Configura la ruta raíz del proyecto |
| 02 | Importa librerías |
| 03 | Carga el dataset desde `data/raw/` |
| 04 | Limpia nombres de columnas |
| 05 | Verifica estructura del dataset |
| 06 | Valida calidad de datos (nulos y duplicados) |
| 07 | Muestra primeros y últimos registros |
| 08 | Estadísticas generales |
| 09 | Indicadores salariales principales |
| 10 | Empleado con salario más alto |
| 11 | Top 10 salarios más altos |
| 12 | Top 10 salarios más bajos |
| 13 | Conteo de empleados, cargos y países |
| 14 | Empleados por país |
| 15 | Empleados por cargo |
| 16 | Salario promedio por cargo |
| 17 | Salario promedio por país |
| 18 | País mejor pagado |
| 19 | Configuración global de gráficas |
| 20 | Histograma de distribución salarial |
| 21 | Gráfica de salario promedio por cargo |
| 22 | Gráfica de salario promedio por país |
| 23 | Gráfica de empleados por país |
| 24 | Boxplot de salarios por cargo |
| 25 | Dashboard resumen (4 gráficas combinadas) |

### 6. Revisar las gráficas generadas

Al terminar el notebook, las imágenes quedan guardadas en:

```
reports/figures/
├── 01_distribucion_salarios.png
├── 02_salario_por_cargo.png
├── 03_salario_por_pais.png
├── 04_empleados_por_pais.png
├── 05_boxplot_cargo.png
└── 06_dashboard_resumen.png
```

---

## Uso de los módulos src

Los módulos de `src/` se pueden importar desde cualquier notebook o script:

```python
from src.data.loader import load_raw_data
from src.data.cleaner import validate_quality
from src.features.engineering import add_salary_range
from src.visualization.plots import plot_salary_by_cargo
from src.utils.helpers import print_salary_stats

df = load_raw_data()
df = add_salary_range(df)
print_salary_stats(df)
```

---

## Ejecutar con Docker

```bash
docker build -t salarios-tech .
docker run -p 8888:8888 salarios-tech
```

Luego abrir en el navegador: `http://localhost:8888`
