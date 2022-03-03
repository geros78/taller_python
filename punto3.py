'''Un vendedor recibe un sueldo base más un 15% extra por comisión de sus
ventas efectuadas en el mes. El vendedor desea saber cuanto dinero en
total obtendrá por las ventas que realiza en el mes. Desarrolle un programa
en Python que permita mostrar el valor ganado por comisión y el valor total
a pagar al vendedor.'''

sueldo = int(input("Ingrese la cantidad donada: "))

sueldoComicion = sueldo *0.15
totalSueldo = sueldo+sueldoComicion

print("total del sueldo: ",sueldo)
print("total de comicion: ",sueldoComicion)
print("Total del suelto mas la comicion: ",totalSueldo)

