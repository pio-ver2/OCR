import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image


st.markdown("""
    <style>
        body {
            background-color: #1e2a47;  /* Fondo azul oscuro */
            color: #ffffff;  /* Texto en color blanco */
        }
        .stTitle {
            color: #f4a261;  /* Título en color cálido */
        }
        .stHeader {
            color: #ffb703;  /* Cabecera en tono dorado */
        }
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            background-color: #4c6a92;  /* Fondo de los campos de texto */
            color: white;  /* Texto en los campos de texto en blanco */
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #ffb703;  /* Color amarillo en los botones */
            color: #1e2a47;  /* Texto oscuro en el botón */
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)


st.title("Reconocimiento óptico de Caracteres")


with st.sidebar:
    st.subheader("Ajustes de la imagen")
    filtro = st.radio("Aplicar filtro", ('Con Filtro', 'Sin Filtro'))


img_file_buffer = st.camera_input("Toma una Foto de una Medusa")

if img_file_buffer is not None:
    
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    
    if filtro == 'Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img) 
    else:
        cv2_img = cv2_img  
    
    
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    
    
    st.image(img_rgb, caption="Imagen Procesada", use_column_width=True)

    
    text = pytesseract.image_to_string(img_rgb)
    
    
    if text.strip():  
        st.subheader("Texto Reconocido:")
        st.write(text)
    else:
        st.warning("No se pudo reconocer texto en la imagen. Intenta con otra imagen.")


    


