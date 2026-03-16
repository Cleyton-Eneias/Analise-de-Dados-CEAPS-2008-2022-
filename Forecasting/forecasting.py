import pandas as pd
import streamlit as st
from prophet import Prophet
from prophet.plot import plot_plotly

df = pd.read_csv("E:\Analise-de-Dados-CEAPS-2008-2022--main\Analise-de-Dados-CEAPS-2008-2022--main\Forecasting\dataset_ceaps_forecasting.csv")

df["ds"] = pd.to_datetime(df["ds"])

model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)

fig = plot_plotly(model, forecast)

st.plotly_chart(fig, use_container_width=True)

