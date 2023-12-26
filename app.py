import streamlit as st
import numpy as np
from model import generate

st.set_page_config(
    page_title='Генерация отчёта для курсовой научно-исследовательской работы',
    initial_sidebar_state="expanded",
)

st.markdown("""
    <style>
    .separator {
        height: 4px;
        background-color: #000000;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

st.title('Генерация отчёта для курсовой научно-исследовательской работы')

st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

textInput = st.text_area('ЗАПРОС:', '',height=300, key='example_text')
btn = st.button("Сгенерировать отчёт")
if btn:
    container = st.container()
    header = container.empty()
    header.write("Генерация...")
    response = generate(textInput)
    st.info(response)
    header.write("Генерация завершена!")