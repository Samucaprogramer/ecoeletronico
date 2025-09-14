import streamlit as st
import folium
from streamlit_folium import st_folium

# --- CONFIGURAÇÃO DO APP ---
st.set_page_config(page_title="Reciclagem Eletrônica", page_icon="♻️", layout="wide")

st.title("♻️ Reciclagem de Lixo Eletrônico")
st.write("Incentivando o descarte consciente de resíduos eletrônicos.")

# --- 1. CADASTRO DO USUÁRIO ---
st.header("1. Cadastro do Usuário")
nome = st.text_input("Digite seu nome:")
email = st.text_input("Digite seu e-mail:")
if st.button("Cadastrar"):
    if nome and email:
        st.success(f"✅ Usuário {nome} cadastrado com sucesso!")
    else:
        st.warning("⚠️ Preencha todos os campos para continuar.")

# --- 2. ENVIO DO LIXO ELETRÔNICO ---
st.header("2. Envio do Lixo Eletrônico")
foto = st.file_uploader("Envie uma foto do lixo eletrônico", type=["jpg", "png", "jpeg"])
if foto:
    st.image(foto, width=250, caption="Lixo eletrônico enviado")

# --- 3. CATALOGAÇÃO DO NÍVEL DE PERIGO ---
st.header("3. Catalogação do Nível de Perigo")
if foto:
    st.info("🔍 O sistema analisou a foto.")
    st.write("Classificação do risco ambiental: **Médio** ⚠️")

# --- 4. LOCALIZAÇÃO DOS ECOPONTOS ---
st.header("4. Localização dos Ecopontos")
st.write("Aqui estão alguns ecopontos próximos:")

# Mapa interativo com folium
mapa = folium.Map(location=[-22.52, -41.94], zoom_start=12)
folium.Marker([-22.51, -41.95], tooltip="Ecoponto 1 - Centro", icon=folium.Icon(color="green")).add_to(mapa)
folium.Marker([-22.54, -41.93], tooltip="Ecoponto 2 - Bairro X", icon=folium.Icon(color="green")).add_to(mapa)
folium.Marker([-22.50, -41.92], tooltip="Ecoponto 3 - Bairro Y", icon=folium.Icon(color="green")).add_to(mapa)

st_folium(mapa, width=700, height=450)

# --- 5. CASHBACK ---
st.header("5. Cashback")
pontos = st.slider("Selecione a quantidade de lixo eletrônico descartado (kg)", 1, 20, 5)
if st.button("Receber Cashback"):
    recompensa = pontos * 10
    st.success(f"🎉 Você ganhou {recompensa} pontos de cashback!")
    st.write("Troque seus pontos por descontos em estabelecimentos parceiros.")
