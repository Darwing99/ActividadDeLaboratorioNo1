import pandas as pd
import yaml
from pathlib import Path


def load_config(config_path="config/config.yaml"):
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_raw_data(config=None):
    if config is None:
        config = load_config()
    path = config["paths"]["raw_data"]
    df = pd.read_excel(path)
    df.columns = df.columns.str.strip()
    return df


def save_processed_data(df, filename, config=None):
    if config is None:
        config = load_config()
    output_path = Path(config["paths"]["processed_data"]) / filename
    df.to_csv(output_path, index=False)
    print(f"Datos guardados en: {output_path}")
