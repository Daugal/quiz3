num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


listaPares = num[1::2]
listaImpares = num[0::2]

print(listaPares)

print(listaImpares)

##############################


mascotas = ["Mico", "Noa", "Chispa", "Nina", "Rayo", "Toby", "Chiqui", "Rocky", "Plutón",
           "Thor", "Chico", "Simba", "Luna", "Bruno", "Lola", "Nico", "Coco", "Bimba", "Linda", "Max"]

primero, segundo, tercero, *otros , antepenultimo, penultimo, ultimo = mascotas

print(primero, segundo, tercero, antepenultimo, penultimo, ultimo)



#######################################

mascotas = ["Bruno", "Noa", "Chispa", "Nina", "Rayo", "Bruno", "Noa", "Rocky", "Plutón",
           "Thor", "Chico", "Noa", "Luna", "Bruno", "Lola", "Nico", "Coco", "Noa", "Linda", "Max"]


while mascotas.count("Noa") > 0:
    mascotas.remove("Noa")

print("Lista 2 sin Noa:", mascotas)
