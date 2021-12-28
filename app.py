import streamlit as st
from apps import chap1
from multiapp import MultiApp

st.title("LIFE SCIENCES")
st.write("by RaguRam")


app = MultiApp()

st.markdown("""
This app summarises the book LifeSciences
""")

# Add all your application here
app.add_app("Chapter1", chap1.app)

# The main app
app.run()