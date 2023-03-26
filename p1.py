 
 

ciclistas=[] 

rtiempos=[1250,1580,2792] 

 
 

registro=0 

while registro !=5: 

     

    print ("******************MENÚ DE OPCIONES*****************") 

    print("1. Registrar de ciliclista ") 

    print("2. Ver tabla de posiciones ") 

    print("3. Modificar tiempo registrado ") 

    print("4. Borrar tiempo registrado ") 

    print("5. Salir ") 

    registro = int(input()) 

    if registro ==1: 

        print("Registrar ****") 

        nombre =(input("Ingresa el nombre del ciclista: ")) 

        ciclistas.append(nombre) 

        Edad =(int (input("Edad del ciclista: "))) 

        ciclistas.append(Edad) 

        Pais =(input("Pais del ciclista: ")) 

        ciclistas.append(Pais) 

        Equipo = (input("Equipo: " )) 

        ciclistas.append(Equipo) 

        tiempo = (int (input("Digite el tiempo registrado en la prueba individual: minutos "))) 

        tiempo+=1 

        rtiempos.sort() 

        rtiempos.append(tiempo) 

        print(f"Tiempo registrado de forma exitosa:{ciclistas}") 

    if registro ==2: 

        print(f"La tabla de posiciones es:  {rtiempos}") 

    elif registro ==3: 

        print(len(rtiempos)) 

        print ("Ingrese el indice a modificar") 

        i=int (input()) 

        print ("ingrese un nuevo valor") 

        val = input() 

        rtiempos[i] = val 

        print(rtiempos) 

    elif registro ==4: 

        print(len(rtiempos)) 

        print ("Ingrese el indice a borrar") 

        i=int (input()) 

        del rtiempos [i] 

        print(rtiempos) 

    elif registro ==5: 

        exit() 

    else: 

     print("opcion invalida") 

 