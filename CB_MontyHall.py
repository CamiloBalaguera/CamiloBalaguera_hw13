import numpy as np
import matplotlib.pyplot as plt

resultados1 = []
resultados2 = []
contador1 = 0
contador2 = 0
n = 1000

def sort_doors():
	opciones = ["goat", "goat", "car"]
	np.random.shuffle(opciones)
	return opciones

def choose_door():
	return np.random.choice(3, 1)[0]

def reveal_door(lista, choice):
	for i in range(len(lista)):
		if i != choice:
			if lista[i] == "goat":
				lista[i] = "GOAT_MONTY"
				return lista

def finish_game(lista,choice,change):
	if change == False:
		return lista[choice]
	else:
		for i in range(len(lista)):
			if (i != choice) and (lista[i] != "GOAT_MONTY"):

				return lista[i]

for i in range(n):
	changes = True
	# Se realiza el juego cuando SI se cambia de decision
	choice1 = choose_door()
	resultados1.append(finish_game(reveal_door(sort_doors(), choice1), choice1, changes)) 

	changes = False
	# Se realiza el juego cuando NO se cambia de decision
	choice2 = choose_door()
	resultados2.append(finish_game(reveal_door(sort_doors(), choice2), choice2, changes))

for i in range(len(resultados1)):
	if resultados1[i] == "car":
		contador1 += 1
	if resultados2[i] == "car":
		contador2 += 1

probabilidad1 = contador1/n
probabilidad2 = contador2/n
print ("La probabilidad de ganar cuando NO se realiza el cambio de puerta es", probabilidad2, "\n", "La probabilidad de ganar cuando SI se realiza el cambio de puerta es", probabilidad1)
	
	
	
	
	
