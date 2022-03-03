'''Dada la cantidad de alumnos de Redes, contabilidad y diseño determine el
porcentaje de alumnos de cada uno de los cursos.'''

redes = int(input("cantidad estudiantes redes: "))
diseño = int(input("cantidad estudiantes diseño: "))
contabilidad = int(input("cantidad estudiantes contabilidad: "))

totalEstudiantes= redes+diseño+contabilidad

totalporcentaje1 = (redes/totalEstudiantes)*100
totalporcentaje2 = (diseño/totalEstudiantes)*100
totalporcentaje3 = (contabilidad/totalEstudiantes)*100

print("La inversion total de estudiantes es: ",totalEstudiantes)

print("Porcentaje estudiantes de redes: ",totalporcentaje1)
print("Porcentaje estudiantes diseño: ",totalporcentaje2)
print("Porcentaje estudiantes contabilidad ",totalporcentaje3)