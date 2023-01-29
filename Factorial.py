#Pedirle al usuario que ingrese un numero
#Debemos convertir este input un int
#Ponemos un condicional por si el numero es menor o igual a cero, si lo es, poner un mensaje de error 
#Debemos hacer una variable que recorra todos los numeros hasta llegar al que el usuario ingreso
#Guardar en una variable el resultado de cada iteracion, que se vayan multiplicando por el nuevo resultado
#Imprimir la variable con el resultado del factorial
N = input('Ingrese numero \n')
num = int(N)
if num <= 0:
    print("Mensaje de error")
i=0
y=1
for i in range(1,num+1):
    y = y*i
print(y)
