#Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
#- Mostrar una suma de los dos números
#- Mostrar una resta de los dos números (el primero menos el segundo)
#- Mostrar una multiplicación de los dos números
#- En caso de introducir una opción inválida, el programa informará de que no es correcta.

num1=int(input("Digite el primer numero: "))
num2=int(input("Digite el segundo numero: "))
opcion=int(input("1.Mostrar una suma de los dos números \n2.Mostrar una resta de los dos números \n3.Mostrar una multiplicación de los dos números \nEliga una opción: "))
if opcion==1:
    print("La suma de los dos numeros es: ",num1+num2)
elif opcion==2:
    if num1>num2:
        print("La resta de los dos numeros es: ",num1-num2)
    else:
        print("El primer numero es menor que el segundo. No se puede realizar la resta")
elif opcion==3:
    print("El producto de los dos numeros es: ",num1*num2)
else:
    print("La opcion elegida es incorrecta")