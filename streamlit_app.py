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

individual_calculations_page = st.Page(
    page="./views/individual_calculations_page.py",
    title="Individual Calculations",
    icon=":material/functions:"
)

variation_calculations_page = st.Page(
    page="./views/variation_calculations.py",
    title="Variation Calculations",
    icon=":material/functions:"
)

pg = st.navigation(
    {
        "Info":[about_page,info_assumptions_page],
        "Models":[individual_calculations_page, variation_calculations_page],
    }
)

pg.run()