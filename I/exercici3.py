#Renaming files
import os
def nameChanger():
    #se podria hacer en 1 solo input
    directory = input("Ruta del directori")
    fileName = input("Nom actual de l'arxiu:")
    newFileName = input("Nou nom de l'arxiu:")
   
    if os.path.isdir(directory):

        for file in os.listdir(directory):
            if file == fileName:
               # os.rename(f"{directory}/{file}", f"{directory}/{newFileName}")
                os.rename(os.path.join(directory, file), os.path.join(directory, newFileName)) #el path.join comprueba que el archivo existe en ese directorio
                print(f"Arxiu renombrat: '{file}' -> '{newFileName}'")
                return
        print(f"No existeix cap arxiu amb el nom '{fileName}'")

    else:
        print("Ruta no vàlida.")


nameChanger()