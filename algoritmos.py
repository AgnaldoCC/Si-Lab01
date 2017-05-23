def maximo(lista):
	maior = lista[0]
	for i in range(len(lista)):
		if lista[i] > maior:
			maior = lista[i]
	return maior


def minimo(lista):
	menor = lista[0]
	for i in range(len(lista)):
		if lista[i] < menor:
			menor = lista[i]
	return menor
