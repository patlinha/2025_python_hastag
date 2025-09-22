import streamlit as st
from openai import OpenAI
# no terminal -> streamlit run nomeArquivo.py
# pip install openai
# https://platform.openai.com/settings/organization/api-keys

modelo = OpenAI(api_key="tokenOpenAI")

st.write("### Chatbot com IA") # formatação de texto com markdown

# session_state = memoria (local) do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# exibir histórico de msgs
for msg in st.session_state["lista_mensagens"]:
    role = msg["role"]
    texto = msg["content"]
    st.chat_message(role).write(texto)


msg_usuario = st.chat_input("Escreva sua msg aqui para IA responder")

if msg_usuario:
    st.chat_message("user").write(msg_usuario)
    msg = {"role":"user", "content": msg_usuario}
    st.session_state["lista_mensagens"].append(msg)

    # resposta IA
    resposta_modelo = modelo.chat.completions.create(
        messages = st.session_state["lista_mensagens"],
        model = "gpt-3.5-turbo"
    )

    resposta_ia = resposta_modelo.choices[0].message.content


    # exibir resposta IA na tela
    st.chat_message("assistant").write(resposta_ia)
    msg_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(msg_ia)

    #print(st.session_state["lista_mensagens"])
