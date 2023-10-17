numero = 10
i = 0
suma = 0

while i <= numero:
    if i % 2 == 0:
        suma = suma + i
    
    i += 1


print("La suma de los pares es: ", suma)