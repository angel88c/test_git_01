
edad = 13
estatura = 1.5

def montana_rusa(edad, estatura):
    if edad > 14 and estatura > 1.62:
        return ("El usuario puede subirse al Push-Pull.")

    else:
        if edad <= 14:
            if estatura <= 1.62:
                return ("El usuario no tiene la edad y la estatura suficientes para subirse al Push-Pull.") 
            else:
                return ("El usuario no tiene la edad suficiente para subirse al Push-Pull")
        else:
            return ("El usuario no tiene la estatura suficiente para subirse al Push-Pull.")   
        
    
print(montana_rusa(edad=15, estatura=1.65))
print(montana_rusa(edad=13, estatura=1.65))
print(montana_rusa(edad=16, estatura=1.6))
print(montana_rusa(edad=13, estatura=1.6))