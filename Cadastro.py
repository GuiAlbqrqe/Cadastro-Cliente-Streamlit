import streamlit as st
import pandas as pd
from datetime import date


def gravar_dados(nome, cep, endereco, numero_casa, ponto_referencia, email, data_nasc, tipo):
    if nome and data_nasc <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(
                f'"{nome}";"{cep}";"{endereco}";"{numero_casa}";"{ponto_referencia}";"{email}";"{data_nasc}";"{tipo}"\n')
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False


st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon="📙",
    layout="wide"
)

st.title("Cadastro de clientes")
col1, col2 = st.columns(2)
st.divider()

with col1:
    nome = st.text_input("Nome do cliente", placeholder="Digite o nome do Cliente",
                         key="nome_cliente")

    dt_nasc = st.date_input("Data Nascimento", value=None, min_value=date(
        1900, 1, 1), max_value=date.today(), format="DD/MM/YYYY")

    email = st.text_input("E-mail do Cliente", placeholder="Digite o E-mail do Cliente",
                          key="email_cliente")

    cep = st.text_input("CEP do Cliente", placeholder="Digite o CEP do Cliente",
                        key="cep_cliente")

with col2:

    endereco = st.text_input("Endereço do Cliente", placeholder="Digite o Endereço do Cliente",
                             key="endereco_cliente")

    numero_casa = st.text_input("Número da Residência e Tipo de Endereço", placeholder="Digite o Número e Tipo",
                                key="numero_casa")

    ponto_referencia = st.text_input("Ponto de Referência", placeholder="Digite um Ponto de Referência",
                                     key="pronto_referencia")

    tipo = st.selectbox("Tipo do Cliente",
                        ("Pessoa Jurídica", "Pessoa Física"), index=None, placeholder="Pessoa Física ou Jurídica?", key="tipo_cliente")

btn_cadastrar = st.button("Cadastrar",
                          on_click=gravar_dados,
                          args=[nome, cep, endereco, numero_casa, ponto_referencia, email, dt_nasc, tipo])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!",
                   icon="✅")

    else:
        st.error("Houve algum proglema no cadastro!",
                 icon="❌")
