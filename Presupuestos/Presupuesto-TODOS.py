# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 17:29:06 2022

@author: Usuario
"""

import pandas as pd

anios = [*range(2013,2022,1)]
anios = [str(x) for x in anios]

#%%

for i in anios:
    dataset_1 = f'presupuesto-ejecutado-{i}-primer-trimestre.csv'
    dataset_2 = f'presupuesto-ejecutado-{i}-segundo-trimestre.csv'
    dataset_3 = f'presupuesto-ejecutado-{i}-tercer-trimestre.csv'
    dataset_4 = f'presupuesto-ejecutado-{i}-cuarto-trimestre.csv'
    
    df_trim_1 = pd.read_csv(dataset_1, sep = ';', encoding = 'latin-1', decimal=",")
    if df_trim_1.shape[1] == 1:
        df_trim_1 = pd.read_csv(dataset_1, sep = ',', encoding = 'latin-1', decimal=".")

    df_trim_2 = pd.read_csv(dataset_1, sep = ';', encoding = 'latin-1', decimal=",")
    if df_trim_2.shape[1] == 1:
        df_trim_2 = pd.read_csv(dataset_1, sep = ',', encoding = 'latin-1', decimal=".")
        
    df_trim_3 = pd.read_csv(dataset_1, sep = ';', encoding = 'latin-1', decimal=",")
    if df_trim_3.shape[1] == 1:
        df_trim_3 = pd.read_csv(dataset_1, sep = ',', encoding = 'latin-1', decimal=".")
        
    df_trim_4 = pd.read_csv(dataset_1, sep = ';', encoding = 'latin-1', decimal=",")
    if df_trim_4.shape[1] == 1:
        df_trim_4 = pd.read_csv(dataset_1, sep = ',', encoding = 'latin-1', decimal=".")
        
    
    try:
        df_comuna_trim_1 = df_trim_1[['ubicacion_geografica','desc_ubic','vigente']].groupby(['ubicacion_geografica','desc_ubic']).sum().reset_index().sort_values(by='ubicacion_geografica').loc[:14]
    except:
        df_trim_1.columns = df_trim_1.columns.str.upper()
        df_comuna_trim_1 = df_trim_1[['GEO','GEO_DESC','VIGENTE']].groupby(['GEO','GEO_DESC']).sum().reset_index().sort_values(by='GEO').loc[:14]
    
    try:
        df_comuna_trim_2 = df_trim_2[['ubicacion_geografica','desc_ubic','vigente']].groupby(['ubicacion_geografica','desc_ubic']).sum().reset_index().sort_values(by='ubicacion_geografica').loc[:14]
    except:
        df_trim_2.columns = df_trim_1.columns.str.upper()
        df_comuna_trim_2 = df_trim_2[['GEO','GEO_DESC','VIGENTE']].groupby(['GEO','GEO_DESC']).sum().reset_index().sort_values(by='GEO').loc[:14]
        
    try:
        df_comuna_trim_3 = df_trim_3[['ubicacion_geografica','desc_ubic','vigente']].groupby(['ubicacion_geografica','desc_ubic']).sum().reset_index().sort_values(by='ubicacion_geografica').loc[:14]
    except:
        df_trim_3.columns = df_trim_1.columns.str.upper()
        df_comuna_trim_3 = df_trim_3[['GEO','GEO_DESC','VIGENTE']].groupby(['GEO','GEO_DESC']).sum().reset_index().sort_values(by='GEO').loc[:14]
        
    try:
        df_comuna_trim_4 = df_trim_4[['ubicacion_geografica','desc_ubic','vigente']].groupby(['ubicacion_geografica','desc_ubic']).sum().reset_index().sort_values(by='ubicacion_geografica').loc[:14]
    except:
        df_trim_4.columns = df_trim_1.columns.str.upper()
        df_comuna_trim_4 = df_trim_4[['GEO','GEO_DESC','VIGENTE']].groupby(['GEO','GEO_DESC']).sum().reset_index().sort_values(by='GEO').loc[:14]

    
    try:
        df_comuna_trim_1.rename(columns = {'ubicacion_geografica':'comuna','desc_ubic':'desc_comuna','vigente':'presupuesto'}, inplace=True)
    except:
        df_comuna_trim_1.rename(columns = {'GEO':'comuna','GEO_DESC':'desc_comuna','VIGENTE':'presupuesto'}, inplace=True)
    
    try:
        df_comuna_trim_2.rename(columns = {'ubicacion_geografica':'comuna','desc_ubic':'desc_comuna','vigente':'presupuesto'}, inplace=True)
    except:
        df_comuna_trim_2.rename(columns = {'GEO':'comuna','GEO_DESC':'desc_comuna','VIGENTE':'presupuesto'}, inplace=True)
        
    try:
        df_comuna_trim_3.rename(columns = {'ubicacion_geografica':'comuna','desc_ubic':'desc_comuna','vigente':'presupuesto'}, inplace=True)
    except:
        df_comuna_trim_3.rename(columns = {'GEO':'comuna','GEO_DESC':'desc_comuna','VIGENTE':'presupuesto'}, inplace=True)
            
    try:
        df_comuna_trim_4.rename(columns = {'ubicacion_geografica':'comuna','desc_ubic':'desc_comuna','vigente':'presupuesto'}, inplace=True)
    except:
        df_comuna_trim_4.rename(columns = {'GEO':'comuna','GEO_DESC':'desc_comuna','VIGENTE':'presupuesto'}, inplace=True)
        
    

    df_comuna_final = pd.concat([df_comuna_trim_1,df_comuna_trim_2,df_comuna_trim_3,df_comuna_trim_4], ignore_index = True)
    
    try:
        df_comuna_final.rename(columns = {'GEO':'comuna','GEO_DESC':'desc_comuna','VIGENTE':'presupuesto'}, inplace=True)
    except:
        pass
    
    df_comuna_final['desc_comuna'] = df_comuna_final['desc_comuna'].str.upper()
    df_comuna_final = df_comuna_final.groupby(['comuna','desc_comuna']).sum().reset_index().sort_values(by='comuna').loc[:14]
    
    
    df_comuna_final.to_csv(f'AGRUPADOS/final_{i}.csv', sep=';', index=None)
    
#%%


df_1 = pd.read_csv('AGRUPADOS/final_2013.csv', sep=';')
df_1['anio'] = 2013
df_1['comuna'] = df_1['comuna'].astype(int)

df_2 = pd.read_csv('AGRUPADOS/final_2014.csv', sep=';')
df_2['anio'] = 2014
df_2['comuna'] = df_2['comuna'].astype(int)

df_3 = pd.read_csv('AGRUPADOS/final_2015.csv', sep=';')
df_3['anio'] = 2015
df_3['comuna'] = df_3['comuna'].astype(int)

df_4 = pd.read_csv('AGRUPADOS/final_2016.csv', sep=';')
df_4['anio'] = 2016
df_4['comuna'] = df_4['comuna'].astype(int)

df_5 = pd.read_csv('AGRUPADOS/final_2017.csv', sep=';')
df_5['anio'] = 2017
df_5['comuna'] = df_5['comuna'].astype(int)

df_6 = pd.read_csv('AGRUPADOS/final_2018.csv', sep=';')
df_6['anio'] = 2018
df_6['comuna'] = df_6['comuna'].astype(int)

df_7 = pd.read_csv('AGRUPADOS/final_2019.csv', sep=';')
df_7['anio'] = 2019
df_7['comuna'] = df_7['comuna'].astype(int)

df_8 = pd.read_csv('AGRUPADOS/final_2020.csv', sep=';')
df_8['anio'] = 2020
df_8['comuna'] = df_8['comuna'].astype(int)

df_9 = pd.read_csv('AGRUPADOS/final_2021.csv', sep=';')
df_9['anio'] = 2021
df_9['comuna'] = df_9['comuna'].astype(int)

#%%

df_final = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9])
df_final.to_csv('AGRUPADOS/final.csv', sep=';', index=None)

