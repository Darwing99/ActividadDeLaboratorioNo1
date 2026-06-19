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
