'''Haga un programa en Python que permita ingresar el dinero invertido por
tres personas para formar una empresa. Cada una de ellas invierte una
cantidad distinta. Imprimir el porcentaje que cada quien invierte con respecto
al total de la inversión.'''

inversion1 = int(input("Digite la primera inversion: "))
inversion2 = int(input("Digite la segunda inversion: "))
inversion3 = int(input("Digite la tercera inversion: "))

totalInversion= inversion1+inversion2+inversion3

totalporcentaje1 = (inversion1/totalInversion)*100
totalporcentaje2 = (inversion2/totalInversion)*100
totalporcentaje3 = (inversion3/totalInversion)*100

print("La inversion total es: ",totalInversion)

print("Porcentaje inversion 1: ",totalporcentaje1)
print("Porcentaje inversion 2: ",totalporcentaje2)
print("Porcentaje inversion 3: ",totalporcentaje3)