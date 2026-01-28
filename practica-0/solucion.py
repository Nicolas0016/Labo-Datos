#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rebotes import pelota
"""
Created on Tue Jan 27 21:40:53 2026

@author: nicolas
"""
def ejercicio1():
    altura_del_obelisco = 67.5 # en metros
    espesor_del_billete = 0.11 # en milimetros
    espesor_del_monticulo = espesor_del_billete
    altura_del_obelisco_mm = altura_del_obelisco * 1000
    dia = 1
    while (altura_del_obelisco_mm > espesor_del_monticulo):
        espesor_del_monticulo *= 2
        dia += 1
    return dia

def ejercicio2(word:str):
    vocals = ["a","e","i","o","u"]
    res = ""
    for letter in word:
        if letter in vocals:
            res += letter + "p" 
        res += letter 
    return res

# ejercicio 3
def pertenece(lista:list, elem) -> bool:
    for item in lista:
        if (item == elem):
            return True
    return False
    
# ejercicio 4
def mas_larga(lista1:list, lista2:list) -> list:
    if(len(lista1) > len(lista2)): 
        return lista1
    return lista2

# ejercicio 5
pelota()

# ejecicio 6
def mezclar(cadena1:str, cadena2:str)-> str:
    indice = 0
    res = ""
    while ((indice < len(cadena1)) and (indice < len(cadena2))):
        res += cadena1[indice]
        res += cadena2[indice]
        indice += 1
        
    if not (indice < len(cadena1)):
        res += cadena1[indice:] 
    if not (indice < len(cadena2)):
        res += cadena2[indice:] 
    return res

# ejercicio 7
# traductor
def traductor_geringoso(lista:list[str]):
    res = {}
    for word in lista:
        res[word] = ejercicio2(word)
    return res
        
def filaDeTabla(number:int)->list[int]:
    res = [number,0,0,0,0,0,0,0,0,0,0]
    for i in range(1,len(res)):
        res[i] = (i-1)*number
    return res[1:]

def tablaDeMultiplicar():
   res = [0,1,2,3,4,5,6,7,8,9]
   for i in range(len(res)):
       res[i] = filaDeTabla(i)
   
   return res
        
    
    
def main():
    print(tablaDeMultiplicar())
if __name__ == "__main__":
    main()
















