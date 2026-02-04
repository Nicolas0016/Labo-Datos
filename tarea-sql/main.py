#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 15:45:10 2026

@author: nicolas
"""

import pandas as pd
import duckdb as dd
#%%
carpeta = "~/programacion/Labo-Datos/tarea-sql/"

casos = pd.read_csv(carpeta+"casos.csv")
departamento = pd.read_csv(carpeta+"departamento.csv") 
grupoetario = pd.read_csv(carpeta+"grupoetario.csv")
grupo_etario = pd.read_csv(carpeta+"grupoetario.csv")
provincia= pd.read_csv(carpeta+"provincia.csv")
tipo_evento = pd.read_csv(carpeta + "tipoevento.csv")

#%% Listar sólo los nombres de todos los departamento

consulta = """
        SELECT Descripcion
        FROM departamento
"""

df_resultado = dd.sql(consulta).df()
df_resultado

#%% Listar sólo los nombres de todos los departamento

consulta = """
        SELECT DISTINCT Descripcion
        FROM departamento
"""

df_resultado = dd.sql(consulta).df()
df_resultado

#%%

consulta = """
        SELECT DISTINCT Descripcion
        FROM departamento
"""

df_resultado = dd.sql(consulta).df()
df_resultado

#%%

consulta = """
        SELECT DISTINCT 
        ID , 
        Descripcion
        FROM departamento
"""

df_resultado = dd.sql(consulta).df()
df_resultado
#%%

consulta = """
        SELECT DISTINCT 
        ID, 
        Descripcion,
        id_provincia
        FROM departamento
"""

df_resultado = dd.sql(consulta).df()
df_resultado
#%%
consulta = """
        SELECT DISTINCT 
        ID AS codigo_depto, 
        Descripcion AS nombre_depto
        FROM departamento
"""

df_resultado = dd.sql(consulta).df()
df_resultado
#%%
consulta = """
        SELECT DISTINCT *
        FROM departamento
        WHERE id_provincia = 54
"""

df_resultado = dd.sql(consulta).df()
df_resultado

#%%

consulta = """
        SELECT DISTINCT *
        FROM departamento
        WHERE 
        id_provincia = 22 OR 
        id_provincia = 78 OR
        id_provincia = 86
"""

df_resultado = dd.sql(consulta).df()
df_resultado
#%%
consulta = """
        SELECT DISTINCT *
        FROM departamento
        WHERE 
        id_provincia >= 50 AND
        id_provincia <= 59
"""

df_resultado = dd.sql(consulta).df()
df_resultado

#%%INNER JOIN

consulta = """
        SELECT DISTINCT 
        departamento.id, departamento.descripcion, 
        provincia.descripcion as provincia
        FROM departamento
        INNER JOIN provincia
        ON departamento.id_provincia = provincia.id
"""

df_resultado = dd.sql(consulta).df()
df_resultado

#%%

consulta = """
        SELECT DISTINCT 
        *
        FROM casos
        INNER JOIN departamento
        ON casos.id_depto = departamento.id
        WHERE departamento.id_provincia = '22'
"""

df_resultado = dd.sql(consulta).df()
df_resultado

#%%

consulta = """
        SELECT DISTINCT 
        *
        FROM casos
        INNER JOIN departamento
        ON casos.id_depto = departamento.id
        WHERE 
        departamento.id_provincia = '6' AND 
        casos.cantidad > 10
"""

df_resultado = dd.sql(consulta).df()
df_resultado
#%%
consulta = """
        SELECT DISTINCT 
        *
        FROM casos
        RIGHT JOIN departamento
        ON casos.id_depto = departamento.id
        WHERE casos.id IS NULL
        
"""

df_resultado = dd.sql(consulta).df()
df_resultado


#%%
consulta = """
        SELECT DISTINCT 
        tipo_evento.descripcion
        FROM casos
        RIGHT JOIN tipo_evento
        ON casos.id_tipoevento = tipo_evento.id
        WHERE casos.id IS NULL
        
"""

df_resultado = dd.sql(consulta).df()
df_resultado

#%%

consulta = """
    SELECT sum(cantidad) AS Total_Registros from casos
"""

df_resultado = dd.sql(consulta).df()
df_resultado

#%%

consulta = """
    SELECT anio as AÑO, SUM(cantidad) as cantidad FROM casos
    INNER JOIN tipo_evento
    ON id_tipoevento = tipo_evento.id
    
    GROUP BY anio
"""

df_resultado = dd.sql(consulta).df()
df_resultado

#%%

consulta = """
    SELECT anio as AÑO, SUM(cantidad) as cantidad FROM casos
    INNER JOIN tipo_evento
    ON id_tipoevento = tipo_evento.id
    WHERE anio = 2019
    GROUP BY anio
"""

df_resultado = dd.sql(consulta).df()
df_resultado
#%%

consulta = """
    SELECT id_depto, count(*) as cantidad 
    FROM casos
    GROUP BY id_depto
"""

df_resultado = dd.sql(consulta).df()
df_resultado