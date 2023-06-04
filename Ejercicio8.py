# Create a Python program that reads a text file and counts the occurrences of each word using a dictionary. 
# The program should print the words and their counts.

def contar_ocurrencias(archivo):
    
    with open(archivo, 'r') as file: 
        ocurrencias = {} 

        for linea in file:
            
            palabras = linea.strip().split() # Dividir la línea en palabras
        
            for palabra in palabras:
                if palabra in ocurrencias:
                    ocurrencias[palabra] += 1
                else:
                    ocurrencias[palabra] = 1

    for palabra, cuenta in ocurrencias.items():
        print(f'{palabra}: {cuenta}')


archivo = 'archivo_de_lectura.txt'  # Guardar el archivo en la misma carpeta del archivo py
contar_ocurrencias(archivo)
