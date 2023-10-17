"""
Escriba un código que simule ser una máquina checadora de algún estacionamiento. Después de que el usuario ingresó su boleto, lo primero que verá es el costo por uso del estacionamiento (un valor entero random entre 35 y 60). La máquina le pedirá únicamente 3 monedas de valor N que en conjunto sumen el costo total del estacionamiento. Si la suma de las 3 monedas no coincide con el costo total se le solicitará al usuario pasar a la administración; sino, se le dará las gracias por usar el estacionamiento. 
"""

import random

QUANTITY_COINS = 3
parking_cost = random.randint(35, 60)

print("Favor de pagar el total $", parking_cost, " del estacionamiento con ",QUANTITY_COINS," monedas.")
total_amount = 0
i = 1
while i <= QUANTITY_COINS:
    coin = int(float(input("Ingrese una moneda: ")))
    total_amount = total_amount + coin
    i += 1
    
if total_amount >= parking_cost:
    exchange = total_amount - parking_cost
    if exchange > 0:
        print("Tome su cambio: ", exchange) 
        
    print("Gracias por usar el estacionamiento.")
else:
    print("Saldo insuficiente $",total_amount," para cubrir el costo, $", parking_cost," favor de pasar a la Administración.")
    print("Gracias.")