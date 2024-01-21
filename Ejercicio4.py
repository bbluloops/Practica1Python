#Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
#pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
#puede ser calculada de la siguiente forma:

# 1+2+3+...+n=n(n+1)/2

N=int(input("Digite un numero: "))

suma=N*(N+1)/2

print("La suma de los primeros ",N," números es: ",suma)
