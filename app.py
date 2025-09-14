import streamlit as st

st.title("♻️ Reciclagem de Lixo Eletrônico")

menu = ["Início", "Enviar Lixo Eletrônico", "Sobre"]
opcao = st.sidebar.selectbox("Menu", menu)

if opcao == "Início":
    st.write("Bem-vindo! Descubra como descartar seus resíduos eletrônicos corretamente.")

elif opcao == "Enviar Lixo Eletrônico":
    arquivo = st.file_uploader("Envie uma imagem", type=["png","jpg","jpeg"])
    if arquivo:
        st.image(arquivo, caption="Imagem enviada", use_column_width=True)
        st.success("Arquivo enviado com sucesso!")

elif opcao == "Sobre":
    st.write("App criado para incentivar a reciclagem de lixo eletrônico.")
