# Escreva um programa que pergunte a quantidade de km percorrido por um carro e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60 reais por dia e O,15 por km rodado!

import streamlit as st

with st.sidebar:
    st.title("Preço do Alugel do Carro")
    st.header("Informações")

    st.write("Escreva um programa que pergunte a quantidade de km percorrido por um carro e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60,00 por dia e O,15 por km rodado!")

    st.image('carro.png')

st.title("Calcular")

carroKm = st.number_input("Insira a quantidade de Km percorridos:", min_value=0.0)
dias = st.number_input("Digite a quantidade de dias que o carro foi alugado:", min_value=0)

if st.button("Calcular"):
    calcularCarroKm = carroKm * 60
    calcularDias = dias * 0.15
    resultado = calcularCarroKm + calcularDias

    st.code(f'O preço sera de: {resultado:.2f}')

    col1, col2, col3 = st.columns(3)
    col1.metric('Valor por Km', f'R${calcularCarroKm:.2f}', f'{calcularCarroKm:.2f}', delta_color='normal')
    col2.metric('Valor por dia', f'R${calcularDias:.2f}', f'{calcularDias:.2f}', delta_color='normal')
    col3.metric('Valor total', f'R${resultado:.2f}', f'{resultado:.2f}', delta_color='normal')