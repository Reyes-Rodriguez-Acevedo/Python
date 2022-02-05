print("2. Abrir el archivo “base_de_datos_de_clientes.csv” en Python")
informacion_archivo = open("base_de_datos_de_clientes.csv")
print(informacion_archivo)

print("Leer el archivo:\nbase_de_datos_de_clientes.csv")
informacion_archivo = open("base_de_datos_de_clientes.csv","r",encoding="latin-1")
lineas = informacion_archivo.readlines()
informacion_archivo.close()
for linea in lineas:
	print(linea)

print("3. Cargar la información del archivo “base_de_datos_de_clientes.csv” a Python")
archivo = open("base_de_datos_de_clientes.csv","r",encoding="latin-1")
archivo_en_lineas = archivo.readlines()
numero_de_clientes = len(archivo_en_lineas)
'archivo.close()'
matriz_de_datos = []
for linea in archivo_en_lineas:
	linea = linea.strip()
	fila = linea.split(";")
	matriz_de_datos.append(fila)
print(matriz_de_datos)

print("5. La información que contiene el archivo en algunos casos se encuentra corrupta\ni. Quitar los caracteres extra al principio de la columna RUT")
for fila in matriz_de_datos:
    RUT = fila[0]
    fila[0] = RUT[5:len(RUT)]
print(fila[0])

print("5. La información que contiene el archivo en algunos casos se encuentra corrupta\nii. Eliminar los guiones (“-“) en la Fecha de Nacimiento")
for fila in matriz_de_datos:
    fecha_de_nacimiento = fila[3]
    fila[3] = fecha_de_nacimiento.replace("-","")
print(fila[3])

print("6. calcular la edad de cada persona como una resta simple entre el año actual (2018) y el año de la fecha de nacimiento")
for fila in matriz_de_datos:
    fecha_de_nacimiento = fila[3]
    fecha_de_nacimiento_lista = fecha_de_nacimiento.split("/")
    edad = fila[4]
    fila[4] = 2018 - int(fecha_de_nacimiento_lista[0])
print(fila[4])

print("7. Guarda los cambios realizados en los pasos anteriores en un archivo con formato CSV de nombre “clientes_limpio.csv”")
archivo_guardar = open("clientes_limpio.csv","w",encoding="latin-1")
archivo_guardar.write("RUT;Nombre;Género;Fecha de Nacimiento;Edad;Tipo cliente;Monto;Puntaje Crediticio\n")
archivo_guardar = open("clientes_limpio.csv","a",encoding="latin-1")
for fila in matriz_de_datos:
	fila_para_escribir = ""
	for i in range(0,len(fila)):
		if i == len(fila)-1:
			fila_para_escribir += str(fila[i])
		else:
			fila_para_escribir += str(fila[i]) + ";"
	fila_para_escribir += "\n"
	archivo_guardar.write(fila_para_escribir)
archivo_guardar.close()





















