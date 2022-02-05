# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:56:03 2020

@author: rrodriguez
"""

import pandas as pd
import numpy as np

#1.1-Cargar el archivo "detalle_boletas.csv" en un Data Frame de nombre detalle_boletas
print("1.1-Cargar el archivo detalle_boletas.csv")
detalle_boletas = pd.read_csv("detalle_boletas.csv",encoding="utf-8",sep=",")
print(detalle_boletas.head())
print(detalle_boletas.tail())
print(detalle_boletas.dtypes)
print(detalle_boletas.shape)

#1.2-Eliminar columna "Precio_prod" de detalle_boletas
print("1.2-Eliminar columna Precio_prod")
del detalle_boletas["Precio_prod"]
print(detalle_boletas.head())
print(detalle_boletas.tail())
print(detalle_boletas.dtypes)
print(detalle_boletas.shape)

#1.3-Crear una columna "Pais_Venta" con valores "Chile"
print("1.3-Crear una columna Pais_Venta")
detalle_boletas["Pais_Venta"] = "CHILE"
print(detalle_boletas.head())
print(detalle_boletas.tail())
print(detalle_boletas.dtypes)
print(detalle_boletas.shape)

#1.4-Cambiar el nombre de la columna "NXXX" por "Num Boleta"
print("1.4-Cambiar el nombre de la columna NXXX por Num Boleta")
detalle_boletas = detalle_boletas.rename(columns={"NXXX":"Num Boleta"})
print(detalle_boletas.head())
print(detalle_boletas.tail())
print(detalle_boletas.dtypes)
print(detalle_boletas.shape)

#1.5-Eliminar filas del Data Frame detalle_boletas donde la columna "ID" tenga los valores "4XXXXX" y la columna "Num Boletas" tenga valores “55417XXXXXXX”
print("1.5.1-Eliminar filas de detalle_boletas donde ID = 4XXXXX")
detalle_boletas = detalle_boletas.drop(detalle_boletas[detalle_boletas["ID"]=="4XXXXX"].index)
print(detalle_boletas.loc[detalle_boletas["ID"]=="4XXXXX"])
print(detalle_boletas.head())
print(detalle_boletas.tail())
print(detalle_boletas.dtypes)
print(detalle_boletas.shape)
print("1.5.2-Eliminar filas de detalle_boletas donde Num Boleta = 55417XXXXXXX")
detalle_boletas = detalle_boletas.drop(detalle_boletas[detalle_boletas["Num Boleta"]=="55417XXXXXXX"].index)
print(detalle_boletas.loc[detalle_boletas["Num Boleta"]=="55417XXXXXXX"])
print(detalle_boletas.head())
print(detalle_boletas.tail())
print(detalle_boletas.dtypes)
print(detalle_boletas.shape)

#1.6-Eliminar caracteres extra en la columna "Fecha"
#Referencia: https://www.it-swarm.dev/es/python/eliminar-caracteres-especiales-en-pandas-dataframe/825481028/
#Referencia: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html
print("1.6-Eliminar caracteres extra en la columna Fecha")
detalle_boletas["Fecha"] = detalle_boletas["Fecha"].replace(regex=True, inplace=False, to_replace=r"[^0-9/]", value="")
#detalle_boletas["Fecha"] = detalle_boletas["Fecha"].astype("datetime64")
print(detalle_boletas.head())
print(detalle_boletas.tail())
print(detalle_boletas.dtypes)
print(detalle_boletas.shape)

#1.7-Calcular e imprimir estadísticos descriptivos de la columna "Cantidad" para todos los productos del Data Frame
print("1.7-Calcular e imprimir estadísticos descriptivos de la columna Cantidad")
pt_cantidad = detalle_boletas.pivot_table(index="ID",values="Cantidad",aggfunc={np.mean,np.std,np.min,np.max})
print(pt_cantidad)
print(pt_cantidad.dtypes)
print(pt_cantidad.shape)

#1.8-Separar la columna "Fecha" en tres columnas: "Anho", "Mes" y "Dia"
print("1.8-Separar la columna Fecha en tres columnas: Anho, Mes y Dia")
df_fecha = detalle_boletas["Fecha"].str.split("/",expand=True)
df_fecha.columns=["Anho","Mes","Dia"]
print(df_fecha.head())
print(df_fecha.tail())
print(df_fecha.dtypes)
print(df_fecha.shape)

#1.9-Agregar estas columnas al Data Frame detalle boletas
print("1.9-Agregar estas columnas al Data Frame detalle boletas")
detalle_boletas = detalle_boletas.join(df_fecha)
print(detalle_boletas.head())
print(detalle_boletas.tail())
print(detalle_boletas.dtypes)
print(detalle_boletas.shape)

#1.10-Eliminar la columna "Fecha" después de agregar las columnas "Anho", "Mes" y "Dia"
print("1.10-Eliminar la columna Fecha")
del detalle_boletas["Fecha"]
print(detalle_boletas.head())
print(detalle_boletas.tail())
print(detalle_boletas.dtypes)
print(detalle_boletas.shape)

#2.1-Cargar "Lista productos.csv" en un Data Frame de nombre lista_productos
print("2.1-Cargar Lista productos.csv")
lista_productos = pd.read_csv("Lista productos.csv",encoding="utf-8",sep=",")
print(lista_productos.head())
print(lista_productos.tail())
print(lista_productos.dtypes)
print(lista_productos.shape)

#2.2-Unir el Data Frame lista_productos a detalle_boletas en base a la información de la columna "ID", a un nuevo Data Frame llamado detalle_boletas2
print("2.2-Unir el Data Frame lista_productos a detalle_boletas en detalle_boletas2")
detalle_boletas["ID"] = detalle_boletas["ID"].astype("int64")
detalle_boletas["Anho"] = detalle_boletas["Anho"].astype("int64")
detalle_boletas["Mes"] = detalle_boletas["Mes"].astype("int64")
detalle_boletas["Dia"] = detalle_boletas["Dia"].astype("int64")
print(detalle_boletas.dtypes)
print(detalle_boletas.shape)
detalle_boletas2 = detalle_boletas.merge(lista_productos,left_on="ID",right_on="ID",how="left")

#2.3-Imprimir detalle_boletas2
print("2.3-Imprimir detalle_boletas2")
pd.set_option("display.max_columns",10)
print(detalle_boletas2.head())
print(detalle_boletas2.tail())
print(detalle_boletas2.dtypes)
print(detalle_boletas2.shape)

#2.4-Crear columna "Ingreso total" como la multiplicación de la columna "Precio Unitario" y "Cantidad"
print("2.4-Crear columna Ingreso total = Precio Unitario * Cantidad")
detalle_boletas2["Ingreso total"] = detalle_boletas2["Precio Unitario"] * detalle_boletas2["Cantidad"]

#2.5-Imprimir detalle_boletas2
print("2.5-Imprimir detalle_boletas2")
pd.set_option("display.max_columns",11)
print(detalle_boletas2.head())
print(detalle_boletas2.tail())
print(detalle_boletas2.dtypes)
print(detalle_boletas2.shape)

#2.6-Calcular e imprimir estadísticos descriptivos de la columna "Ingreso total" para todos los productos del Data Frame
print("2.6-Calcular e imprimir estadísticos descriptivos de la columna Ingreso total")
pt_ingreso = detalle_boletas2.pivot_table(index="ID",values="Ingreso total",aggfunc={np.mean,np.std,np.min,np.max})
print(pt_ingreso)
print(pt_ingreso.dtypes)
print(pt_ingreso.shape)

