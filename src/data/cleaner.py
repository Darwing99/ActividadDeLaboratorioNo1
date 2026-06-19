import pandas as pd


def validate_quality(df):
    report = {
        "filas": len(df),
        "columnas": len(df.columns),
        "nulos": df.isnull().sum().to_dict(),
        "duplicados": df.duplicated().sum(),
    }
    return report


def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df
