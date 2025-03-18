import streamlit as st
from datetime import datetime, timedelta
from black_scholes_model import BlackScholesModel

today = datetime.today().date()
tomorrow = today + timedelta(days=1)
one_year_fowards = today + timedelta(days=365)


# Config browser tab style.
st.set_page_config(
    page_title="Black-Scholes Options Pricing Model",
    page_icon="📊",
    layout="wide"
)

st.title("Black-Scholes Options Pricing Model")
st.divider()

st.subheader("Inputs")
inputs_col1, inputs_col2 = st.columns(2)

with inputs_col1:
    # Get inputs from user.
    asset_price = st.number_input("Current Asset Price", min_value=0.00, value=100.00, step=0.01)
    strike_price = st.number_input("Strike Price", min_value=0.00, value=100.00, step=0.01)
    years_until_maturity = st.number_input("Years Until Maturity", min_value=0.00, value=2.00, step=0.01)

with inputs_col2:
    # Get inputs from user.
    interest_rate = st.number_input("Annual Risk-Free Interest Rate (%)", min_value=1.00, value=2.5, step=0.01)
    volatility = st.number_input("Volatility (%)", min_value=0.0, max_value=100.0, value=30.0, step=0.1)


# Calculate call and put value.
model = BlackScholesModel(asset_price, strike_price, interest_rate, years_until_maturity, volatility)
call_price = model.calculate_call_value()
put_price = model.calculate_put_value()


st.divider()
outputs_col1, outputs_col2 = st.columns(2)

with outputs_col1:
    st.success(f"Call Value: ****{call_price}****")


with outputs_col2:
    st.error(f"Call Value: ****{put_price}****")