import streamlit as st

# Page Setup
st.set_page_config(
    page_title="Housing Calculations",
    page_icon=":material/functions:",
    layout="wide",
)

# Sidebar Styling 
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Content
with st.sidebar:
    st.title("Inputs/Variables")

    with st.container(border=True):
        st.subheader("Basic House Info")

        current_house_price = st.number_input("House Price ($)", min_value=0, value=600000, step=1000, format="%i", key="hp")
        cbr_annual_growth_rate = st.number_input("Canberra Annual Growth Rate (%)", min_value=0.0, value=4.17, step=0.01, format="%.2f", key="cagr", help="Based on historical data from 2010 to 2025, averaged out. Source: Allhomes ACT Real Estate Market Trends Report.")
        deposit_percentage = st.number_input("Deposit Percentage (%)", min_value=0.0, value=10.0, step=0.1, format="%.2f", key="dp")
        loan_interest_rate = st.number_input("Loan Interest Rate (%)", min_value=0.0, value=6.04, step=0.01, format="%.2f", key="lir", help="This would change depending on deposit amount see assumptions for how we do variations with differing deposits.")
        loan_term_years = st.slider("Loan Term (Years)", min_value=5, max_value=30, value=30, step=1, format="%i", key="lty")

    with st.container(border=True):
        st.subheader("Upfront Costs")

        conveyancer_fee = st.number_input("Conveyancer Fee ($)", min_value=0, value=2500, step=10, format="%i", key="cf")
        mortgage_registration_fee = st.number_input("Mortgage Registration Fee ($)", min_value=0, value=200, step=10, format="%i", key="mrf")
        misc_expenses = st.number_input("Miscellaneous Expenses ($)", min_value=0, value=3000, step=10, format="%i", key="me", help="E.g. pest and building inspections, loan application fees, moving costs etc.")
        stamp_duty = st.number_input("Stamp Duty ($)", min_value=0, value=0, step=10, format="%i", key="sd", help="Waived for first home buyers in ACT if purchase price is below $1M.")
        lenders_mortgage_insurance = st.number_input("Lender's Mortgage Insurance ($)", min_value=0, value=0, step=10, format="%i", key="lmi", help="Only applicable if deposit is less than 20% or not first home buyer.")

    with st.container(border=True):
        st.subheader("Ongoing Costs")
        st.write("Town House")

        strata_fees_th = st.number_input("Strata Fees ($/year)", min_value=0, value=2500, step=10, format="%i", key="sfth")
        council_rates_th = st.number_input("Council Rates ($/year)", min_value=0, value=2000, step=10, format="%i", key="crth")
        contents_insurance_th = st.number_input("Contents Insurance ($/year)", min_value=0, value=500, step=10, format="%i", key="hcith", help="Building insurance is included in strata fees.")

        st.write("House")

        council_rates_h = st.number_input("Council Rates ($/year)", min_value=0, value=2500, step=10, format="%i", key="crh")
        building_insurance_h = st.number_input("Building Insurance ($/year)", min_value=0, value=1000, step=10, format="%i", key="bh")
        contents_insurance_h = st.number_input("Contents Insurance ($/year)", min_value=0, value=500, step=10, format="%i", key="cinh")


# Tabs Setup
tab1, tab2, tab3 = st.tabs(["Individual", "Variations", "Borrowing Power"])