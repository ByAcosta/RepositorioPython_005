a=int(input("Digite un numero:"))
b=int(input("Digite un numero: "))
suma=a+b
multi=a*b
print("La suma de "+str(a)+"y de "+str(b+" es igual a "+str(suma)))
print("La multiplicación de " + str(a) + " y de "+ str(b) + " es igual a "+str(multi))
#if
if(a>b):
    print("El numero " + str(a) + " es mayor que " + str(b))
elif(a<b):
    print("El numero " + str(b) + " es mayor que " + str(a))
else:
    print("Los numeros son iguales")