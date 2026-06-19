import pandas as pd


def print_salary_stats(df):
    stats = {
        "Máximo": df["Salario"].max(),
        "Mínimo": df["Salario"].min(),
        "Promedio": round(df["Salario"].mean(), 2),
        "Mediana": df["Salario"].median(),
        "Desviación Estándar": round(df["Salario"].std(), 2),
    }
    for k, v in stats.items():
        print(f"{k}: {v}")
    return stats


def top_n(df, column, n=10, ascending=False):
    return df.sort_values(by=column, ascending=ascending).head(n)
