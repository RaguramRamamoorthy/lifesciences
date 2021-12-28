import streamlit as st
from streamlit_lottie import st_lottie
import requests

from apps import chap1, chap2
from multiapp import MultiApp

st.title("LIFE SCIENCES")
st.write("by RaguRam")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_lifesciences = load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_vtuepexz.json')
st_lottie(lottie_lifesciences, height=200)

app = MultiApp()

# Add all your application here
app.add_app("chapter1", chap1.app)
app.add_app("chapter2", chap2.app)

# The main app
app.run()
