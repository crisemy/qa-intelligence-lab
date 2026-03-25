import streamlit as st
import pandas as pd
import json

with open("../component-4-experiment-engine/dataset/experiments.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)

st.title("QA Intelligence Lab Dashboard")

st.write("Dataset Overview")
st.write(df.describe())

st.scatter_chart(
    df,
    x="latencyMs",
    y="errorRate"
)