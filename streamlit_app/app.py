import streamlit as st
import pandas as pd
import snowflake.connector

st.set_page_config(page_title="Orders Analytics Dashboard", layout="wide")

st.title("📊 Orders Analytics Dashboard")
st.write("Real-time data from Snowflake Marts Layer")

@st.cache_resource
def init_connection():
    return snowflake.connector.connect(
        user=st.secrets["snowflake"]["user"],
        password=st.secrets["snowflake"]["password"],
        account=st.secrets["snowflake"]["account"],
        warehouse=st.secrets["snowflake"]["warehouse"],
        database=st.secrets["snowflake"]["database"],
        role="ACCOUNTADMIN"
    )

try:
    conn = init_connection()
    
    @st.cache_data(ttl=60)
    def run_query(query):
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetch_pandas_all()

    # الاستعلام المباشر من جدول fct_orders النهائي
    df = run_query("SELECT * FROM MY_DATABASE.RAW_MARTS.FCT_ORDERS;")

    st.sidebar.header("Filter Options")
    status_filter = st.sidebar.multiselect(
        "Select Order Status:",
        options=df["ORDER_STATUS"].unique(),
        default=df["ORDER_STATUS"].unique()
    )

    filtered_df = df[df["ORDER_STATUS"].isin(status_filter)]

    col1, col2 = st.columns(2)
    col1.metric("Total Orders", len(filtered_df))
    col2.metric("Total Revenue", f"${filtered_df['AMOUNT'].sum():,.2f}")

    st.subheader("Orders Amount Trend")
    st.line_chart(filtered_df.set_index("ORDER_DATE")["AMOUNT"])

    st.subheader("Filtered Marts Data")
    st.dataframe(filtered_df)

except Exception as e:
    st.error(f"Error connecting to Snowflake: {e}")
