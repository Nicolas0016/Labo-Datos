import pandas as pd

especies_seleccionadas = ['tilia x moltkei', 'jacaranda mimosifolia', 'tipuana tipu', 'jacarandá mimosifolia', 'tilia viridis subsp. x moltkei']
columnas_de_interes = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']

df_parques = pd.read_csv('arbolado-en-espacios-verdes.csv')
df_veredas = pd.read_csv('arbolado-publico-lineal-2017-2018.csv')

df_tipas_veredas = df_veredas[columnas_de_interes].copy()
df_tipas_veredas['nombre_cientifico'] = df_tipas_veredas['nombre_cientifico'].str.lower()
df_tipas_veredas = df_tipas_veredas[df_tipas_veredas['nombre_cientifico'].isin(especies_seleccionadas)]

df_tipas_parques = df_parques.copy()
df_tipas_parques = df_tipas_parques.rename(columns={
    'diametro': 'diametro_altura_pecho', 
    'altura_tot': 'altura_arbol'         
})
df_tipas_parques['nombre_cie'] = df_tipas_parques['nombre_cie'].str.lower()
df_tipas_parques = df_tipas_parques[df_tipas_parques['nombre_cie'].isin(especies_seleccionadas)]

df_tipas_parques = df_tipas_parques[['nombre_cie', 'diametro_altura_pecho', 'altura_arbol']].copy()

df_tipas_veredas['ambiente'] = 'vereda'
df_tipas_parques['ambiente'] = 'parque'
df_tipas_parques = df_tipas_parques.rename(columns={'nombre_cie': 'nombre_cientifico'})

# Unificar nombres de especies antes de concatenar
def unificar_nombre_especie(nombre):
    nombre = nombre.lower().strip()
    
    # Jacarandá/Jacaranda
    if 'jacaranda' in nombre or 'jacarandá' in nombre:
        return 'jacaranda mimosifolia'
    
    # Tilia/Tilo
    elif 'tilia' in nombre or 'moltkei' in nombre:
        return 'tilia x moltkei'
    
    # Tipuana/Tipu
    elif 'tipuana' in nombre or 'tipu' in nombre:
        return 'tipuana tipu'
    
    return nombre

# Aplicar unificación
df_tipas_veredas['nombre_unificado'] = df_tipas_veredas['nombre_cientifico'].apply(unificar_nombre_especie)
df_tipas_parques['nombre_unificado'] = df_tipas_parques['nombre_cientifico'].apply(unificar_nombre_especie)

nuevo_df = pd.concat([df_tipas_veredas, df_tipas_parques], ignore_index=True)
nuevo_df['altura_arbol'] = pd.to_numeric(nuevo_df['altura_arbol'], errors='coerce')

alturas_vereda = nuevo_df[nuevo_df['ambiente'] == 'vereda']['altura_arbol'].dropna()
alturas_parque = nuevo_df[nuevo_df['ambiente'] == 'parque']['altura_arbol'].dropna()
