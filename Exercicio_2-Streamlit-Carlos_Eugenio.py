import pandas as pd 
import numpy as np 
import plotly.express as px 
import streamlit as st
import datetime

#### CARREGAR OS DADOS ####
df_hap=pd.read_csv('RECLAMEAQUI_HAPVIDA.csv',sep=';')
df_ibyte=pd.read_csv('RECLAMEAQUI_IBYTE.csv',sep=';')
df_nagem=pd.read_csv('RECLAMEAQUI_NAGEM.csv',sep=';')

## DATETIME ####
df_hap['TEMPO']=pd.to_datetime(df_hap['TEMPO'])
df_ibyte['TEMPO']=pd.to_datetime(df_ibyte['TEMPO'])
df_nagem['TEMPO']=pd.to_datetime(df_nagem['TEMPO'])

####CRIAR COLUNA ESTADO EM TODOS OS DATASETS ###
df_hap['UF'] = df_hap['LOCAL'].str[-2:]
df_ibyte['UF'] = df_ibyte['LOCAL'].str[-2:]
df_nagem['UF'] = df_nagem['LOCAL'].str[-2:]


#### STREAMLIT###
st.title('DASHBOARD - RECLAME AQUI - IBYTE, HAP VIDA E NAGEM')

st.write('Esse dashboard apresenta dados do Reclame Aqui da Ibyte, Hap Vida e Nagem')

lista_locais=df_hp['UF'].unique()
local = st.selectbox(
    'Selecione o local',
    lista_locais)
 
    
hap_local=df_hap[local].sum()
ibyte_local=df_ibyte[local].sum()
nagem_local=df_nagem[local].sum()


col1, col2, col3= st.columns(3)
col1.metric(label="Reclamações - Hap Vida", value=hap_local)
col2.metric(label="Reclamações - Ibyte", value=ibyte_local)
col3.metric(label="reclamações - Nagem", value=nagem_local)

st.markdown('---')

fig_hap=px.bar(df_hap,x='DATA',y=local,labels={local:'Hap Vida'},title=local)

fig_ibyte=px.bar(df_ibyte,x='DATA',y=local,labels={local:'Ibyte'},title=local)

fig_nagem=px.bar(df_nagem,x='DATA',y=local,labels={local:'Nagem'},title=local)

with st.sidebar:
        seletor=st.selectbox(
    'Selecione o tipo do dado',
    ['hap Vida','Ibyte','Nagem',"NENHUM PLOT"])
    
    

if seletor=='Hap Vida': 
        st.plotly_chart(fig_hap)

if seletor=='Ibyte':       
        st.plotly_chart(fig_ibyte)

if seletor=='Nagem':       
        st.plotly_chart(fig_nagem)









