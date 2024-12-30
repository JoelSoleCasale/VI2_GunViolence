import streamlit as st


st.set_page_config(
    page_title="U.S. Gun Violence Analysis",
    page_icon="🇺🇸",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"About": """*Authors*:  Joel Sole and Nathaniel Mitrani\n"""}
)

st.title('Analysis of the evolution of the Mass Shootings in the U.S. across its different areas')

final_vis = open('final_vis.html', 'r').read()

st.components.v1.html(final_vis, width=1500, height=820, scrolling=True)
