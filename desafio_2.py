#Vamos a practicar el uso de varios tipos de variables y la función input a través de algunas actividades.
#  Resuelve los problemas propuestos en código.

#Recopilación y muestra de datos

# - Crea un programa que solicite al usuario que escriba su nombre y luego imprima "Hola, [nombre]."
usuario_nom= input("Ingresa tu nombre")
print(f"Hola, {usuario_nom}")

#2 - Crea un programa que solicite al usuario que escriba su nombre y edad, y luego imprima 
# "Hola, [nombre], tienes [edad] años."
usuario_nom= input("Ingresa tu nombre")
usuario_edad= input("Ingresa tu edad:")
print(f"Hola,{usuario_nom} tienes {usuario_edad} años")

#3 - Crea un programa que solicite al usuario que escriba su nombre, edad y altura en metros, y luego imprima "Hola, [nombre], tienes [edad] años y mides [altura] metros."
usuario_nom= input("Ingresa tu nombre")
usuario_edad= input("Ingresa tu edad:")
usuario_alt= input("Ingresa tu altura en metros:")
print(f"Hola,{usuario_nom} tienes {usuario_edad} años y mides {usuario_alt} metros")
#Calculadora con operadores

#4 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la suma de ambos valores.
print("Ingresa dos valores númericos" )
valor1= int (input("Ingresa el primer valor:") )
valor2= int (input("Ingresa el segundo valor:"))
print(" El resultado de la  suma es de", valor1 + valor2)


#5 - Crea un programa que solicite tres valores numéricos al usuario y luego imprima la suma de los tres valores.
print("Ingresa tres valores númericos" )
valor1= int (input("Ingresa el primer valor:") )
valor2= int (input("Ingresa el segundo valor:"))
valor3= int (input("Ingresa el tercer valor:"))
print(" El resultado de la  suma es de", valor1 + valor2 + valor3)

#6 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la resta del primero menos el segundo valor.
print("Ingresa dos valores númericos" )
valor1= int (input("Ingresa el primer valor:") )
valor2= int (input("Ingresa el segundo valor:"))
print("El resultado del primer valor menos el segundo es de:", valor1 - valor2)

#7 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la multiplicación de los dos valores.
print("Ingresa dos valores númericos" )
valor1= int (input("Ingresa el primer valor:") )
valor2= int (input("Ingresa el segundo valor:"))
print(" El resultado de la multiplicación de los dos valores es de", valor1 * valor2)

#8 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador, y realice la división entre los dos valores.
#  Asegúrate de que el valor del denominador no sea igual a 0.
print("Ingresa dos valores númericos (numerador y denominador)" )
numerador= int (input("Ingresa el numerador:") )
denominador= int (input("Ingresa el denominador:"))
print(" El resultado de la división es de", numerador/denominador)
#9 - Crea un programa que solicite dos valores numéricos, un operador y una potencia, y realice la exponenciación entre estos dos valores.
print("Ingresa dos valores númericos (operador y potencia)" )
operador= int (input("Ingresa el operador:") )
potencia= int (input("Ingresa la potencia:"))
print(" El resultado de la exponenciación es de", operador**potencia)

#10 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador, y realice la división 
# entera entre los dos valores. Asegúrate de que el valor del denominador no sea igual a 0.
print("Ingresa dos valores númericos (numerador y denominador)" )
numerador= int (input("Ingresa el numerador:") )
denominador= int (input("Ingresa el denominador (no debe ser 0):"))
print(" El resultado de la división es de", numerador//denominador)

#11 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador,
#  y devuelva el resto de la división entre los dos valores. Asegúrate de que el valor del denominador no sea igual a 0.
print("Ingresa dos valores númericos (numerador y denominador)" )
numerador= int (input("Ingresa el numerador :") )
denominador= int (input("Ingresa el denominador (no debe ser 0):")) 
print(" El resultado de la división es de", numerador%denominador)
#12 - Crea un código que solicite las 3 notas de un estudiante e imprima el promedio de las notas.
nota1= int (input("Ingresa la nota 1 :") )
nota2= int (input("Ingresa la nota2:")) 
nota3= int (input("Ingresa la nota 3:")) 
print(" El promedio es de ", (nota1+nota2+nota3)/3)
#13 - Crea un código que calcule e imprima el promedio ponderado de los números 5, 12, 20 y 15 con pesos respectivamente iguales a 1, 2, 3 y 4.
media_ponderada = (5*1 + 12*2 + 20*3 + 15*4) / (1+2+3+4)
print(f'Media {media_ponderada}.')
#Editando textos

#14 - Crea una variable llamada "frase" y asígnale una cadena de texto de tu elección. Luego, imprime la frase en pantalla.
frase= 'Hola'
print(frase)
#15 - Crea un código que solicite una frase y luego imprima la frase en pantalla.
frase= input('Escribe una frase:')
print(frase)
#16 - Crea un código que solicite una frase al usuario y luego imprima la misma frase ingresada pero en mayúsculas.
frase= input('Escribe una frase:')
print(frase.upper())
#17 - Crea un código que solicite una frase al usuario y luego imprima la misma frase ingresada pero en minúsculas.
frase= input('Escribe una frase:')
print(frase.lower())
#18 - Crea una variable llamada "frase" y asígnale una cadena de texto de tu elección. Luego, imprime la frase sin espacios en blanco al principio y al final.
frase='                                 Margaritas  '
print(frase.strip())
#19 - Crea un código que solicite una frase al usuario y luego imprima la misma frase sin espacios en blanco al principio y al final.
frase= input('Escribe una frase:')
print(frase.strip())
#20 - Crea un código que solicite una frase al usuario y luego imprima la misma frase sin espacios en blanco al principio y al final, además de convertirla a minúsculas.
frase= input('Escribe una frase:')
print(frase.strip().lower())
#21 - Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las vocales "e" reemplazadas por la letra "f".
frase= input('Escribe una frase:')
print(frase.replace())
#22 - Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las vocales "a" reemplazadas por el carácter "@".

#23 - Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las consonantes "s" reemplazadas por el carácter "$".