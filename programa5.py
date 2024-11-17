#Escribe un programa que tome una calificación numérica de un estudiante (entre 0 y 100) y le asigne una letra según la siguiente tabla:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Menos de 60: F

calificacion= int(input("Ingrese la calificacion del alumno: "))

if 90<= calificacion <=100:
    print("A")
elif 80 <= calificacion <89:
    print("B")
elif 70 <= calificacion <79:
    print("C")
elif 60 <= calificacion <69:
    print("D")
elif 0<= calificacion <60:
    print("F")
    
else:
    print("Nota Invalida")
    
     