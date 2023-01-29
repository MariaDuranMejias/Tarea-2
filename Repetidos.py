#Se debe generar una lista, en este caso, se creo una lista a partir de numero aleatorios del 1 al 10
#Si no es cero, se prosigue en la busqueda de elementos repetidos en la lista
#Para esto, se crea una segunda lista vacia
#Se genera una variable que recorra la lista que creamos al inicio, si el elemento no se encuentra en la lista vacia se copiara
#en esta lista, de lo contrario no se copiara, de esta forma no se copiaran elementos repetidos.
#Imprimir la nueva lista sin elementos repetidos


import random

a= random.randrange(1, 10)
b= random.randrange(1, 10)
c= random.randrange(1, 10)
d= random.randrange(1, 10)
e= random.randrange(1, 10)
f= random.randrange(1, 10)
g= random.randrange(1, 10)
h= random.randrange(1, 10)

mylist = [a, b, c, d, e, f, g, h]
print(mylist)

result = []
a = len(mylist)

if a>0:
    for item in mylist:
        if item not in result:
            result.append(item)
    print(result)

#Condicion de fallo
# bug_list = []
# b = len(bug_list)
# print(b)
# if b <=0:
#     print("Mensaje de error")