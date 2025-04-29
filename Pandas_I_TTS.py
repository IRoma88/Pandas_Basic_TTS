# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np

"""En este primer proyecto vamos a trabajar con el famoso dataset del Titanic.

En el siguiente enlace puedes descargar un zip que conitene 3 csv: https://drive.google.com/file/d/11P8Z3B4jgFbrMnyksamaF9sJFv245v24/view?usp=drive_link.

Carga los 3 archivos en el cuaderno, crea los datasets correspondientes (con el mismo nombre, sin el .csv ) y comprueba los 5 primeros elementos de cada archivo.
"""

train = pd.read_csv('/content/train.csv')

gender_submission =pd.read_csv('/content/gender_submission.csv')

test = pd.read_csv('/content/test.csv')

train.head()

test.head()

gender_submission.head()

"""#Ejercicio 1

Utiliza el método describe para comparar los dataframe 'train' y 'test'
"""

train.describe()

test.describe()

"""Almacena en la **solución_1** el nombre del dataset (cadena de texto) como que contenga la edad máxima más alta y en la **solución_1b** el nombre del que tenga la media de edad más alta.

El resultado tiene que ser algo con un formato, por ejemplo:

`solucion_1 = "test"`
"""

edad_alta = train['Age'].max()

solucion_1= edad_alta

edad_media = train['Age'].mean()

solucion_1b= edad_media

solucion_1, solucion_1b

"""#Ejercicio 2

Actualiza el dataframe 'train' para que quede ordenado por la columna PassengerID de menor a mayor y lo mismo para el dataframe 'test' pero con orden de mayor a menor.
"""



"""Almacena en la variable solucion_2 los 10 primeros elementos del dataframe 'train' y en la variable solucion_2b los 10 primeros del dataframe 'test'."""

solucion_2=train.sort_values(['PassengerId'],ascending=True).head(10)

solucion_2b=test.sort_values(['PassengerId'],ascending=True).head(10)

solucion_2

solucion_2b

"""#Ejercicio 3

Si te has fijado, en la columna 'Cabin' hay muchos valores que faltan (NaN). Almacena los dataframes 'train' y 'test' en las variables solucion_3 y solucion_3b, respectivamente, ordenados según el número de cabina de menor a mayor y dejando en último lugar las filas con valores faltantes.

**Pista: puedes usar el argumento na_position**
"""

solucion_3=train.sort_values(['Cabin'],ascending=True,na_position='last')
solucion_3b=test.sort_values(['Cabin'],ascending=True,na_position='last')

solucion_3

solucion_3b

"""#Ejercicio 4

Almacena en la variable solucion_4 el número total de mujeres que había en el titanic (sumando las de ambos dataframe)
"""

Sexos_train = pd.DataFrame(train.groupby(['Sex'])['PassengerId'].count()).rename(columns={'PassengerId':'Sex_train'})
Sexos_train

Sexos_test = pd.DataFrame(test.groupby(['Sex'])['PassengerId'].count()).rename(columns={'PassengerId':'Sex_test'})
Sexos_test

sexos_totales = pd.concat([Sexos_train,Sexos_test],axis=1)
sexos_totales

Sexos_suma = sexos_totales.sum(axis=1)

solucion_4= Sexos_suma['female']


solucion_4

"""#Ejercicio 5

Convierte la columna 'Embarked' de los dataframe 'train' y 'test' a una de tipo categórica y comprueba que valores puede tomar esta variable usando el método dtype.
"""

# Convertir 'Embarked' a tipo categórico
train['Embarked'] = train['Embarked'].astype('category')
test['Embarked'] = test['Embarked'].astype('category')

# Comprobar el tipo de datos y los valores únicos
print(train['Embarked'].dtype)  # Verifica que ahora es categoría
print(test['Embarked'].dtype)

print(train['Embarked'].cat.categories)  # Valores únicos en train
print(test['Embarked'].cat.categories)   # Valores únicos en test

"""Almacena en la variable solución 5 los pasajeros que tenian el valor en la columna 'Embarked' distinto de 'C' del dataframe 'train'."""

solucion_5=train[train['Embarked'] != 'C']

solucion_5

"""# Ejercicio 6

Almacena en la variable solucion_6 el resultado de filtrar el dataframe 'test' para los pasajeros 'hombres' con tarifa ('Fare') menor que 100.
"""

solucion_6=test[(test['Sex'] == 'male') & (test['Fare'] < 100)]

solucion_6

"""Y en la variable solucion_6b el resultado de filtrar el dataset 'test' por aquellos cuya tarifa ('Fare') sea superior a 500 o su edad superior a 70 años."""

solucion_6b=test[(test['Fare'] > 500) | (test['Age'] > 70)]

solucion_6b

"""#Ejercicio 7

Comprueba en qué columnas faltan datos y cuantos faltan para el dataframe 'train'. Almacenalo en la variable solucion_7.
"""

solucion_7=train.isnull().sum()

solucion_7

"""#Ejercicio 8

Vamos a eliminar las columnas 'Cabin' (porque tiene muchos missing values) y la columna nombre (porque ocupa mucho y no es información que nos resulte útil en este punto). Almacénalo en el dataframe train_cleaned y test_cleaned respectivamente
"""

train_cleaned=train.drop(columns=['Cabin', 'Name'])
train_cleaned

test_cleaned=test.drop(columns=['Cabin', 'Name'])
test_cleaned

"""#Ejercicio 9

Rellena los valores desconocidos de la columna edad, de los dataframes resultantes del ejercicio anterior, con la media de edad respectiva de cada dataframe.



"""

train_cleaned['Age'].fillna(train_cleaned['Age'].mean(), inplace=True)
test_cleaned['Age'].fillna(test_cleaned['Age'].mean(), inplace=True)

train_cleaned, test_cleaned

"""#Ejercicio 10

Por último utiliza el dataframe gender_submission para añadir la columna Survived al dataframe test_cleaned.
"""

test_cleaned['Survived'] = gender_submission['Survived']

test_cleaned


  print('¡Felicidades! puedes avanzar al siguiente modulo \n El token es: ',pwd.hexdigest())
else:
  print('Hay algún error en el código o tu forma es diferente a la planteada, pregunta por el foro si no lo ves claro.')
