import csv
import json
from pathlib import Path

#Configuracion de rutas
BASE_DIR = Path(__file__).resolve().parent #funciona como un "pivote" para construir rutas relativas
RUTA_INPUT = BASE_DIR / "Bronze" / "ventas_sucias.csv" #vemos que se reutilzia el BASE_DIR para construir la ruta de entrada y salida, lo que hace que el codigo sea mas flexible y facil de mantener. Si se mueve el proyecto a otra ubicacion, solo se necesita actualizar el BASE_DIR.
RUTA_OUTPUT = BASE_DIR / "Silver" / "ventas_limpias.json"

#Funciones de transformacion
def quitar_nulos(lista):
    datos_limpios = [i for i in lista if i is not None and str(i).strip() != ''] # Mantiene el dato 'i' SOLO SI no es None Y si al quitarle espacios (.strip()) no queda vacío ('').
    return datos_limpios

def formatear_nombres(lista):
    exitos = []     
    errores = []
    for i in lista:
        try:
            exitos.append(str(i).upper())
        except AttributeError as e:
            errores.append({"valor": i, "error": str(e)})
    print(f"Numero de exitos: {len(exitos)}, Numero de errores: {len(errores)}")
    return exitos, errores

#Ejecucion del pipeline
def ejecutar_pipeline():
    if not RUTA_INPUT.exists():
        print(f"No encuentro el archivo en: {RUTA_INPUT}")
        return
    
    with open(RUTA_INPUT, mode='r', encoding='utf-8') as archivo:
        reader = csv.reader(archivo)
        next(reader)
        lista_ventas = [row[0] for row in reader if row]
    
    datos_limpios = quitar_nulos(lista_ventas)
    datos_formateados, errores = formatear_nombres(datos_limpios)
    
    with open(RUTA_OUTPUT, mode='w', encoding='utf-8') as archivo_salida:
        json.dump({"ventas": datos_formateados, "errores": errores}, archivo_salida, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    ejecutar_pipeline()

#Comentario para ensayar guardar cambios en git.