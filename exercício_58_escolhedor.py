

##Importando a biblioteca

import streamlit as st ##importando como st para facilitar a digitação

st.title('Escolhedor de janta')#título do nosso aplicativo

#criar abas

aba1, aba2 = st.tabs(["simples", "N valores"])

with aba1:
    #colocar tudo que esta dentro da aba1 com um "tab" pra dentro
    opcao1 = st.text_input('insira a opção 1:')
    opcao2 = st.text_input('insira a opção 2:')
    opcao3 = st.text_input('insira a opção 3:')

    #importar uma biblioteca que trabalha com valores aleatórios

    import random

    if st.button ("escolher"):
        lista_de_opcoes = [opcao1, opcao2, opcao3]
        escolha_final = random.choice(lista_de_opcoes)
        st.markdown ("## Sua escolha foi...")
        st.markdown (f"# :blue[{escolha_final}]")

    #para rodar o código, clicar no terminal no canto esquedo inferior e escrever:
    #streamlit run exercício_58_escolhedor.py


with aba2:
    if "lista_n_opcoes" not in st.session_state:
        st.session_state.lista_n_opcoes = []

    st.markdown (f"## Opções: {st.session_state.lista_n_opcoes}")

    nova_opcao = st.text_input('Insira uma nova opção:')
    if st.button("Inserir opção"):
        st.session_state.lista_n_opcoes.append(nova_opcao)
        st.rerun#atualizar a tela

    if st.button('Apagar lista'):
        st.session_state.lista_n_opcoes.clear()
        st.rerun

    import time

    if st.button ("Escolher"):
        with st.spinner("escolhendo"):
            time.sleep(3)
            escolha_final2 = random.choice(st.session_state.lista_n_opcoes)
            st.markdown("## Sua escolha foi...")
            st.markdown(f"# :blue[{escolha_final2}]")


##-----------------Criando uma função para "unir" os botões de escolha

# def faz_a_escolha(lista):
    #scolha_final2 = random.choice(lista)
    #st.markdown("## Sua escolha foi...")
    #st.markdown(f"# :blue[{escolha_final2}]")

#    if st.button ("escolher"):
#       lista_de_opcoes = [opcao1, opcao2, opcao3]
#       faz_a_escolha = (lista_de_opcoes)

#    if st.button ("Escolher"):
#        faz_a_escolha = (st.session_state.lista_n_opcoes)
#-------------------------------FIM
