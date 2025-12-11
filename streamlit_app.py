import streamlit as st

# Page Setup

about_page = st.Page(
    page="./views/about_page.py",
    title="About Page",
    icon=":material/person:",
    default=True
)

info_assumptions_page = st.Page(
    page="./views/info_assumptions_page.py",
    title="Information & Assumptions",
    icon=":material/book_ribbon:"
)

calculations_page = st.Page(
    page="./views/calculations_page.py",
    title="Calculations",
    icon=":material/functions:"
)

pg = st.navigation(
    {
        "Info":[about_page,info_assumptions_page],
        "Models":[calculations_page],
    }
)

pg.run()