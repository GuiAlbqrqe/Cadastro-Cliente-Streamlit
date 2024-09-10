import streamlit as st
import pandas as pd

dados = pd.read_csv("clientes.csv", sep=";", header=0,dtype={"CEP": str})

dados['Data de Nascimento'] = pd.to_datetime(dados['Data de Nascimento']).dt.strftime('%d/%m/%Y')

num_linhas = len(dados)
altura = min(400 + (num_linhas * 35), 800)

st.title("Clientes Cadastrados")
st.divider()

st.dataframe(dados, height=altura)