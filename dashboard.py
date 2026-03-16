import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Dashboard CEAPS",
    layout="wide"
)


st.title("📊 Dashboard de Gastos dos Senadores (CEAPS)")

df = pd.read_csv("ceaps_limpo.csv", sep=",")

# =============================
# MÉTRICAS
# =============================

total_gasto = df["VALOR_REEMBOLSADO"].sum()
total_senadores = df["SENADOR"].nunique()
total_registros = len(df)

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total de Gastos", f"R$ {total_gasto:,.2f}")
col2.metric("👤 Total de Senadores", total_senadores)
col3.metric("📄 Registros de Despesas", total_registros)

st.divider()

# =============================
# TOP 10 SENADORES            
# =============================

top_senadores = (
    df.groupby("SENADOR")["VALOR_REEMBOLSADO"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig1 = px.bar(
    top_senadores,
    x="SENADOR",
    y="VALOR_REEMBOLSADO",
    title="Top 10 Senadores com Maiores Gastos",
    color="SENADOR"
)

st.plotly_chart(fig1, use_container_width=True)

# =============================
# GASTOS POR TIPO DE DESPESA
# =============================

gastos_tipo = (
    df.groupby("TIPO_DESPESA")["VALOR_REEMBOLSADO"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig2 = px.pie(
    gastos_tipo,
    names="TIPO_DESPESA",
    values="VALOR_REEMBOLSADO",
    title="Distribuição dos Gastos por Tipo",
    height=600
)

fig2.update_layout(
    legend=dict(
        orientation="h",
        y=-0.2
    )
)

fig2.update_layout(
    margin=dict(t=25, b=0, l=0, r=0),
    height=400
)

fig2.update_traces(
    textposition='inside',
    textfont_size=14
)

st.plotly_chart(fig2, use_container_width=True)

# =============================
# GASTOS POR ANO
# =============================

gastos_ano = df.groupby("ANO")["VALOR_REEMBOLSADO"].sum().reset_index()

fig3 = px.line(
    gastos_ano,
    x="ANO",
    y="VALOR_REEMBOLSADO",
    title="Evolução dos Gastos ao Longo dos Anos"
)

st.plotly_chart(fig3, use_container_width=True)