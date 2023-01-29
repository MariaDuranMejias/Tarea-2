#Se define el diccionario que se suministro
sampleDict = {
    "class": {
        "student": {
            "name": "",
            "marks": {
                "physics": 70,
                "history": 80,
                "math": 90
                },
            }
        }
    }

#Se cambia el diccionario de notas por el promedio de las notas del estudiante
sampleDict["marks"] = int((70+80+90)/3)
#Se rellene rellena el diccionario de nombre con el nombre del estudiante
sampleDict["name"] = "Mike"

#Se definen como variables el nombre y el promedio
a = sampleDict["name"]
b = sampleDict["marks"]
#Se imprime las variables como un resultado
print("{",a,":",b,"}")

