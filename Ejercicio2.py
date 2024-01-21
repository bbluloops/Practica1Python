#En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
#restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
#Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
#porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
#dejar como propina.

consumo=float(input("Digite su consumo: "))
propina=float(input("Porcentaje de propina desea dejar: "))

cantidad_propina=consumo*propina/100

print("La cantidad de propina que debe dejar es:  ",cantidad_propina)
