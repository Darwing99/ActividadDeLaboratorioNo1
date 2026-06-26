import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


def plot_salary_by_cargo(df, save_path=None):
    avg = df.groupby("Cargo")["Salario"].mean().sort_values()
    fig, ax = plt.subplots(figsize=(10, 6))
    avg.plot(kind="barh", ax=ax, color="steelblue")
    ax.set_title("Salario Promedio por Cargo")
    ax.set_xlabel("Salario (USD)")
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path)
    return fig


def plot_salary_by_pais(df, save_path=None):
    avg = df.groupby("País")["Salario"].mean().sort_values()
    fig, ax = plt.subplots(figsize=(10, 6))
    avg.plot(kind="barh", ax=ax, color="seagreen")
    ax.set_title("Salario Promedio por País")
    ax.set_xlabel("Salario (USD)")
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path)
    return fig


def plot_salary_distribution(df, save_path=None):
    fig, ax = plt.subplots(figsize=(10, 5))
    df["Salario"].hist(bins=40, ax=ax, color="coral", edgecolor="white")
    ax.set_title("Distribución de Salarios")
    ax.set_xlabel("Salario (USD)")
    ax.set_ylabel("Frecuencia")
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path)
    return fig


def plot_employees_by_pais(df, save_path=None):
    empleados_pais = df["País"].value_counts()
    umbral = 0.03 * empleados_pais.sum()
    principales = empleados_pais[empleados_pais >= umbral].copy()
    otros_total = empleados_pais[empleados_pais < umbral].sum()
    if otros_total > 0:
        principales["Otros"] = otros_total

    colores = plt.cm.tab20.colors[: len(principales)]
    explode = [0.04] * len(principales)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(
        principales.values,
        labels=principales.index,
        autopct="%1.1f%%",
        colors=colores,
        explode=explode,
        startangle=140,
        pctdistance=0.82,
        textprops={"fontsize": 9},
    )
    ax.set_title("Distribución de Empleados por País")
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path)
    return fig
