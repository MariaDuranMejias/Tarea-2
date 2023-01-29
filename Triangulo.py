#Pedirle al usuario que ingrese un numero
#Convertir ese numero en un int
#Ingresar la condicion de fallo que seria si ese numero es igual a cero
#Lo primero que hay que hacer es imprimir todos los numeros hasta el que ingreso el usuario, ej: 
#1
#2
#3
#Poner cada iteracion de i en una linea diferente
#Despues se necesitamos imprimir todos los numeros antes del numero en el que este la iteracion anterior, ej:
#1
#1
#2
#1
#2
#3
#Como se imprimen hacia abajo, se deben poner en la misma fila, eliminando el salto de linea
#1
#12
#123
#Debemos poner un espacio entre cada digito

N = input('Ingrese numero \n')
num = int(N)
if num <= 0:
    print("Mensaje de error")

i=0
j=0
for i in range(1,num+1):
    print("")
    for j in range(1,i+1):
        print(j, end=" ")