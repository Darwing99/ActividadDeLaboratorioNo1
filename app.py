import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from src.data.loader import load_raw_data, load_config
from src.data.cleaner import clean_data, validate_quality
from src.visualization.plots import (
    plot_salary_by_cargo,
    plot_salary_by_pais,
    plot_salary_distribution,
    plot_employees_by_pais,
)

st.set_page_config(
    page_title="Análisis de Salarios Tecnológicos",
    page_icon="💼",
    layout="wide",
)

st.title(" Análisis Estratégico de Salarios Tecnológicos")
st.caption("Actividad de Laboratorio No. 1 — Darwing Rodilso Hernandez Castellanos")

@st.cache_data
def get_data():
    config = load_config()
    df = load_raw_data(config)
    df = clean_data(df)
    return df, config

try:
    df, config = get_data()
except FileNotFoundError:
    st.error("No se encontró el archivo de datos. Verifica que el Excel esté en `data/raw/`.")
    st.stop()

# ── Sidebar filtros ──────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Filtros")
    cargos_disp = sorted(df["Cargo"].unique())
    paises_disp = sorted(df["País"].unique())

    cargos_sel = st.multiselect("Cargo", cargos_disp, default=cargos_disp)
    paises_sel = st.multiselect("País", paises_disp, default=paises_disp)

df_f = df[df["Cargo"].isin(cargos_sel) & df["País"].isin(paises_sel)]

if df_f.empty:
    st.warning("No hay datos para los filtros seleccionados.")
    st.stop()

# ── KPIs ─────────────────────────────────────────────────────────────────────
st.subheader("Resumen Ejecutivo")
k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Empleados",       f"{len(df_f):,}")
k2.metric("Salario Máximo",  f"${df_f['Salario'].max():,.0f}")
k3.metric("Salario Mínimo",  f"${df_f['Salario'].min():,.0f}")
k4.metric("Promedio",        f"${df_f['Salario'].mean():,.0f}")
k5.metric("Mediana",         f"${df_f['Salario'].median():,.0f}")

st.divider()

# ── Gráficos ──────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("Salario Promedio por Cargo")
    st.pyplot(plot_salary_by_cargo(df_f))

with col2:
    st.subheader("Salario Promedio por País")
    st.pyplot(plot_salary_by_pais(df_f))

st.subheader("Distribución de Salarios")
st.pyplot(plot_salary_distribution(df_f))

col5, col6 = st.columns(2)
with col5:
    st.subheader("Empleados por País")
    st.pyplot(plot_employees_by_pais(df_f))

with col6:
    st.subheader("Estadísticas por Cargo")
    st.dataframe(
        df_f.groupby("Cargo")["Salario"]
        .agg(Promedio="mean", Maximo="max", Minimo="min", Empleados="count")
        .sort_values("Promedio", ascending=False)
        .style.format({"Promedio": "${:,.0f}", "Maximo": "${:,.0f}", "Minimo": "${:,.0f}"}),
        use_container_width=True,
    )

st.divider()

# ── Tablas ────────────────────────────────────────────────────────────────────
col3, col4 = st.columns(2)

with col3:
    st.subheader("Promedio por Cargo")
    tbl_cargo = (
        df_f.groupby("Cargo")["Salario"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
        .rename(columns={"Salario": "Salario Promedio"})
    )
    tbl_cargo["Salario Promedio"] = tbl_cargo["Salario Promedio"].map("${:,.2f}".format)
    st.dataframe(tbl_cargo, use_container_width=True, hide_index=True)

with col4:
    st.subheader("Promedio por País")
    tbl_pais = (
        df_f.groupby("País")["Salario"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
        .rename(columns={"Salario": "Salario Promedio"})
    )
    tbl_pais["Salario Promedio"] = tbl_pais["Salario Promedio"].map("${:,.2f}".format)
    st.dataframe(tbl_pais, use_container_width=True, hide_index=True)

st.divider()

# ── Calidad de datos ──────────────────────────────────────────────────────────
with st.expander("Reporte de calidad de datos"):
    report = validate_quality(df_f)
    st.json(report)
