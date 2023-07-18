import json

#validar que lo que ingrese sea un numero entero
def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                print("\n!ERROR¡. El numero ingresado no puede ser cero ni menor a cero")
                input("Presione ENTER para continuar...")
                continue
            return n
        except ValueError:
            print("!OOPS¡. Ingresaste una letra, recuerda que solo son numeros enteros")

# Validar que lo que ingrese sea un String
def leerStr(msg):
    while True:
        try:
            nom = input(msg)
            if nom.isdigit() == True:
                print("\n!ERROR¡. Nombre no valido")
                input("Presione ENTER para continuar...")
                continue
            return nom
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")
            
            
# Validar que escoja M/F segun corresponda el sexo del alumno
def leerSexo(msg):
    while True:
        try:
            s = input(msg).upper()
            if s == "M" or s == "F":
                return s
            else:
                print("\n!ERROR¡. Opcion no valida")
                input("Presione ENTER para continuar...")
        except ValueError:
            print("\n!OOPS¡. Ubo un error inesperado en el programa")
            input("Presione ENTER para continuar...")
        

#  Validar si va a volver a repetir la ultima accion
def valiRepe(msg):
    while True:
        try:
            i = leerInt(msg)
            if i < 1 or i > 2:
                print("!ERROR¡. Ingrese una opcion valida")
                input("Presione ENTER para continuar...")                
                continue
            return i
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")
            input("Presione ENTER para continuar...")

            
# Menu del programa
def menu():
    print("\n\n******** BANCO ACME ********")
    print("Bienvenidos...")
    while True:
        print("1. Registrar nuevo")
        print("2. Asignacion de tarjeta")        
        print("3. Modificar de tarjeta")
        print("4. Eliminar tarjeta")
        print("5. Mostrar las tarjetas de un cliente")
        print("6. Mostrar informacion de la tarjeta")
        print("7. Listado de las tarjetas de credito")
        print("8. Listado de clientes con tarjeta")
        print("9. Cantidad de tarjetas")
        print("10. Salir")
        try:
            m = leerInt("Ingrese una opcion  ")
            if m < 1 or m > 10:
                print("!ERROR¡. Ingrese una opcion valida")
                input("Presione ENTER para continuar...")
                continue
            else:
                return m
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")
            input("Presione ENTER para continuar...")
            

def llenarDiccio(dic,nit,nom,sex,tel,tarje):
   
    dic[nit] = {}
    dic[nit]["nombre"] = nom
    dic[nit]["sexo"] = sex
    dic[nit]["telefono"] = tel
    dic[nit]["tarjeta"] = tarje
    
    return dic


            
def registrarCliente(clientes,ruta):
    while True:
        print("\nRegistro cliente nuevo")
        nom = leerStr("Ingrese el nombre del cliente:  ")
        cc = leerInt("Ingrese el numero de cedula del cliente:  ")
        sex = leerSexo("Ingrese el sexo del cliente (M/F):  ")
        tel = leerInt("Ingrese el numero telefonico del cliente:  ")
        tarje = 0
        
        clientes = llenarDiccio(clientes,cc,nom,sex,tel,tarje)
        
        with open(ruta,"w") as file:
            json.dump(clientes,file)
        print("Cliente agregado exitosamente\n")
        op = valiRepe("Deseas registrar otro cliente. \n  1. Si \n  2. No\n")
        if op == 2:
            break
   
   
   



def mostrarCliente(cc,clientes,tarjetas):
    print(f"Documento\t\t{cc}")
    print(f"Nombre   \t\t{clientes[cc]['nombre']}")
    for k in tarjetas[cc].keys():
        print(f"Tipo de tarjeta\t{tarjetas[cc][k]['tipo']}")
        print(f"Numero de tarjeta\t{k}")
        print(f"Vencimiento\t{tarjetas[cc][k]['vence']}")
        
        


def buscarCliente(clientes,tarjetas,mod=0):
    while True:
        print("\nbuscar cliente")
        cc = str(leerInt("Ingrese el numero de documento:  "))
        encontrado = False
        for k in clientes.keys():
            if cc == k:
                print("Cliente encontrado")
                encontrado = True
                if mod == 2:
                    return cc
                if mod == 0 and clientes[k]["tarjeta"] == 1:
                    mostrarCliente(cc,clientes,tarjetas)
                else:
                    print("El cliente no tiene tarjeta de credito asignada")
                    input("Presione ENTER para continuar...")
                    pass
        if encontrado == True:
            return cc        
        
    
def TipoTarjeta():
    print("\nTipo de tarjeta")
    print("1. Master Card")
    print("2. Visa")
    print("3. American express")
    t = leerInt("Escoje:  ")
    if t > 3:
        raise TypeError('Valor no valido')
    else:
        if t == 1:
            ti = "Master Card"
        elif t== 2 :
            ti ="Visa"
        else:
            ti="American Express"
    return ti
    
        
def fechaVenci():
    while True:
        print("\nFecha de vencimiento")
        mes = leerInt("Ingrese el mes:  ")
        año = leerInt("Ingrese el año:  ")
        print(f"Ingresaste mes {mes}  año {año} ")
        op = valiRepe("¿Estas seguro? \n  1. Si \n  2. No  ")
        if op == 1:
            mes = str(mes)
            año = str(año)
            fe = mes+"/"+año
            return fe


def codigoVerificacion():
    while True:
        try:
            ver = leerInt("Ingrese codigo de verificadion de 3 digitos ente (100-999):   ")
            if ver < 100 or ver > 999:
                print("\n!ERROR¡. El codigo no esta entre los rangos permitidos")
                input("Presione ENTER para continuar...")
                continue
            return ver
        except ValueError:
            print("!OOPS¡. Ubo un error inesperado en el programa")
            
            

def asignarTarjeta(clientes, ruta,tarjetas,ruta2):
    try:
        cc = buscarCliente(clientes,tarjetas,1)
    except ValueError:
        print("\nEl cliente tiene que estar registrado antes de asignarle una tarjeta")
        pass
    
    tipo = TipoTarjeta()
    num = leerInt ("Ingrese el numero de la tarjeta  ")
    venc = fechaVenci()
    veri = codigoVerificacion()
    print (clientes[cc]["tarjeta"])
        
    if clientes[cc]["tarjeta"] == 0:
        tarjetas[cc]={}
    tarjetas[cc][num] = {}
    tarjetas[cc][num]["tipo"] = tipo
    tarjetas[cc][num]["vence"] = venc
    tarjetas[cc][num]["verificacion"] = veri    
       
    clientes[cc]["tarjeta"] = 1
   
    with open(ruta,"w") as file:
            json.dump(tarjetas,file)
    with open(ruta2,"w") as file:
            json.dump(clientes,file)
    print("La tarjeta ha sido asignada con exito")
    input("Presione ENTER para continuar...")
    
    
    
def modificartarjeta(ruta,tarjetas,clientes):
    cc = buscarCliente(clientes,tarjetas,1)        
    for k in tarjetas[cc].keys():
         print(k)
    tar = str(leerInt("Ingrese el numero de la tarjeta que deseas modificar:  "))
    while True:
        print("¿Que deseas modificar? \n1. Tipo \n2. Codigo de verificacion \n3. Fecha de vencimiento ")
        op = leerInt("> ")
        if op == 1:
            nTipo = TipoTarjeta()
            tarjetas[cc][tar]["tipo"] = nTipo
            print("Cambio realizado con exito")
        elif op == 2:
            nCod = codigoVerificacion
            tarjetas[cc][tar]["verificacion"] = nCod
            print("Cambio realizado con exito")
        elif op == 3:
            nFech = fechaVenci()
            tarjetas[cc][tar]["vence"] = nFech
            print("Cambio realizado con exito")
        else:
            print("!ERROR¡. No es una opcion valida")
            continue
        with open(ruta,"w") as file:
            json.dump(tarjetas,file)
        en = valiRepe("Deseas modificar algo mas \n 1. Si \n 2. No\n")
        if en == 2:
            break
        
        
def eliminarTarjeta(ruta,tarjetas,clientes):
    cc = buscarCliente(clientes,tarjetas,1)
    tar = str(leerInt("Ingrese el numero de la tarjeta que deseas eliminar:  "))
    tarjetas[cc].pop(tar)
    print("Cliente eliminado con exito")
    input("Presione ENTER para continuar...")
    
    with open(ruta,"w") as file:
        json.dump(tarjetas,file)        
    

def buscarTarjeta(tarjetas):
    while True:
        encon = False
        t = str(leerInt("Ingrese el numero de la tarjeta:  "))
        for k in tarjetas.keys():
            for x in tarjetas[k].keys():
                if t == x:
                    return t, k
        
        if encon == False:
            print("!OOPS¡. La tarjeta no fue encontrada")
            input("Presione ENTER para continuar...")
         
def mostarTarjeta(clientes, tarjetas):
    num, cc = buscarTarjeta(tarjetas)
    print("Datos de la tarjeta")
    print(f"numero de tarjeta\t\t\t{num}")
    print(f"Tipo de tarjeta\t\t\t{tarjetas[cc][num]['tipo']}")
    print(f"Fecha de vencimiento\t\t{tarjetas[cc][num]['vence']}") 
    print(f"Codigo de verificacion\t\t{tarjetas[cc][num]['verificacion']}")
    print(f"Nombre del propietario\t\t{clientes[cc]['nombre']}")
    print(f"cedula\t\t\t\t{cc}")
    print(f"Numero telefonico\t\t{clientes[cc]['telefono']}")
    print(f"Sexo\t\t\t\t{clientes[cc]['sexo']}")
    input("Presione ENTER para continuar...")
    
    
def listadoTarjetas(clientes,tarjetas):
    print("\nListado de las tarjetas de credito")
    print("Numero tarjeta\t\tFecha vencimiento\t\tTipo\t\t\tDocumento\t\tNombre")
    for k in tarjetas.keys():
            for x in tarjetas[k].keys():
                print(f"{x}\t\t\t\t{tarjetas[k][x]['vence']}\t\t\t{tarjetas[k][x]['tipo']}\t{k}\t\t{clientes[k]['nombre']}")
    
    input("Presione ENTER para continuar...")
                
  
def clientesTarjeta(clientes):
    print("\nClientes que tienen tarjeta de credito")
    print("Cedula\t\tNombre\t\tTelefono")
    for k in clientes.keys():
        if clientes[k]["tarjeta"] == 1:
            print(f"{k}\t{clientes[k]['nombre']}\t\t{clientes[k]['telefono']}")
    input("Presione ENTER para continuar...")
            
def cantidadTarjetas(tarjetas):
    count = [0,0,0]
    for k in tarjetas.keys():
        for x in tarjetas[k].keys():
            print(tarjetas[k][x]["tipo"])
            if tarjetas[k][x]["tipo"] == "Master Card":
                count[0] += 1
            elif tarjetas[k][x]["tipo"] == "Visa":
                count[1] += 1
            elif tarjetas[k][x]["tipo"] == "American Express":
                count[2] += 1
                
    print("\nEn este momento en el mercado hay:")
    print(f"Master Card\t\t\t{count[0]}")
    print(f"Visa\t\t\t\t{count[1]}")
    print(f"American Express\t\t{count[2]}")
    input("Presione ENTER para continuar...")
        

def cargarInfo(ruta):
    with open ( ruta,"a+") as file:
        file.seek(0)
        # Verificar datos
        try:
            dic = json.load(file)
        except Exception as e:
            dic ={}
        return dic
    
               
def main():
    ruta1 = "reto1/bancoAcneClientes.json"
    ruta2 = "reto1/bancoAcneTarjetas.json"
        
    
    while True:
        clientes = cargarInfo(ruta1)
        tarjetas = cargarInfo(ruta2)
        op = menu()
        
        if op == 1:
            registrarCliente(clientes,ruta1)
        elif op == 2:
            asignarTarjeta(clientes, ruta2,tarjetas,ruta1)
        elif op == 3:
            modificartarjeta(ruta2,tarjetas,clientes)
        elif op == 4:
            eliminarTarjeta(ruta2,tarjetas,clientes)
        elif op == 5:
            buscarCliente(clientes,tarjetas)
            input("Presione ENTER para continuar...")
        elif op == 6:
            mostarTarjeta(clientes, tarjetas)
        elif op == 7:
            listadoTarjetas(clientes,tarjetas)
        elif op == 8:
            clientesTarjeta(clientes)
        elif op == 9:
            cantidadTarjetas(tarjetas)
        else:
            break
        
        
main()