# Baby Steps - TDD

# Importando a biblioteca
import streamlit as st

# Inteface gráfica com o usuário
num =st.number_input("Digite um valor: ",step=1)

# Algoritmo para positivo negativo e nulo
if num >= 1:
    st.write(f"Número positivo: {num}")
elif num <= -1:
    st.write(f"Número negativo: {num}")
else:
    st.write(f"Número nulo")
# Mostrando os resultados

