import streamlit as st
import pandas as pd

FILE_SLEEP = "청소년.xlsx"

@st.cache_data
def load_sleep():
    raw = pd.read_excel(FILE_SLEEP, sheet_name="데이터", header=None)

    df = raw.iloc[2:].copy()
    df.columns = [
        "시점","수면_전체","수면_남","수면_여",
        "건강인지_전체","건강인지_남","건강인지_여"
    ]

    df["시점"] = pd.to_numeric(df["시점"], errors="coerce")
    df = df.dropna(subset=["시점"])
    df["시점"] = df["시점"].astype(int)

    for c in df.columns[1:]:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    return df.reset_index(drop=True)

sleep_df = load_sleep()

st.title("🌙 수면 & 건강인지율 분석")
