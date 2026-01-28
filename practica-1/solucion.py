#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 11:41:09 2026

@author: nicolas
"""
import pandas as pd
ARCHIVO = "./arbolado-en-espacios-verdes.csv"
def obtener_diccionario_del_parque(file_name:str):
    return pd.read_csv(file_name)
    
    

def leer_parque(nombre_del_archivo:str, parque:str):
    df = obtener_diccionario_del_parque(nombre_del_archivo)
    df['altura_tot'] = pd.to_numeric(df['altura_tot'])
    if(parque):
        return df[df['espacio_ve'] == parque.upper()]
    return df


def especies(lista_arboles):
    nombres_unicos = []
    
    for nombre in lista_arboles['nombre_com']:
        if nombre not in nombres_unicos:
            nombres_unicos.append(nombre)
    return pd.Series(data=nombres_unicos)
    

def contar_ejemplares(lista_arboles):
    res = []
    for arbol in lista_arboles['nombre_com']:
        if arbol in res:
            res[arbol] +=1
        else:
            res[arbol] = 1
    return res

def obtener_alturas(lista_arboles:pd.DataFrame, especie):
    return list(lista_arboles[lista_arboles['nombre_com'] == especie]['altura_tot'])
    

def calcular_promedio_y_maximo(lista_de_alturas):
    if not lista_de_alturas:
        return 0,0
    promedio = sum(lista_de_alturas) / len(lista_de_alturas)
    maximo = max(lista_de_alturas)
    return round(promedio,2), maximo

def obtener_inclinaciones(lista_arboles, ejemplares):
    inclinaciones_registradas = []
    for inclinacion in lista_arboles[lista_arboles['nombre_com']==ejemplares]['inclinacio']:
        inclinaciones_registradas.append(inclinacion)
    return inclinaciones_registradas


def especimen_mas_inclinado(lista_arboles):
    registro_de_especies = []
    especies_registradas = especies(lista_arboles)
    
    for especie in especies_registradas:
        maximo_registro = max(obtener_inclinaciones(lista_arboles, especie))
        registro_de_especies.append((especie,maximo_registro))
    return max(registro_de_especies, key=lambda x:x[1])


def especie_promedio_mas_inclinada(lista_arboles):
    registro_de_especies = []
    especies_registradas = especies(lista_arboles)
    
    for especie in especies_registradas:
        maximo_registro = sum(obtener_inclinaciones(lista_arboles, especie)) / len(obtener_inclinaciones(lista_arboles, especie))
        registro_de_especies.append((especie,maximo_registro))
        
    return max(registro_de_especies, key=lambda x:x[1])

parque = leer_parque('arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
ejemplares = especie_promedio_mas_inclinada(parque)
















