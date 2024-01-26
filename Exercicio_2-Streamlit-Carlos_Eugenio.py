# Exercícios 

# Utilize os arquivos do **RECLAME AQUI** e crie um dashboard com algumas caracteristicas. 

# Empresas: 
# - Hapvida
# - Nagem
# - Ibyte

# O painel deve conter tais informações: 
# 1. Série temporal do número de reclamações. 
# 2. Frequência de reclamações por estado. 
# 3. Frequência de cada tipo de **STATUS**
# 4. Distribuição do tamanho do texto (coluna **DESCRIÇÃO**) 

# Alguns botões devem ser implementados no painel para operar filtros dinâmicos. Alguns exemplos: 
# 1. Seletor da empresa para ser analisada. 
# 2. Seletor do estado. 
# 3. Seletor por **STATUS**
# 4. Seletor de tamanho do texto 

# Faça o deploy da aplicação. Dicas: 
# https://www.youtube.com/watch?v=vw0I8i7QJRk&list=PLRFQn2r6xhgcDMhp9NCWMqDYGfeeYsn5m&index=16&t=252s
# https://www.youtube.com/watch?v=HKoOBiAaHGg&t=515s

# Exemplo do github
# https://github.com/jlb-gmail/streamlit_teste

# **OBSERVAÇÃO**
# A resposta do exercicio é o link do github e o link da aplicação. Coloque-os abaixo.  

import pandas as pd 
import numpy as np 
import plotly.express as px 
import streamlit as st
import datetime
import seaborn as sns
import matplotlib as plt
import matplotlib.pyplot as plt

#### CARREGAR OS DADOS ####
df_hap=pd.read_csv('RECLAMEAQUI_HAPVIDA.csv')
df_ibyte=pd.read_csv('RECLAMEAQUI_IBYTE.csv')
df_nagem=pd.read_csv('RECLAMEAQUI_NAGEM.csv')

## DATETIME ##
df_hap['TEMPO']=pd.to_datetime(df_hap['TEMPO'])
df_ibyte['TEMPO']=pd.to_datetime(df_ibyte['TEMPO'])
df_nagem['TEMPO']=pd.to_datetime(df_nagem['TEMPO'])

### CRIAR COLUNA ESTADO EM TODOS OS DATASETS ###
df_hap['UF'] = df_hap['LOCAL'].str[-2:]
df_ibyte['UF'] = df_ibyte['LOCAL'].str[-2:]
df_nagem['UF'] = df_nagem['LOCAL'].str[-2:]


#### STREAMLIT ####
st.title('DASHBOARD - RECLAME AQUI - IBYTE, HAP VIDA E NAGEM')

st.write('Esse dashboard apresenta dados do Reclame Aqui da Ibyte, Hap Vida e Nagem - Trabalho 2 - Carlos Eugenio')

lista_locais=df_hap['UF'].unique()

lista_status= df_hap['STATUS'].unique()

#lista_ano=df_ibyte['ANO'].unique()


with st.sidebar:
        local = st.selectbox('Selecione o Estado',lista_locais)
        status = st.selectbox('Selecione o Status do atendimento', lista_status)
        #ano = st.selectbox('Selecione o Ano das reclamações',lista_ano)
        seletor = st.selectbox('Selecione a Empresa', ['','Nagem', 'Hap Vida','Ibyte'])       
 

# hap_local=(df_hap['UF']==local).sum()
# ibyte_local=(df_ibyte['UF']==local).sum()
# nagem_local=(df_nagem['UF']==local).sum()


# col1 = st.columns(1)
# col1, col2, col3 = st.columns(1)
# col1.metric(label="Reclamações - Hap Vida", value=hap_local)
# col2.metric(label="Reclamações - Ibyte", value=ibyte_local)
# col3.metric(label="reclamações - Nagem", value=nagem_local)


# fig_hap=px.bar(df_hap, x='STATUS', y='TEMPO', labels={'Ocorrências - Hap Vida - ','ANO'},title='Reclamações - HAP VIDA')

# fig_ibyte=px.bar(df_ibyte, x='STATUS', y='TEMPO', labels={'Ocorrências - Ibyte - ','ANO'},title='Reclamações - IBYTE')

# fig_nagem=px.bar(df_nagem, x='STATUS', y='TEMPO', labels={'Ocorrências - Nagem - ','ANO'},title='Reclamações - NAGEM')

if seletor=='Hap Vida': 
        df_local=df_hap[df_hap['UF']==local]
        df_status=df_local[df_local['STATUS']==status]
        # df_ano=df_status[df_status['ANO']==ano]
        qtd_hap=(df_local['STATUS']==status).sum()
        
        st.write("Reclamações - HAP VIDA", qtd_hap)
        st.write(df_status)
        st.markdown('---')
        
        fig_UF=px.bar(df_hap, x='STATUS', y='UF', labels={'Ocorrências - HAP VIDA - '},title='Reclamações - HAP VIDA - Por STATUS')
        st.plotly_chart(fig_UF)
        st.markdown('---')

        fig_local=px.bar(df_local, x='LOCAL', y='STATUS', labels={'Ocorrências - IBYTE - '},title='Reclamações - HAP VIDA - Por LOCAL')
        st.plotly_chart(fig_local)
        st.markdown('---')
        
        fig_hap=px.bar(df_local, x='ANO', y='STATUS', labels={'Ocorrências - HAP VIDA - '},title='Reclamações - HAP VIDA - Por ANO')
        st.plotly_chart(fig_hap)
        st.markdown('---')
        
        fig_UF=px.bar(df_hap, x='UF', y='STATUS', labels={'Ocorrências - NAGEM - '},title='Reclamações - HAP VIDA - Por ESTADO')
        st.plotly_chart(fig_UF)

       
if seletor=='Ibyte':       
        df_local=df_ibyte[df_ibyte['UF']==local]
        df_status=df_local[df_local['STATUS']==status]
        # df_ano=df_status[df_status['ANO']==ano]
        qtd_ibyte=(df_local['STATUS']==status).sum()
        
        st.write("Reclamações - IBYTE", qtd_ibyte)
        st.write(df_status)
        st.markdown('---')
        
        fig_UF=px.bar(df_ibyte, x='STATUS', y='UF', labels={'Ocorrências - IBYTE - '},title='Reclamações - IBYTE - Por STATUS')
        st.plotly_chart(fig_UF)
        st.markdown('---')
        
        fig_local=px.bar(df_local, x='LOCAL', y='STATUS', labels={'Ocorrências - IBYTE - '},title='Reclamações - IBYTE - Por LOCAL')
        st.plotly_chart(fig_local)
        st.markdown('---')

        fig_ibyte=px.bar(df_local, x='ANO', y='STATUS', labels={'Ocorrências - IBYTE - '},title='Reclamações - IBYTE')
        st.plotly_chart(fig_ibyte)
        st.markdown('---')
        
        fig_UF=px.bar(df_ibyte, x='UF', y='STATUS', labels={'Ocorrências - NAGEM - '},title='Reclamações - IBYTE - Por ESTADO')
        st.plotly_chart(fig_UF)


if seletor=='Nagem':       
        df_local=df_nagem[df_nagem['UF']==local]
        df_status=df_local[df_local['STATUS']==status]
        # df_ano=df_status[df_status['ANO']==ano]
        qtd_nagem=(df_local['STATUS']==status).sum()
        
        st.write("Reclamações - NAGEM", qtd_nagem)
        st.write(df_status)
        st.markdown('---')
        
        fig_UF=px.bar(df_nagem, x='STATUS', y='UF', labels={'Ocorrências - NAGEM - '},title='Reclamações - NAGEM - Por STATUS')
        st.plotly_chart(fig_UF)
        st.markdown('---')

        fig_local=px.bar(df_local, x='LOCAL', y='STATUS', labels={'Ocorrências - IBYTE - '},title='Reclamações - NAGEM - Por LOCAL')
        st.plotly_chart(fig_local)
        st.markdown('---')
        
        fig_nagem=px.bar(df_local, x='ANO', y='STATUS', labels={'Ocorrências - NAGEM - '},title='Reclamações - NAGEM - Pos ANO')
        st.plotly_chart(fig_nagem)
        st.markdown('---')
        
        fig_UF=px.bar(df_nagem, x='UF', y='STATUS', labels={'Ocorrências - NAGEM - '},title='Reclamações - NAGEM - Por ESTADO')
        st.plotly_chart(fig_UF)
    

# with st.sidebar:
#       seletor=st.selectbox('Selecione a Empresa', ['','Hap Vida','Ibyte','Nagem',"NENHUM PLOT"])


# fig_hap=px.bar(df_hap, x='STATUS', y='TEMPO', labels={'Ocorrências - Hap Vida - ','ANO'},title='Reclamações - HAP VIDA')

# fig_ibyte=px.bar(df_ibyte, x='STATUS', y='TEMPO', labels={'Ocorrências - Ibyte - ','ANO'},title='Reclamações - IBYTE')

# fig_nagem=px.bar(df_nagem, x='STATUS', y='TEMPO', labels={'Ocorrências - Nagem - ','ANO'},title='Reclamações - NAGEM')
  

# if seletor=='Hap Vida': 
#         st.plotly_chart(fig_hap)
       
# if seletor=='Ibyte':       
#         st.plotly_chart(fig_ibyte)

# if seletor=='Nagem':       
#         st.plotly_chart(fig_nagem)









