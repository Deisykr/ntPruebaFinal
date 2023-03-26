#pedir 20 numeros y validar multiplos de 2, de 3 y cuantos son multiplos de 2 y 3 al mismos tiempo 

 
 

def generar_multiplos (numero, n): 

  return [numero * i for i in range (1,n + 1)] 

 
 
 

print(generar_multiplos(2,20)) 

print(generar_multiplos(3,20)) 

 
 

#if generar_multiplos % 2 == 0 and generar_multiplos % 3 == 0: 

#print ("Es multiplo de 2 y 3") 

 