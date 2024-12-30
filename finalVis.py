import altair as alt
import streamlit as st
import json
import pickle


st.set_page_config(
    page_title="U.S. Gun Violence Analysis",
    page_icon="🇺🇸",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"About": """*Authors*:  Joel Sole and Nathaniel Mitrani\n"""}
)

with open('final_vis.pkl', 'rb') as f:
    final_vis = pickle.load(f)

st.title('Analysis of the evolution of the Mass Shootings in the U.S. across its different areas')

st.altair_chart(final_vis, use_container_width=True)