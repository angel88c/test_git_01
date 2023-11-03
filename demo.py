"""
    Demo script
"""
import os
import sys

def function_1(**kwargs):
    if kwargs["status"]:
        print("True")

def saludar(nombre):
    print ("Hey " + nombre)
    
def saludar(nombre, apellido):
    print("Hey " +nombre + " " + apellido)
    
if __name__ == "__main__":
    function_1(data="213", status=False)
    saludar("Alex", "Eli")
    print("Sobreescrito") 
