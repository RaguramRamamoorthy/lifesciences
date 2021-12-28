import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.title("LIFE SCIENCES")
st.write("by RaguRam")

def load_lottieurl(url: str):

    r = requests.get(url)

    if r.status_code != 200:

        return None

    return r.json()

lottie_lifesciences = load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_vtuepexz.json')

st_lottie(lottie_lifesciences, height=200)