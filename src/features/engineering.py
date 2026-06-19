import pandas as pd
import yaml


def add_salary_range(df, config=None):
    if config:
        bins = config["analysis"]["salary_bins"]
        labels = config["analysis"]["salary_labels"]
    else:
        bins = [0, 30000, 60000, 90000, 120000, 999999]
        labels = ["Muy Bajo", "Bajo", "Medio", "Alto", "Muy Alto"]

    df["Rango_Salarial"] = pd.cut(df["Salario"], bins=bins, labels=labels)
    return df


def add_salary_zscore(df):
    mean = df["Salario"].mean()
    std = df["Salario"].std()
    df["Salario_ZScore"] = (df["Salario"] - mean) / std
    return df
