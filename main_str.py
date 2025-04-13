import os
import openai
import streamlit as st

# Leer la API key y quitar saltos de línea
with open("api_key.txt") as archivo:
    openai.api_key = archivo.readline()

# Inicialización de la sesión: cargar productos y reglas y setear el contexto
if "contexto" not in st.session_state:
    with open("productos_tecnofil.csv") as archivo:
        producto_csv = archivo.read()
    with open("reglas2.txt") as archivo:
        reglas = archivo.readline()  # lee todo el contenido de reglas

    st.session_state.contexto = [
        {'role': 'system', 'content': f"{reglas} {producto_csv}"}
    ]

# Función para enviar mensajes al modelo de OpenAI
def enviar_mensaje(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content

# Título y bienvenida en la interfaz de Streamlit
st.title("Chat de TecnoAI 🤖")
st.markdown("**¡Bienvenido a TecnoAI!**")
st.write("¿Qué necesitas saber hoy? Escribe tu pregunta en el campo de entrada y presiona **Enviar** para comenzar.")

# Entrada de mensaje del usuario
mensaje = st.text_input("Ingresa tu mensaje:")

# Botón para enviar el mensaje
if st.button("Enviar"):
    if mensaje:
        st.session_state.contexto.append({'role': 'user', 'content': mensaje})
        respuesta = enviar_mensaje(st.session_state.contexto)
        st.session_state.contexto.append({'role': 'assistant', 'content': respuesta})
        st.success(f"**Asistente:** {respuesta}")
    else:
        st.warning("Por favor, escribe un mensaje antes de enviar.")

# Mostrar historial de conversación (omitiendo el primer mensaje de sistema)
st.subheader("Historial de conversación:")
for chat in st.session_state.contexto[1:]:
    if chat['role'] == 'user':
        st.markdown(f"**Usuario:** {chat['content']}")
    elif chat['role'] == 'assistant':
        st.markdown(f"**Asistente:** {chat['content']}")
