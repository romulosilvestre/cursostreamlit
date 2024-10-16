import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import pandas as std
import json

def muda_valor(valor):
        if valor >= 1000000:
            return f" {valor/1000000:.1f} milhões"
        elif valor >= 1000:
            return f" {valor/1000:.1f} mil"
        else:
            return f" {valor:.2f}" 

st.title("Dashboard de Vendas:shopping_trolley: ")
url="https://labdados.com/produtos"
response= requests.get(url)

# json > convertido para dicionário > Convertido para databframe
df = pd.DataFrame.from_dict(response.json())
if st.button("todos"):
    st.balloons()         
    st.metric("Receita R$:",muda_valor(df['Preço'].sum()))
    st.metric("Quantidade de vendas (linhas)",muda_valor(df.shape[0]))
    st.metric("Quantidade de variaveis (colunas)",df.shape[1])   
    
    st.dataframe(df)
    st.snow()

     # mostrar bolhas nos mapas
    # ter a latitude e longitue
    # como col"ocamos esse tipo de gráfico
    # st.plotly_chart(my_plotly_chart)
    # podemos usar o matplotlib para criar o gráfico
    # depois criar o gráfico dentro do aplicativo
    # instalamos o plotly para criar gráficos
    # depois o st.plotly para passar a figura
    # st.map () ele é limitado, não consegue aumentar a bolha
    # passo 1 - criar uma tabela com a soma das receitas de cada um dos estados
    # passo 2 - vamos construir uma tabela e vamos agrupar


    ## Tabelas - construir
    receitas_estados = df.groupby('Local da compra')[['Preço']].sum()
    # perdemos a informação de latitude e longitude
    # vamos remover linhas que tem informação duplicada
    # quero retirar as duplicadas com base no subset df.drop_duplicates(subset)
    # quero manter
    receitas_estados = df.drop_duplicates(subset='Local da compra')[['Local da compra','lat','lon']].merge(receitas_estados,left_on='Local da compra',right_index=True).sort_values('Preço',ascending=False)
    
    ## Gráficos com Plotly
    fig_mapa_receita = px.scatter_geo(
                          receitas_estados,
                          lat='lat',
                          lon = 'lon',
                          scope='south america',
                          size='Preço',
                          template = 'seaborn',
                          hover_name='Local da compra', 
                          hover_data = {'lat':False,'lon':False},
                          title="Receita por estado"
                   

    )

    ## Visualização no Streamlit
    st.plotly_chart(fig_mapa_receita)
else:
    st.write("Clique no botão todos")