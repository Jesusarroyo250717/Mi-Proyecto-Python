

num1= float(input("Ingrese el primer número: "))
num2= float(input("Ingrese el segundo número: "))

suma=num1+num2
resta=num1-num2
multiplicación=num1*num2
division= num1/num2 if num2 !=0 else "No se puede devidir entre cero"
division_Entera= num1//num2 if num2 !=0 else "No se puede devidir entre cero"
residuo= num1%num2 if num2 !=0 else "No se puede Calcular el residuo entre cero"

print(f"La suma es: ",suma)
print(f"La resta es: ",resta)
print(f"La multiplicacion es: ",multiplicación)
print(f"La division es: ",division)
print(f"La division entera es: ",division_Entera)
print(f"El residuo es: ",residuo)

