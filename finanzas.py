import time
import datetime
import os
hora = datetime.datetime.now().strftime("%Y-%m-%d")
def crear_meta():
    nombre_meta = input("Ingrese el nombre de la meta a alcanzar: ")
    try:
        valor_meta = int(input("Ingrese el valor de la meta: "))
    except:
        print("Valor invalido, intente de nuevo...")
        return
    with open(f"{nombre_meta}", "w") as archivo:
        archivo.write(f"META: {nombre_meta} | {valor_meta}\n")
    print(f"la meta fue guardada exitosamente.")

def registrar_aporte(monto):
    nombre_meta = input("Ingrese el nombre de la meta a la que desea aportar: ")
    existe = os.path.exists(nombre_meta)
    if existe == True:
        with open(f"{nombre_meta}", "r") as archivo:
            print(archivo.read())
        try:
            monto = int(input("Ingrese el monto a aportar: "))
            if monto >= 0:
                hora = datetime.datetime.now().strftime("%Y-%m-%d")
                with open(f"{nombre_meta}", "a") as archivo:
                    archivo.write(f"{hora} | {monto}\n")
        except:
            print("Monto invalido...")
            return
