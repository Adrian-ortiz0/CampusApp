import json
from datetime import datetime
import os
import time

ruta = "data.json"

#Funciones de orden

def clear():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

def wait_for_keypress():
    print("Presiona cualquier tecla para continuar...")
    os.system('pause >nul')

#Funciones de guardar y cargar

def leer_datos():

    try:
        with open(ruta, "r") as archivo:
            file = json.load(archivo)
            print("Se cargó correctamente")
            return file
        
    except FileNotFoundError:
        print("No existe el archivo!")
        
def guardar_datos(data):
    try:
        with open(ruta, "w") as archivo:
            json.dump(data, archivo, indent=4)
            print("Se guardaron los datos correctamente!")
    except FileNotFoundError:
        print("Error guardando los datos: archivo no encontrado!")

#---------------------------------------------------------------------



def menu_usuarios():
    data = leer_datos()
    print("*************************************")
    print("Bienvenido al inicio de sesión de usuarios!")
    identificacion = input("Ingresa tu número de documento: ")
    
    if identificacion in data["estudiantes"] and data["estudiantes"][identificacion]["estado"] == "aprobado":
        usuario = data["estudiantes"][identificacion]
        print(f"Bienvenido usuario {usuario['nombre']}")
        print("**********************************************************")
        print(f"ID: {identificacion} - Ruta: {usuario['ruta']} - Trainer: {usuario['trainer']}")
            
        while True:

            print("Menu camper!")
            print("****************************************")
            print("1. Ver notas")
            print("2. Ver trainer")
            print("3. Salir")
            opt = int(input("Que deseas hacer? "))
            if opt == 1:
                print("notas")
            elif opt == 2:
                print("marino")
            elif opt == 3:
                print("Adios")
                break
            else:
                print("Ese comando no existe!")
                continue
    else:
        print("No existe el usuario!")
        
def menu_administradores():
    data = leer_datos()
    try:
        while True:
            print("Bienvenido al menu de administradores!")
            print("******************************************")
            print("1. Aprobar campers (Realizar pruebas)")
            print("2. Contratar trainers")
            print("3. Asignar trainers a rutas")
            print("4. Asignar campers a trainers")
            print("5. Eliminar campers")
            print("6. Asignar salones")
            print("7. Salir")
            opt = int(input("Ingresa una opcion: "))
            if opt == 1:
                aprobar_campers()
            elif opt == 2:
                contratar_trainers()
            elif opt == 3:
                asignar_rutas()
            elif opt == 4:
                asignar_campers()
            elif opt == 5:
                eliminar_campers()
            elif opt == 6:
                asignar_salones()
            elif opt == 7:
                break
            else:
                print("El comando no existe!")
    except ValueError:
            print("Error ingresando valor!")

def menu_trainers():
    data = leer_datos()
    identificacion = input("Ingresa tu documento, trainer: ")
    if identificacion in data["trainers"]:   
        print(f"Bienvenido al menu trainer {data['trainers'][identificacion]['nombre']}!")
        print("******************************************")
    else:
        print("No existe ese documento!")

def menu_principal():
    data = leer_datos()
    while True:
        print("Bienvenido a campuslands, elige una opcion!")
        print("*******************************************")
        print("1. Incribirse")
        print("2. Ingresar como usuario")
        print("3. Ingresar como administrador")
        print("4. Ingresar como trainer")
        print("5. Salir")
        
        try:   
            opt = int(input("Ingresa una opcion: "))
            if opt == 1:
                registrar_usuarios()
            elif opt == 2:
                menu_usuarios()
            elif opt == 3:
                menu_administradores()
            elif opt == 4:
                menu_trainers()
            elif opt == 5:
                clear()
                print("Saliendo...")
                time.sleep(2)
                break
            else:
                print("La opcion que ingresaste no esta disponible!")
        except Exception:
            print("El valor ingresado no es valido!")

#Funciones 1. Registro inicial
def registrar_usuarios():
    data = leer_datos()
    clear()
    while True:    
        print("Bienvenido al sistema de registro de campers!")
        print("*************************************************")
        
        opt = int(input("Esta seguro que desea inscribirse?(1.Si/2.No) "))
        if opt == 1:
            try:    
                identificacion = int(input("Ingresa un numero de documento: "))
                
            except ValueError:
                print("Por favor ingresa un valor valido!")
                continue
            if data["estudiantes"].get(str(identificacion), None) is None:
                nombre = input("Ingresar nombre del camper: ")
                edad = int(input("Ingresar la edad del camper: "))
                celular = input("Ingrese su numero de celular: ")
                estado = "inscrito"
                usuario= {
                    "nombre": nombre,
                    "edad": edad,
                    "celular": celular,
                    "estado": estado,
                    "pruebas" : {},
                    "notas" : {},
                    "trainer" : "",
                    "ruta" : ""
                }
                data["estudiantes"][str(identificacion)] = usuario
                clear()
                print("Usuario Registrado con exito!")
                wait_for_keypress()
            else:
                clear()
                print("Ese numero de documento ya fue ingresado!")
                time.sleep(1)
                continue
            guardar_datos(data)
            break
        elif opt == 2:
            break
        else:
            print("Por favor elige entre alguna de las dos opciones disponibles!")
            continue

def aprobar_campers():
    data = leer_datos()
    clear()
    print("Bienvenido al sistema de pruebas para estudiantes inscritos!")
    print("************************************************************")
    while True:
        try:
            elec = int(input("Desea probar campers?(1.Si/2.No) "))
            if elec == 1:
                identificacion = input("Ingresa el documento del camper que deseas probar: ")
                try:
                    if identificacion in data["estudiantes"] and data["estudiantes"][identificacion]["estado"] == "inscrito":
                        nota_cognititva = int(input("Ingresar nota cognititva: "))
                        data["estudiantes"][identificacion]["pruebas"]["Nota cognitiva"] = nota_cognititva
                        nota_habilidades = int(input("Ingresar nota de habilidades: "))
                        data["estudiantes"][identificacion]["pruebas"]["Nota de habilidades"] = nota_habilidades
                        if (nota_cognititva + nota_habilidades) / 2 > 70:
                            data["estudiantes"][identificacion]["estado"] = "Aprobado"
                        else:
                            data["estudiantes"][identificacion]["estado"] = "reprobado"
                        guardar_datos(data)
                    else:
                        clear()
                        print("El camper no existe o el estado del camper ya no es de 'Inscrito' ")
                        break
                except ValueError:
                    print("Ingresar un valor valido!")
                    continue
            elif elec == 2:
                clear()
                time.sleep(2)
                print("Volviendo...")
                break
            else:
                print("Ingresa una opcion valida!")
        except ValueError:
            print("Ingrese un valor valido!")
            continue
                
def eliminar_campers():
    data = leer_datos()
    clear()
    while True:
        print("Bienvenido al sistema de eliminacion de campers!")
        print("************************************************")
        elec = int(input("Estas seguro que deseas continuar? (1.Si/2.No): "))
        try:
            if elec == 1:
                documento = input("Ingresa el numero de documento del camper a eliminar: ")
                if documento not in data["estudiantes"]:
                    print("Ese camper no esta registrado!")
                else:
                    camper_eliminado = data["estudiantes"][documento]
                    while True:
                        print(f"Estas seguro de que deseas eliminar al camper {camper_eliminado['nombre']}? ")
                        opt = int(input("(1.Si / 2.No): "))
                        if opt == 1:
                            data["estudiantes"].pop(documento, None)
                            clear()
                            print("Camper eliminado con exito!")
                            guardar_datos(data)
                            time.sleep(2)
                            wait_for_keypress()
                            break
                        elif opt == 2:
                            clear()
                            time.sleep(1)
                            print("Volviendo...")
                            break
            elif elec == 2:
                clear()
                print("Saliendo...")
                time.sleep(1)
                break
            else:
                print("Ingresa una opcion valida!")
        except ValueError:
            print("Ingrese un valor numerico")
            continue
        
def contratar_trainers():
    data = leer_datos()
    clear()
    while True:
        print("Bienvenido al sistema de contratacion de trainers!")
        elec = int(input("Deseas continuar? (1.Si/2.No): "))
        try:   
            if elec == 1:
                documento = input("Ingresa el documento de identidad del trainer: ")
                nombre = input("Ingresa el nombre del trainer: ")
                while True:
                    print("1. 6:30am - 9:00am")
                    print("2. 9:00am - 1:00pm")
                    print("3. 2:00pm - 6:00pm")
                    opt_horario = int(input("Ingresa el horario que favorece al trainer: "))
                    horario = None
                    if opt_horario == 1:
                        horario = "6:30am - 9:00am"
                        break
                    elif opt_horario == 2:
                        horario = "9:00am - 1:00pm"
                        break
                    elif opt_horario == 3:
                        horario = "2:00pm - 6:00pm"
                        break
                    else:
                        print("Selecciona una opcion que este disponible!")
                        continue    
                trainer = {
                    "nombre" : nombre,
                    "horario" : horario,
                    "ruta" : "",
                    "salon" : ""
                }
                data["trainers"][documento] = trainer
                guardar_datos(data)
                break
            elif elec == 2:
                print("Saliendo...")
                time.sleep(2)
                break
        except Exception:
            print("Valor no valido!")

def asignar_salones():
    data = leer_datos()
    count = 1
    while True:
      try:  
        print("Bienvenido al sistema de asignacion de salones!")
        opt = int(input("Estas seguro de que deseas continuar? (1.Si/2.No): "))
        if opt == 1:
            documento = input("Ingresa el documento del trainer a asignar salon: ")
            horario_trainer = data["trainers"][documento]["horario"]
            if documento in data["trainers"]:
                for salones in data["salones"]:
                    print(f"{count}. {salones}")
                    count += 1
                count = 1
                elec = int(input(f"Elige el salon al que deseas inscribir al trainer: {data['trainers'][documento]['nombre']} "))
                if elec == 1:
                    opc = int(input(f"Estas seguro que deseas asignar al salon kepler?: (1.Si/2.No): "))
                    if opc == 1:
                        if horario_trainer in data["salones"]["kepler"] and data["trainers"][documento]["nombre"] not in data["salones"]["sputnik"][horario_trainer]["profesor"] and data["trainers"][documento]["nombre"] not in data["salones"]["apollo"][horario_trainer]["profesor"]:
                           data["salones"]["kepler"][horario_trainer]["profesor"] = data["trainers"][documento]["nombre"]
                           data["trainers"][documento]["salon"] = "kepler"
                           guardar_datos(data)
                        else:
                            clear()
                            print("Hay cruce de horarios!")
                            time.sleep(1)
                    elif opc == 2:
                            clear()
                            print("Saliendo...")
                            time.sleep(2)
                            break
                    else:
                        print("Ingrese una opcion valida!")
                        continue
                elif elec == 2:
                    opc = int(input(f"Estas seguro que deseas asignar al salon sputnik?: (1.Si/2.No): "))
                    if opc == 1:
                        if horario_trainer in data["salones"]["sputnik"] and data["trainers"][documento]["nombre"] not in data["salones"]["kepler"][horario_trainer]["profesor"] and data["trainers"][documento]["nombre"] not in data["salones"]["apollo"][horario_trainer]["profesor"]:
                           data["salones"]["sputnik"][horario_trainer]["profesor"] = data["trainers"][documento]["nombre"]
                           data["trainers"][documento]["salon"] = "sputnik"
                           guardar_datos(data)
                        else:
                            clear()
                            print("Hay cruce de horarios!")
                            time.sleep(1)
                    elif opc == 2:
                            clear()
                            print("Saliendo...")
                            time.sleep(2)
                            break
                    else:
                        print("Elegir una opcion valida!")
                elif elec == 3:
                    opc = int(input(f"Estas seguro que deseas asignar al salon apollo?: (1.Si/2.No): "))
                    if opc == 1:
                        if horario_trainer in data["salones"]["apollo"] and data["trainers"][documento]["nombre"] not in data["salones"]["kepler"][horario_trainer]["profesor"] and data["trainers"][documento]["nombre"] not in data["salones"]["sputnik"][horario_trainer]["profesor"]:
                           data["salones"]["apollo"][horario_trainer]["profesor"] = data["trainers"][documento]["nombre"]
                           data["trainers"][documento]["salon"] = "apollo"
                           guardar_datos(data)
                        else:
                            clear()
                            print("Hay cruce de horarios!")
                            time.sleep(1)
                    elif opc == 2:
                            clear()
                            print("Saliendo...")
                            time.sleep(2)
                            break
                    else:
                        print("Elige alguna de las opciones disponibles!")
                        continue
        elif opt == 2:
            print("Saliendo...")
            break
        else:
            print("Ingresa una opcion valida!")
            continue
      except ValueError:
          print("Error")
          
def asignar_campers():
    data = leer_datos()
    print("Bienvenido al sistema de asignacion de campers!")
    while True:
        try:
            elec = int(input("Deseas continuar? (1.Si/2.No): "))
            if elec == 1:
                for ruta in data["rutas"]:
                    print(f"-{ruta}")
                
        except ValueError:
            print("Ingrese un valor valido!")
            continue
            
def asignar_rutas():
    data = leer_datos()
    clear()
    while True:
        print("Sistema de asignacion de rutas y salones para trainers!")
        try:
            elec = int(input("Desea continuar? (1.Si/2.No): "))
            if elec == 1:
                documento = input("Ingresa el documento del trainer que vas a gestionar: ")
                if documento not in data["trainers"]:
                    print("Ese trainer no existe!")
                else:
                    while True: 
                        for ruta in data["rutas"]:
                            print(f"- {ruta}")
                        ruta = input("Escribe el nombre de la ruta a asignar: ")
                        if ruta not in data["rutas"]:
                            clear()
                            print("Escribiste incorrectamente el nombre de la ruta o ingresaste una ruta que no existe")
                        else:
                            if data["trainers"][documento]["ruta"]:
                                print("El trainer ya tiene una ruta asignada")
                                break
                            else:
                                data["trainers"][documento]["ruta"] = ruta
                                print("Ruta asignada exitosamente!")
                                guardar_datos(data)
                                break
            elif elec == 2:
                clear()
                print("Saliendo...")
                time.sleep(2)
                break
            else:
                print("Esa opcion no existe!")
                continue
        except ValueError:
            print("Favor ingresar un valor numerico!")
            continue

    
menu_principal()