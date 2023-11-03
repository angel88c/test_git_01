#Ejercicio 1, Evaluacion 2
#Crea una Función que reciba (directamente o desde el usuario) una cadena 
#de texto y retorne un mensaje confirmando si es un Palíndromo o no.
def is_palindrome(cadena: str):
    try:
        cadena_rev = cadena[::-1].replace(" ", "").lower()
        cadena_rev = cadena_rev.replace(" ", "")
        cadena_rev = cadena_rev.lower()
        
        cadena = cadena.lower() #ascii
        cadena = cadena.replace(" ", "")
        
        print(f"cadena entrada: {cadena}")
        print(f"cadena reversa: {cadena_rev}")
        return True if cadena == cadena_rev else False
        
    except Exception as e:
        print("     ->",str(e), f" cadena: {cadena}")
        return False

frases = ["Oir a Diario", "Oiras orar a Rosario", "Anita Lava la tina", 
          "Amor a Roma","Amo la Pacifica Paloma", "The killers", "123", "Seres"]

for frase in frases:
    ok = is_palindrome(frase)
    print(f"La frase '{frase}' {'ES' if ok else 'NO ES'} Palindromo.")
    print(f"")