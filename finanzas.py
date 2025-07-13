import time
import datetime
import os
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

def registrar_aporte():
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
    else:
        print("Esta meta no existe...")
        return

def ver_estado():
    nombre_meta = input("Ingrese el nombre de la meta que desea ver sus detalles: ")
    existe = os.path.exists(nombre_meta)
    if existe:
        with open(f"{nombre_meta}", "r") as archivo:
            lineas = archivo.readlines()
            meta_linea = lineas[0].strip()
            _, valor_str = meta_linea.split("|")
            valor_meta = int(valor_str.strip())
            total_aportado = 0
            for linea in lineas[1:]:
                try:
                    _, monto = linea.strip().split("|")
                    total_aportado += int(monto.strip())
                except:
                    pass
        
        print(f"\n📋 Meta: {nombre_meta}")
        print(f"🎯 Valor de la meta: {valor_meta}")
        print(f"💰 Total aportado: {total_aportado}")
        print(f"🔻 Restante: {valor_meta - total_aportado}\n")
    else:
        print("❌ Esta meta no existe.")