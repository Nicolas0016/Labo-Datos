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
especies_parques = ['tilia x moltkei', 'jacarandá mimosifolia', 'tilia viridis subsp. x moltkei', 'tipuana tipu']
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

# CONVERTIR ALTURAS A NÚMERICAS
nuevo_df['altura_arbol'] = pd.to_numeric(nuevo_df['altura_arbol'], errors='coerce')

# CREAR GRUPOS DE ESPECIES EQUIVALENTES
mapeo_especies = {
    'tilia x moltkei': 'tilia moltkei',
    'tilia viridis subsp. x moltkei': 'tilia moltkei',
    'jacaranda mimosifolia': 'jacaranda',
    'jacarandá mimosifolia': 'jacaranda',
    'tipuana tipu': 'tipuana tipu'
}

# Agregar columna con grupo de especie
nuevo_df['grupo_especie'] = nuevo_df['nombre_cientifico'].map(mapeo_especies)

# Separar alturas por ambiente
alturas_vereda = nuevo_df[nuevo_df['ambiente'] == 'vereda']['altura_arbol'].dropna()
alturas_parque = nuevo_df[nuevo_df['ambiente'] == 'parque']['altura_arbol'].dropna()

#%% 5. CREAR GRÁFICOS
import matplotlib.pyplot as plt

# GRÁFICO 1: Altura por ambiente
plt.figure(figsize=(7, 5))
plt.boxplot([alturas_vereda, alturas_parque], labels=['Vereda', 'Parque'])
plt.title('Altura por ambiente')
plt.ylabel('Altura (m)')
plt.savefig('grafico1_altura.png')
plt.show()

# GRÁFICO 2: Conteo por GRUPO de especie (agrupando nombres similares)
plt.figure(figsize=(10, 6))

# Preparar datos para el gráfico - usar grupos de especies
grupos_especies = nuevo_df['grupo_especie'].unique()
vereda_counts = []
parque_counts = []

for grupo in grupos_especies:
    vereda_counts.append(len(nuevo_df[(nuevo_df['grupo_especie'] == grupo) & 
                                     (nuevo_df['ambiente'] == 'vereda')]))
    parque_counts.append(len(nuevo_df[(nuevo_df['grupo_especie'] == grupo) & 
                                     (nuevo_df['ambiente'] == 'parque')]))

# Crear gráfico de barras
x = range(len(grupos_especies))
bar_width = 0.35

plt.bar(x, vereda_counts, width=bar_width, label='Vereda', color='blue', align='center')
plt.bar([i + bar_width for i in x], parque_counts, width=bar_width, label='Parque', color='green', align='center')

# Formatear etiquetas
etiquetas = [grupo.title() for grupo in grupos_especies]
plt.xticks([i + bar_width/2 for i in x], etiquetas, rotation=0, ha='center')

plt.title('Conteo por especie (agrupando nombres equivalentes)')
plt.ylabel('Cantidad')
plt.legend()
plt.tight_layout()
plt.savefig('grafico2_conteo_agrupado.png', dpi=150, bbox_inches='tight')
plt.show()

# GRÁFICO 3: Altura por especie y ambiente (opcional - más detallado)
plt.figure(figsize=(12, 6))

# Preparar datos para boxplot múltiple
datos_boxplot = []
etiquetas_boxplot = []

for grupo in grupos_especies:
    # Alturas en vereda para este grupo
    alt_vereda = nuevo_df[(nuevo_df['grupo_especie'] == grupo) & 
                         (nuevo_df['ambiente'] == 'vereda')]['altura_arbol'].dropna()
    if len(alt_vereda) > 0:
        datos_boxplot.append(alt_vereda)
        etiquetas_boxplot.append(f'{grupo.title()}\nVereda')
    
    # Alturas en parque para este grupo
    alt_parque = nuevo_df[(nuevo_df['grupo_especie'] == grupo) & 
                         (nuevo_df['ambiente'] == 'parque')]['altura_arbol'].dropna()
    if len(alt_parque) > 0:
        datos_boxplot.append(alt_parque)
        etiquetas_boxplot.append(f'{grupo.title()}\nParque')

# Crear boxplot múltiple
plt.figure(figsize=(12, 6))
box = plt.boxplot(datos_boxplot, labels=etiquetas_boxplot, patch_artist=True)

# Colorear alternadamente
colors = ['lightblue', 'lightgreen'] * len(grupos_especies)
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Altura por especie y ambiente (agrupando nombres equivalentes)')
plt.ylabel('Altura (m)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico3_altura_especie.png', dpi=150, bbox_inches='tight')
plt.show()

