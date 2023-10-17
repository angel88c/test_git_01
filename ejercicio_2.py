#El mes debe estar entre 1 y 12 de lo contrario, es incorrecto.
def validar_mes(month):
    if month >12 or month <=0:
        print("El mes de nacimiento no existe, debe ser entre 1 y 12.")
        return False
    
    return True

#Se verifica que el dia este dentro de los dias del mes, 
#de lo contrario, es incorrecto.
def validar_dia(month, day):
    
    #Suponiendo que los años bisiestos no existen
    dias_al_mes = {
        1: 31, 
        2: 28,
        3:31, 
        4:30, 
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    }
    
    #En este punto la validacion del mes ya necesariamente debió haberse hecho
    if day > dias_al_mes[month] or day <=0:
        return False
    
    return True
    
def obtener_generacion(year):    
    if year >=1920 and year < 1940:
        print("Eres de la generacion silenciosa.")
    elif year >= 1940 and year < 1960:
        print("Eres de la generacion Boomers")
    elif year >= 1960 and year < 1980:
        print("Eres de la generacion X")
    elif year >= 1980 and year < 1990:
        print("Eres de la generacion Y")
    elif year >= 1990:
        print("Eres de la generación Z")
    else:
        print("Generacion no encontrada.")
        
def obtener_edad_y_generacion(year, month, day, year_of_death=None):
    
    current_year = int(2023)
    current_month = int(10)
    current_day = int(8)
    
    edad = current_year - int(year)
    
    print()
    if not validar_mes(month):
        return None
    
    #Se verifica que el año de fallecimiento sea despues del año de nacimiento,
    #De lo contrario, es incorrecto
    if year_of_death is not None and year_of_death < year:
        print("Datos incorrectos, año de fallecimiento no puede ser menor que año de nacimiento.")
        return None
    
    if not validar_dia(month, day):
        print("Datos incorrectos, el mes " +str(month) + " no contiene un dia " + str(day))
        return None
    
    #Si el mes actual es mayor que el mes de nacimiento, ya ha cumplido años el susodicho
    #En caso de que ya haya fallecido, se indica
    if current_month > month:
        if year_of_death is not None:
            print("Ya has fallecido a los "+str(edad)+" años.")
        else:
            print("En este año ya has cumplido " + str(edad) + " años")
            
    #Si estamos en el mes de nacimiento, se verifica si el dia de cumpleaños ya paso.
    elif current_month == month and current_day >= day:
        print("En este año ya has cumplido " + str(edad) + " años")
        if year_of_death is not None:
            print("Ya has fallecido.")
        
    else:
        #Si el dia de cumpleaños no ha ocurrido y no ha fallecido
        #La edad aun no la alcanza, por lo cual se le resta 1
        edad = edad - 1
        if year_of_death is not None:
            print("Ya has fallecido a los "+str(edad)+" años, no cumplirás años")
        else:
            print("Tienes " + str(edad) + " años, en este año cumplirás " + str(edad + 1))
            
    obtener_generacion(year)
    return edad
            
obtener_edad_y_generacion(2060, 11, 13, 2023)
obtener_edad_y_generacion(1889, 0, 14, 1890)
obtener_edad_y_generacion(2001, 6, 0)
obtener_edad_y_generacion(1993, 10, 1)


