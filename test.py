
def comprar_agua_y_chocolate(costo_agua, costo_chocolate, saldo):
    #Sumar los costos del agua
    #y del chocolate
    costo_total = costo_agua + costo_chocolate
    if (saldo >= costo_total):
        print(f"Tu saldo es {saldo}, puedes comprar agua y chocolate.")
    else:
        print(f'Tu saldo {saldo} es insuficiente para comprar agua y chocolate. {costo_total}')


def comprar_agua(costo_agua, saldo):
    if (saldo >= costo_agua):
        print(f"Tu saldo es {saldo}, puedes comprar agua.")
    else:
        print(f'Tu saldo {saldo} es insuficiente para comprar agua. {costo_agua}')

def comprar_chocolate(costo_chocolate, saldo):
    if (saldo >= costo_chocolate):
        print(f"Tu saldo es {saldo}, puedes comprar chocolate.")
    else:
        print(f'Tu saldo {saldo} es insuficiente para comprar chocolate. {costo_chocolate}')

saldo = 200
costo_chocolate = 150
costo_agua = 100

comprar_agua_y_chocolate(costo_agua, costo_chocolate, saldo)
comprar_agua(costo_agua, saldo)
comprar_chocolate(costo_chocolate, saldo)