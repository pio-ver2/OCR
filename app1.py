import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# Estilo visual con fondo colorido y emojis
st.markdown("""
    <style>
        body {
            background-color: #002b36;  /* Fondo oscuro con un toque moderno */
            color: #ffffff;  /* Texto blanco */
        }
        .stTitle {
            color: #ff69b4;  /* Título con color rosado */
            font-size: 2em;
        }
        .stHeader {
            color: #ff6347;  /* Cabecera en color tomate */
        }
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            background-color: #4caf50;  /* Fondo verde para los campos de texto */
            color: white;  /* Texto en blanco */
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #ffa500;  /* Botones en color naranja */
            color: #002b36;  /* Texto oscuro en el botón */
            border-radius: 10px;
            font-size: 1em;
        }
        .stRadio>div>label {
            color: #ffeb3b;  /* Color amarillo para las opciones del radio */
        }
    </style>
""", unsafe_allow_html=True)

# Título principal con emojis
st.title(" Reconocimiento de Texto en Imágenes 📸")

# Instrucciones en el sidebar con emojis
with st.sidebar:
    st.subheader("✨ Ajustes para tu foto")
    filtro = st.radio("¿Quieres aplicar un filtro?", ('🖤 Con Filtro', '💛 Sin Filtro'))

# Captura de imagen desde la cámara
img_file_buffer = st.camera_input("📸 Toma una Foto para Analizar")

if img_file_buffer is not None:
    # Procesamiento de la imagen
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    # Aplicar filtro si el usuario lo selecciona
    if filtro == '🖤 Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)  # Filtro invertido (blanco/negro)
    else:
        cv2_img = cv2_img  # Sin filtro
    
    # Convertir la imagen a RGB para mostrarla correctamente en Streamlit
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    
    # Mostrar la imagen procesada
    st.image(img_rgb, caption="📷 Imagen Procesada", use_column_width=True)

    # Extraer texto con pytesseract
    text = pytesseract.image_to_string(img_rgb)
    
    # Mostrar el texto extraído
    if text.strip():  # Si hay texto extraído
        st.subheader(" Texto Reconocido:")
        st.write(text)
    else:
        st.warning(" No se pudo reconocer texto en la imagen. Intenta con otra imagen.")

