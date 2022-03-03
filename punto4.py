'''Un alumno desea saber cuál será su calificación final en la materia de
fundamentos de programación. Dicha calificación se compone de los
siguientes porcentajes: 50% del promedio de sus tres talleres, 30% de la
calificación de un examen en clase y 20% de la calificación de un proyecto
final.'''


taller1 = float(input("calificacion taller 1: "))
taller2 = float(input("calificacion taller 2: "))
taller3 = float(input("calificacion taller 3: "))
examenClase = float(input("calificacion examen en clase: "))
proyectofinal = float(input("calificacion proyectofinal: "))

totaltaller = ((taller1+taller2+taller3)/3)*0.50

totalexamen = examenClase*0.30
totalproyecto = proyectofinal*0.20

calificacionTotal = +totalexamen+totaltaller+totaltaller

print("Calificacion talleres del estudiante: ",totaltaller)
print("Calificacion Examen en clase del estudiante: ",totalexamen)
print("Calificacion total del proyecto del estudiante: ",totalproyecto)

print("Calificacion final del estudiante: ",calificacionTotal)

