# import streamlit as st

# # Aqui eu coloco o TÍTULO 
# st.title("Olá, Anny!")

# # Aqui cria o calendário
# date = st.date_input("Selecione uma Data")

# # Aqui permite upload do arquivo
# file = st.file_uplouader("Faça um uploud de um arquivo")
# # python -m streamlit run app.py

import streamlit as st
import pandas as pd

# python -m streamlit run app.py

# --------------------------------------------------------------------- Sidebar

st.sidebar.image("logo.png")
st.sidebar.title('Anny Exclusive Motors')

carros = ['Fiat UNO', 'Corsa', 'Fiat Strada', 'HB20', 'Onix', 'Fiat Toro', 'Corolla', 'Civic', 'Honda HR-V', 'SW4', 'Porsche 911', 'Lamborghini']

opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)

# --------------------------------------------------------------------- Principal
st.title('Car Future - Aluguel de Carros')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} será alugada?')
km = st.text_input(f'Quantos km você pretende rodar com o {opcao}?')

if opcao == 'Fiat UNO':
    diaria = 90

elif opcao == 'Corsa':
    diaria = 100

elif opcao == 'Fiat Strada':
    diaria = 130
    
elif opcao == 'HB20':
    diaria = 130

elif opcao == 'Onix':
    diaria = 150

elif opcao == 'Fiat Toro':
    diaria = 210

elif opcao == 'Corolla':
    diaria = 220

elif opcao == 'Civic':
    diaria = 220

elif opcao == 'Honda HR-V':
    diaria = 320

elif opcao == 'SW4':
    diaria = 440

elif opcao == 'Porsche 911':
    diaria = 3500

elif opcao == 'Lamborghini':
    diaria = 6500



if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')