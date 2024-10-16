import streamlit as st

# Dados de exemplo
vendas_atual = 120
vendas_anterior = 100
delta_vendas = vendas_atual - vendas_anterior

# Determinação da cor do delta
delta_color = "normal" if delta_vendas > 0 else "inverse"

# Título da aplicação
st.title("Relatório de Vendas")

# Exibindo a métrica
st.metric(
    label="Vendas deste mês",
    value=vendas_atual,
    delta=delta_vendas,
    delta_color=delta_color,
    help="Comparação com o mês anterior",
    label_visibility="visible"  # Ou "hidden" para ocultar o rótulo
)