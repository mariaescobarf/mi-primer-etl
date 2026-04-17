#ventas = ["camisa", None, "pantalon", "zapatos"]
#def quitar_nulos(lista):
#    datos_limpios = [i for i in lista if i is not None]
#    return datos_limpios
#
#def formatear_nombres(lista):
#    datos_formateados = [i.upper() for i in lista]
#    return datos_formateados
#
#def procesar_ventas(lista_ventas):
#    datos_finales = formatear_nombres(quitar_nulos(lista_ventas))
#    print(datos_finales)
#
#procesar_ventas(ventas)

ventas_sucias = ["camisa", None, 100, "pantalon", "zapatos", 50.5]

def quitar_nulos(lista):
    datos_limpios = [i for i in lista if i is not None]
    return datos_limpios 

def formatear_nombres(lista):
    exitos = []     
    errores = []
    for i in lista:
        try:
            exitos.append(i.upper())
        except AttributeError as e:
            errores.append(str(e))
    print(f"Numero de exitos: {len(exitos)}, Numero de errores: {len(errores)}")
    return exitos, errores

def procesar_ventas(lista_ventas):
    datos_finales = formatear_nombres(quitar_nulos(lista_ventas))
    print(datos_finales)

procesar_ventas(ventas_sucias)
