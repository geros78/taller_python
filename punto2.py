'''Haga un programa en Python que permita ingresar el dinero invertido por
tres personas para formar una empresa. Cada una de ellas invierte una
cantidad distinta. Imprimir el porcentaje que cada quien invierte con respecto
al total de la inversión.'''

inversion1 = float(print("Digite la primera inversion: "))
inversion2 = float(print("Digite la segunda inversion: "))
inversion3 = float(print("Digite la tercera inversion: "))

totalInversion= inversion1+inversion2+inversion3

totalporcentaje1 = totalInversion /inversion1
totalporcentaje2 = totalInversion /inversion2
totalporcentaje3 = totalInversion /inversion3

print("La inversion total es: ",totalporcentaje1)

print("porcentaje inversion 1: ",totalporcentaje1)
print("porcentaje inversion 2: ",totalporcentaje2)
print("porcentaje inversion 3: ",totalporcentaje3)