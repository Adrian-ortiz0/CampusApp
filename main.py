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
            print("4. Asignar campers a rutas y trainers")
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
        while True:   
            print(f"Bienvenido al menu trainer {data['trainers'][identificacion]['nombre']}!")
            print("******************************************")
            print("1. Ver estudiantes")
            print("2. Probar estudiantes")
            print("3. Salir")
            try:
                opt = int(input("Ingresa una opcion: "))
                if opt == 1:
                    ver_estudiantes(identificacion)
                elif opt == 2:
                    probar_estudiantes(identificacion)
                elif opt == 3:
                    print("Saliendo...")
                    break
                else:
                    print("Opcion no valida!")
                    continue
            except ValueError:
                print("Valor no valido!")
                continue
    else:
        print("No existe ese documento!")

def menu_principal():
    data = leer_datos()
    while True:
        print("#    ####                                                  ## #")
        print("#   ##  ##                                                #### #")
        print("#  ##        ####    ##  ##   ######   ##  ##    #####   ##  ##   ######   ###### #")
        print("#  ##           ##   #######   ##  ##  ##  ##   ##       ##  ##    ##  ##   ##  ## #")
        print("#  ##        #####   ## # ##   ##  ##  ##  ##    #####   ######    ##  ##   ##  ## #")
        print("#   ##  ##  ##  ##   ##   ##   #####   ##  ##        ##  ##  ##    #####    ##### #")
        print("#    ####    #####   ##   ##   ##       ######  ######   ##  ##    ##       ## #")
        print("#                             ####                                ####     #### #")
        print("")
        print("************************************************************************************")
        print("1. Incribirse")
        print("")
        print("2. Ingresar como usuario")
        print("")
        print("3. Ingresar como administrador")
        print("")
        print("4. Ingresar como trainer")
        print("")
        print("5. Salir")
        print("")
        
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
    print("¡Bienvenido al sistema de asignación de campers!")
    while True:
        try:
            elec = int(input("¿Deseas continuar? (1.Si/2.No): "))
            if elec == 1:
                documento = input("Ingrese el documento del camper: ")
                if documento in data["estudiantes"] and data["estudiantes"][documento]["estado"] == "Aprobado":
                    for ruta in data["rutas"]:
                        print(f"- {ruta}")
                    ruta_elegida = input("Ingrese el nombre exacto de la ruta que desea asignar: ")
                    if ruta_elegida in data["rutas"]:
                        data["estudiantes"][documento]["ruta"] = ruta_elegida
                        print("Ruta asignada!")
                        guardar_datos(data)
                        for trainer in data["trainers"]["ruta_trainers"][ruta_elegida]:
                            for trainer_name in trainer:
                                print(f"- {trainer_name}")
                        trainer_elegido = input("Escribe el nombre del trainer que recibirá el camper: ")
                        trainer_encontrado = False
                        for trainer in data["trainers"]["ruta_trainers"][ruta_elegida]:
                            if trainer_elegido in trainer:
                                trainer[trainer_elegido].append({
                                    "id": documento,
                                    "nombre": data["estudiantes"][documento]["nombre"]
                                })
                                data["estudiantes"][documento]["trainer"] = trainer_elegido
                                data["estudiantes"][documento]["estado"] = "Cursando"
                                trainer_encontrado = True
                                clear()
                                print("Trainer asignado!")
                                time.sleep(2)
                                guardar_datos(data)
                                break
                        if not trainer_encontrado:
                            print("Escribiste mal el nombre del trainer o el trainer no existe!")
                            continue
                    else:
                        print("¡Esa ruta no existe!")
                else:
                    clear()
                    print("¡Ese camper no existe o no está aprobado!")
                    time.sleep(1)
                    continue
            elif elec == 2:
                clear()
                print("Saliendo...")
                time.sleep(2)
                break
            else:
                print("¡Elige una opción válida!")
        except ValueError:
            print("¡Ingrese un valor válido!")
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
                        nombre_trainer = data["trainers"][documento]["nombre"] 
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
                                trainer_elegido = {
                                    nombre_trainer : []
                                }
                                data["trainers"][documento]["ruta"] = ruta
                                data["trainers"]["ruta_trainers"][ruta].append(trainer_elegido)
                                clear() 
                                print("Ruta asignada exitosamente!")
                                time.sleep(1)
                                wait_for_keypress()
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
        
def ver_estudiantes(identificacion):
    data = leer_datos()
    while True:   
        try:
            trainer_info = data['trainers'].get(identificacion)
            if not trainer_info:
                print("¡Identificación del entrenador no encontrada!")
                break          
            print(f"Bienvenido trainer {trainer_info['nombre']}!")
            elec = int(input("¿Desea ver sus estudiantes? (1.Si/2.No)?: "))
            if elec == 1:
                ruta = trainer_info["ruta"]
                nombre_trainer = trainer_info["nombre"]         
                for trainer in data["trainers"]["ruta_trainers"][ruta]:
                    if nombre_trainer in trainer:
                        estudiantes = trainer[nombre_trainer]
                        if estudiantes:
                            for estudiante in estudiantes:
                                print(f"- ID: {estudiante['id']}, Nombre: {estudiante['nombre']}")
                        else:
                            print("No hay estudiantes asignados.")
                        break          
            elif elec == 2:
                clear()
                print("Saliendo...")
                time.sleep(2)
                break
            
            else:
                print("¡Elige una opción válida!")
        
        except ValueError:
            print("¡Ingrese un valor válido!")
            continue

def probar_estudiantes(identificacion):
    clear()
    data = leer_datos()
    while True:
        try:
            trainer_info = data['trainers'].get(identificacion)
            if not trainer_info:
                print("El identificador del trainer no es válido!")
                break
                
            print(f"Bienvenido trainer {trainer_info['nombre']}!")
            elec = int(input("Desea continuar? (1.Si/2.No)?: "))
            if elec == 1:
                print("1. Introduccion a la programacion")
                print("2. Python")
                print("3. Scrum y Git")
                print("4. Javascript")
                print("5. MySql")
                print("6. MongoDb")
                print("7. Backend")
                print(f"8. {trainer_info['ruta']}")
                modulo = int(input("En que modulo desea evaluar a sus estudiantes: "))
                ruta = trainer_info["ruta"]
                nombre_trainer = trainer_info["nombre"]
                
                for trainer in data["trainers"]["ruta_trainers"][ruta]:
                    if nombre_trainer in trainer:
                        estudiantes = trainer[nombre_trainer]
                        if estudiantes:
                            for estudiante in estudiantes:
                                print(f"- ID: {estudiante['id']}, Nombre: {estudiante['nombre']}")
                        else:
                            print("No hay estudiantes asignados.")
                        break
                
                estudiante = input("Ingrese el documento de identidad del estudiante a evaluar: ")
                
                if estudiante not in data["estudiantes"]:
                    print("El estudiante no existe!")
                    continue

                estudiante_modulos = data["estudiantes"][estudiante].get("modulo", {})

                if modulo == 1:
                    nota_int_taller = int(input("Ingrese la nota de taller: "))
                    nota_int_filtro = int(input("Ingrese la nota de filtro: "))
                    nota_int_final = (nota_int_taller * 0.60 + nota_int_filtro * 0.40)
                    estudiante_modulos["introduccion a la programacion"] = {
                        "taller" : nota_int_taller,
                        "filtro" : nota_int_filtro,
                        "final" : nota_int_final  
                    }
                
                elif modulo == 2 and "introduccion a la programacion" in estudiante_modulos:
                    nota_py_taller = int(input("Ingrese la nota de taller: "))
                    nota_py_filtro = int(input("Ingrese la nota de filtro: "))
                    nota_py_final = (nota_py_taller * 0.60 + nota_py_filtro * 0.40)
                    estudiante_modulos["python"] = {
                        "taller" : nota_py_taller,
                        "filtro" : nota_py_filtro,
                        "final" : nota_py_final  
                    }
                
                elif modulo == 3 and "python" in estudiante_modulos:
                    nota_sg_taller = int(input("Ingrese la nota de taller: "))
                    nota_sg_filtro = int(input("Ingrese la nota de filtro: "))
                    nota_sg_final = (nota_sg_taller * 0.60 + nota_sg_filtro * 0.40)
                    estudiante_modulos["scrum_git"] = {
                        "taller" : nota_sg_taller,
                        "filtro" : nota_sg_filtro,
                        "final" : nota_sg_final  
                    }
                
                elif modulo == 4 and "scrum_git" in estudiante_modulos:
                    nota_js_taller = int(input("Ingrese la nota de taller: "))
                    nota_js_filtro = int(input("Ingrese la nota de filtro: "))
                    nota_js_final = (nota_js_taller * 0.60 + nota_js_filtro * 0.40)
                    estudiante_modulos["javascript"] = {
                        "taller" : nota_js_taller,
                        "filtro" : nota_js_filtro,
                        "final" : nota_js_final  
                    }
                
                elif modulo == 5 and "javascript" in estudiante_modulos:
                    nota_sql_taller = int(input("Ingrese la nota de taller: "))
                    nota_sql_filtro = int(input("Ingrese la nota de filtro: "))
                    nota_sql_final = (nota_sql_taller * 0.60 + nota_sql_filtro * 0.40)
                    estudiante_modulos["mysql"] = {
                        "taller" : nota_sql_taller,
                        "filtro" : nota_sql_filtro,
                        "final" : nota_sql_final  
                    }
                
                elif modulo == 6 and "mysql" in estudiante_modulos:
                    nota_db_taller = int(input("Ingrese la nota de taller: "))
                    nota_db_filtro = int(input("Ingrese la nota de filtro: "))
                    nota_db_final = (nota_db_taller * 0.60 + nota_db_filtro * 0.40)
                    estudiante_modulos["mongodb"] = {
                        "taller" : nota_db_taller,
                        "filtro" : nota_db_filtro,
                        "final" : nota_db_final  
                    }
                
                elif modulo == 7 and "mongodb" in estudiante_modulos:
                    nota_back_taller = int(input("Ingrese la nota de taller: "))
                    nota_back_filtro = int(input("Ingrese la nota de filtro: "))
                    nota_back_final = (nota_back_taller * 0.60 + nota_back_filtro * 0.40)
                    estudiante_modulos["backend"] = {
                        "taller" : nota_back_taller,
                        "filtro" : nota_back_filtro,
                        "final" : nota_back_final  
                    }
                
                elif modulo == 8 and "backend" in estudiante_modulos:
                    nota_core_taller = int(input("Ingrese la nota de taller: "))
                    nota_core_filtro = int(input("Ingrese la nota de filtro: "))
                    nota_core_final = (nota_core_taller * 0.60 + nota_core_filtro * 0.40)
                    estudiante_modulos[trainer_info['ruta']] = {
                        "taller" : nota_core_taller,
                        "filtro" : nota_core_filtro,
                        "final" : nota_core_final  
                    }
                
                else:
                    clear()
                    print("El estudiante no ha aprobado el módulo anterior o el módulo no es válido!")
                    time.sleep(2)
                    continue
                
                data["estudiantes"][estudiante]["modulo"] = estudiante_modulos
                guardar_datos(data)
                clear()
                print("Notas guardadas con éxito")
                
            elif elec == 2:
                clear()
                print("Saliendo...")
                time.sleep(2)
                break
                
        except ValueError:
            print("Ingresa un valor válido!")
            continue
menu_principal()