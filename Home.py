import pandas as pd
import streamlit as st

st.set_page_config(page_title="EC Dashboard", page_icon="📊", layout="wide")

st.title("EC Dashboard")


@st.cache_data
def load_data():
    orders = pd.read_csv("sample_data/orders.csv", parse_dates=["created_at"])
    users = pd.read_csv("sample_data/users.csv", parse_dates=["created_at"])
    return orders, users


orders, users = load_data()

col1, col2, col3 = st.columns(3)
col1.metric("注文数", f"{len(orders):,}")
col2.metric("販売額 (USD)", f"${orders['sale_price'].sum():,.0f}")
col3.metric("ユーザー数", f"{len(users):,}")

st.subheader("注文データ (orders.csv)")
st.dataframe(orders.head(50))

st.subheader("ユーザーデータ (users.csv)")
st.dataframe(users.head(50))
