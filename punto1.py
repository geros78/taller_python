'''Una Institución educativa ha recibido una donación especial que será
repartida entre las carreras de Telecomunicaciones, Sistemas,
Administración y Contabilidad de la siguiente forma:
a. Telecomunicaciones 10% del valor dado a sistemas
b. Sistemas: 25% del valor dado a Administración
c. Administración: 35% del valor de la donación
d. Contabilidad: lo que resta de la donación'''

donacion = int(input("Ingrese la cantidad donada: "))

telecomunicaciones = donacion*0.10
sistemas = donacion*0.25
administracion = donacion*0.35
contabilidad = donacion*0.30

print("La cantidad donada a telecomunicaciones es: ",telecomunicaciones)
print("La cantidad donada a sistemas es: ",sistemas)
print("La cantidad donada a administracion es: ",administracion)
print("La cantidad donada a contabilidad es: ",contabilidad)

