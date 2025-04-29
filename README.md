# 🛳️ Titanic (Pandas I) - Análisis Exploratorio de Datos

Este proyecto analiza el famoso dataset del Titanic utilizando **Pandas**. A través de una serie de ejercicios prácticos, se exploran, limpian y transforman los datos con el objetivo de entender mejor las variables, el tratamiento de valores nulos, y la preparación para análisis posterior o modelos de predicción.

---

## 📦 Contenido del repositorio

- `titanic(Pandas I).zip`: Contiene los tres archivos CSV originales:
  - `train.csv`: Conjunto de entrenamiento con información completa de pasajeros.
  - `test.csv`: Conjunto de prueba para predicciones.
  - `gender_submission.csv`: Resultado de predicción básica para el conjunto `test`.

- `notebook.py` o `.ipynb`: Script/cuaderno principal con el desarrollo de todos los ejercicios propuestos.

- `README.md`: Este archivo.

---

## 🧾 Objetivos del proyecto

- Cargar y visualizar datos con `pandas`.
- Analizar estadísticas descriptivas.
- Identificar valores faltantes y tratarlos adecuadamente.
- Filtrar, ordenar y combinar datasets.
- Realizar operaciones lógicas y de limpieza.
- Añadir columnas basadas en otros datasets.

---

## 🧠 Ejercicios destacados

1. **Comparación estadística** entre `train` y `test`.
2. **Ordenamiento personalizado** por `PassengerId`.
3. **Manejo de valores nulos** en la columna `Cabin`.
4. **Filtrado por género** y tarifas.
5. Conversión de columnas a **tipos categóricos**.
6. Relleno de **valores nulos en `Age` con la media**.
7. **Eliminación de columnas innecesarias** (`Cabin`, `Name`).
8. **Fusión de datasets** usando `gender_submission` para añadir la columna `Survived`.

---

## ▶️ Cómo usar este repositorio

1. Clona este repositorio o descarga los archivos manualmente.

2. Asegúrate de tener Python 3 y las librerías necesarias:

```bash
pip install pandas numpy
````

3. Descomprime el archivo titanic(Pandas I).zip en la misma carpeta del notebook.

4. Ejecuta el cuaderno línea por línea para ver los resultados de los ejercicios.

## 📊 Datasets utilizados


| **Archivo**              | **Descripción**                                                                 |
|--------------------------|---------------------------------------------------------------------------------|
| `train.csv`              | Contiene datos de pasajeros (supervivencia, clase, edad, sexo, etc.).           |
| `test.csv`               | Datos similares a `train`, sin la columna `Survived`.                           |
| `gender_submission.csv`  | Predicción básica que indica si el pasajero sobrevivió (usado como base).       |

## ✍️ Autor
Proyecto desarrollado como práctica introductoria a la librería Pandas para análisis de datos.

## 📄 Licencia
Este proyecto es de uso libre con fines educativos. Puedes modificarlo y reutilizarlo dando atribución.
