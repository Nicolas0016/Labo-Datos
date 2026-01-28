import pandas as pd

columnas_vereda = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']

#%% VEREDAS
especies_veredas = ['tilia x moltkei', 'jacaranda mimosifolia', 'tipuana tipu']
df_veredas = pd.read_csv('arbolado-publico-lineal-2017-2018.csv')

df_tipas_veredas = df_veredas[columnas_vereda].copy()
df_tipas_veredas['nombre_cientifico'] = df_tipas_veredas['nombre_cientifico'].str.lower()
df_tipas_veredas = df_tipas_veredas[df_tipas_veredas['nombre_cientifico'].isin(especies_veredas)]
df_tipas_veredas['ambiente'] = 'vereda'


#%% Parques
especies_parques = ['tilia x moltkei', 'jacarandá mimosifolia', 'Tilia viridis subsp. x moltkei', 'tipuana tipu']
df_parques = pd.read_csv('arbolado-en-espacios-verdes.csv')

df_tipas_parques = df_parques.copy()
df_tipas_parques = df_tipas_parques.rename(columns={
    'diametro': 'diametro_altura_pecho', 
    'altura_tot': 'altura_arbol'         
})
df_tipas_parques['nombre_cie'] = df_tipas_parques['nombre_cie'].str.lower()
df_tipas_parques = df_tipas_parques[df_tipas_parques['nombre_cie'].isin(especies_parques)]

df_tipas_parques = df_tipas_parques[['nombre_cie', 'diametro_altura_pecho', 'altura_arbol']].copy()
df_tipas_parques['ambiente'] = 'parque'
df_tipas_parques = df_tipas_parques.rename(columns={'nombre_cie': 'nombre_cientifico'})
df_tipas_parques['ancho_acera'] = pd.NA

#%% CONCATENAR DOS DF
nuevo_df = pd.concat([df_tipas_veredas, df_tipas_parques], ignore_index=True)
