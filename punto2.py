'''Haga un programa en Python que permita ingresar el dinero invertido por
tres personas para formar una empresa. Cada una de ellas invierte una
cantidad distinta. Imprimir el porcentaje que cada quien invierte con respecto
al total de la inversión.'''

inversion1 = int(print("Digite la primera inversion: "))
inversion2 = int(print("Digite la segunda inversion: "))
inversion3 = int(print("Digite la tercera inversion: "))

totalInversion= inversion1+inversion2+inversion3

totalInversion1 = totalInversion /inversion1
totalInversion2 = totalInversion /inversion2
totalInversion3 = totalInversion /inversion3