import streamlit as st
import pandas as pd
import numpy as np

import pickle
from sklearn.neighbors import KNeighborsClassifier

model = pickle.load(open('model.pkl', 'rb'))

# Title
st.title('Prediksi Kelayakan Konsumsi Air untuk di konsumsi')
st.image('img.jpg', use_column_width=True)
st.write('Suatu kelayakan dari suatu air yang akan dikonsumsi berdasarkan dengan Tingkat keasaman air,  Kandungan mineral dalam air,  Kandungan padatan terlarut dalam air, Kandungan kloramina dalam air,  Kandungan sulfat dalam air,  Kandungan sulfat dalam air,  Kemampuan air untuk menghantarkan arus listrik,  Kandungan karbon organik dalam air,  Kandungan trihalometana dalam air,  Kekeruhan air akibat partikel-padatan yang mengambang di dalamnya ')
st.write('Untuk menguji kelayakan air maka silahkan isi form berikut: ')

col1, col2 = st.columns(2)

#inputan
# Input

ph = st.text_input("Tingkat keasaman air ( 0-14 )", key="ph")
Hardness = st.text_input("Kandungan mineral ( >=10 )", key="Hardness")
Solids = st.text_input("Kandungan padatan terlarut ( >=0 )", key="Solids")
Chloramines = st.text_input("Kandungan kloramina ( 0-14 )", key="Chloramines")
Sulfate = st.text_input("Kandungan sulfat ( 0-1000 )", key="Sulfate")
Conductivity = st.text_input("Kemampuan air untuk menghantarkan arus listrik ( 0-800 )", key="Conductivity")
Organic_carbon = st.text_input("Kandungan karbon organik ( 0-30 )", key="Organic_carbon")
Trihalomethanes = st.text_input("Kandungan trihalometana ( 0-125 )", key="Trihalomethanes")
Turbidity = st.text_input("Kekeruhan air  ( 0-7 )", key="Turbidity")

# Prediksi
pred_potability = ''

# Tombol untuk prediksi
if st.button('Prediksi'):
    # Konversi nilai input ke tipe numerik
    ph = float(ph)
    Hardness = float(Hardness)
    Solids = float(Solids)
    Chloramines = float(Chloramines)
    Sulfate = float(Sulfate)
    Conductivity = float(Conductivity)
    Organic_carbon = float(Organic_carbon)
    Trihalomethanes = float(Trihalomethanes)
    Turbidity = float(Turbidity)

    # Lakukan prediksi
    pred_potability = model.predict([[ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]])

    if pred_potability == 1:
        st.success('Air Layak untuk Dikonsumsi')
    else:
        st.error('Air Tidak Layak untuk Dikonsumsi')