Saldodecuentas=[] 

cantidad=(input) 

Saldodecuentas.sort() 

 
 

contador=0 

while contador !=2: 

    print("******Bienvenida al Banco de Hierro de las Islas Bravas*****\n\ 

    Cuentas de la Reina Lannister\n\ 

        1. Ingresar saldo a mis cuentas\n\ 

        2. salir") 

    contador = int(input()) 

     

    if contador ==1: 

         

        print ("Ingresar saldo en la cuenta #001: ") 

        cantidad=input() 

        Saldodecuentas.append(cantidad) 

         

         

        print ("Ingresar saldo en la cuenta #002: ") 

        cantidad=input() 

        Saldodecuentas.append(cantidad) 

         

        

        print ("Ingresar saldo en la cuenta #003: ") 

        cantidad=input() 

        Saldodecuentas.append(cantidad) 

         

         

        print ("Ingresar saldo en la cuenta #004:") 

        cantidad=input() 

        Saldodecuentas.append(cantidad) 

         

         

        print ("Ingresar saldo en la cuenta #005: ") 

        cantidad=input() 

        Saldodecuentas.append(cantidad) 

         

         

        print ("Ingresar saldo en la cuenta #006: ") 

        cantidad=input() 

        Saldodecuentas.append(cantidad) 

         

         

        print ("Ingresar saldo en la cuenta #007:") 

        cantidad=input() 

        Saldodecuentas.append(cantidad) 

         

         

        print ("Ingresar saldo en la cuenta #008: ") 

        cantidad=input() 

        Saldodecuentas.append(cantidad) 

         

         

        print ("Ingresar saldo en la cuenta #009: ") 

        cantidad=input() 

        Saldodecuentas.append(cantidad) 

         

         

        print ("Ingresar saldo en la cuenta #010: ") 

        cantidad=input() 

        Saldodecuentas.append(cantidad) 

        #sort 

        Saldodecuentas.sort() 

        Saldodecuentas.append(cantidad) 

         

        print(Saldodecuentas) 

        print("El saldo de la Reina es:********") 

        print("******************************************") 

         

        #for i in range (len(Saldodecuentas)): 

            #print(Saldodecuentas[i]) 

         

         

        print(f"El saldo de tu cuenta #001 es:" + Saldodecuentas[0]) 

        print(f"El saldo de tu cuenta #002 es:"+ Saldodecuentas[1]) 

        print(f"El saldo de tu cuenta #003 es:"+ Saldodecuentas[2]) 

        print(f"El saldo de tu cuenta #004 es:"+ Saldodecuentas[3]) 

        print(f"El saldo de tu cuenta #005 es:"+ Saldodecuentas[4]) 

        print(f"El saldo de tu cuenta #006 es:"+ Saldodecuentas[5]) 

        print(f"El saldo de tu cuenta #007 es:"+ Saldodecuentas[6]) 

        print(f"El saldo de tu cuenta #008 es:"+ Saldodecuentas[7]) 

        print(f"El saldo de tu cuenta #009 es:"+ Saldodecuentas[8]) 

        print(f"El saldo de tu cuenta #010 es:"+ Saldodecuentas[9]) 

         

         

    elif contador ==2: 

        print("Vuelva pronto") 

        exit() 

     

 

 