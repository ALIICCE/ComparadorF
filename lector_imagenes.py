'''COMPARADOR DE ARCHIVOS'''

'''Compara dos archivos txt e imprime en terminal sus diferencias
    ademas de generar un archivo "output.txt" donde escribe la salida de la terminal'''

def compara_archivos(archivo1, archivo2):
    with open(archivo1, "r") as f1, open(archivo2, "r") as f2, open("output.txt", "w") as out_file:
        lineas1 = f1.readlines()
        lineas2 = f2.readlines()

        max_lineas = max(len(lineas1), len(lineas2))
        iguales = True

        def escribir(msg=""):
            print(msg)
            print(msg, file=out_file)

        def resumen_diferencias(linea1, linea2, num_linea):
            min_len = min(len(linea1), len(linea2))
            posiciones = []

            for j in range(min_len):
                if linea1[j] != linea2[j]:
                    posiciones.append(j+1)

            if len(linea1) != len(linea2):
                posiciones.extend(range(min_len+1, max(len(linea1), len(linea2))+1))

            if posiciones:
                return f"Diferencias en linea {num_linea} en caracteres {posiciones}"
            return None

        for i in range(max_lineas):
            if i >= len(lineas1):
                escribir(f"El archivo {archivo2} tiene una linea extra en {i+1}: {lineas2[i].strip()}")
                iguales = False
                continue
            if i >= len(lineas2):
                escribir(f"El archivo {archivo1} tiene una linea extra en {i+1}: {lineas1[i].strip()}")
                iguales = False
                continue

            # Compara linea por linea
            if lineas1[i] != lineas2[i]:
                escribir(f"\nDiferencia en la linea {i+1}:")
                escribir(f"  {archivo1}: {lineas1[i].rstrip()}")
                escribir(f"  {archivo2}: {lineas2[i].rstrip()}")

                resumen = resumen_diferencias(lineas1[i], lineas2[i], i+1)
                if resumen:
                    escribir(f"   → {resumen}")

                iguales = False

        if iguales:
            escribir("Los archivos son iguales.")


compara_archivos("foto.txt", "foto2.txt")
