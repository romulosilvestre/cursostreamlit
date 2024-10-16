import streamlit as st
import random
# 1. Crie um algoritmo que descobra um número secreto!

# 2. Criar o número secreto

numero_secreto = random.randint(1, 10)

# 3. Título na aplicação
st.write(f"número secreto gerado:{numero_secreto}")
st.title("Jogo do Número Secreto")

# 4. Dar uma mensagem de boas vindas

st.write("Boas-vindas ao jogo do número secreto")

# 5. Receber o chute do usuário
chute = st.number_input("Escolha um número de 1 a 10",
                        min_value=1,
                        max_value=10,step=1)
# 6. Verificar o chute com o número secreto
if st.button('Jogar'):
    if chute == numero_secreto:
    # 7. Mostrar uma mensagem personalizada
       st.balloons() 
       st.success(f"Isso aí! Você descobriu o número secreto: {numero_secreto}")
       st.snow() 
    else:
       st.error(f'Infelizmente você Errou! O código era:{numero_secreto}! Tente novamente!')