import streamlit as st


st.set_page_config(
    page_title="U.S. Gun Violence Analysis",
    page_icon="🇺🇸",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"About": """*Authors*:  Joel Sole and Nathaniel Mitrani\n"""}
)

st.title('Analysis of the evolution of the Mass Shootings in the U.S. across its different areas')

final_vis_path = 'final_vis.html'

st.components.v1.html(open(final_vis_path, 'r').read(), height=800, scrolling=True)
