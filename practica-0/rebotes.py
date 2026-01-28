#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 22:16:20 2026

@author: nicolas
"""

import pandas as pd
def pelota():
    altura_inicial = 100 # metros
    current_altura = altura_inicial
    registros = [0]*10
    for i in range(10):
        current_altura *= 3/5
        registros[i] = current_altura
    
    diccionario = {
        'numero_de_botes' : [x for x in range(10)],
        'altura' : registros
    }
    
    df = pd.DataFrame(data=diccionario)
    df.set_index('numero_de_botes', inplace=True)
    df
