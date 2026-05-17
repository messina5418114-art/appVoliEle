import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="✈️ Mia App Voli", layout="wide")
st.title("✈️ Mia App Voli Personale")

st.markdown("*Ricerca voli low cost*")

col1, col2 = st.columns(2)
with col1:
    origin = st.text_input("Partenza (es. ROM, MIL, FCO)", "ROM")
with col2:
    destination = st.text_input("Destinazione (es. PAR, LON, BCN)", "PAR")

dep_date = st.date_input("Data di partenza", datetime.today() + timedelta(days=30))

if st.button("🔍 Cerca Voli", type="primary"):
    # Costruisci URL Aviasales con i parametri
    aviasales_link = f"https://aviasales.tpx.gr/Y9PD2gJ6?origin={origin}&destination={destination}&depart_date={dep_date.strftime('%d.%m.%Y')}"
    st.markdown(f"[✈️ Clicca qui per cercare i voli su Aviasales]({aviasales_link})", unsafe_allow_html=True)
    st.success("✅ Reindirizzamento a Aviasales!")