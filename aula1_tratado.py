import streamlit as st
import requests
import pandas as pd

st.title("DASHBOARD DE VENDAS:shopping_trolley:")

url = "https://labdados.com/produtos"
response = requests.get(url)

# Verifica se a resposta foi bem-sucedida
if response.status_code == 200:
    try:
        # Tenta converter a resposta em JSON
        data = response.json()
        df = pd.DataFrame.from_dict(data)
        
        if st.button("todos"):
            st.balloons()
            st.dataframe(df)
            st.snow()
        else:
            st.write("clique no botão todos")
    except ValueError:
        st.error("Erro ao converter a resposta para JSON.")
else:
    st.error("Erro ao acessar os dados: " + str(response.status_code))