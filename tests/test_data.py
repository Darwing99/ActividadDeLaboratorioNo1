import sys
sys.path.append(".")

from src.data.loader import load_raw_data
from src.data.cleaner import validate_quality, clean_data


def test_load_data():
    df = load_raw_data()
    assert df is not None
    assert len(df) > 0
    print("OK - Carga de datos")


def test_columns_exist():
    df = load_raw_data()
    required = ["Nombre", "Cargo", "Salario", "País"]
    for col in required:
        assert col in df.columns, f"Columna faltante: {col}"
    print("OK - Columnas requeridas presentes")


def test_no_nulls():
    df = load_raw_data()
    report = validate_quality(df)
    for col, nulls in report["nulos"].items():
        assert nulls == 0, f"Nulos encontrados en {col}: {nulls}"
    print("OK - Sin valores nulos")


def test_salary_positive():
    df = load_raw_data()
    assert (df["Salario"] > 0).all(), "Hay salarios negativos o cero"
    print("OK - Salarios positivos")


if __name__ == "__main__":
    test_load_data()
    test_columns_exist()
    test_no_nulls()
    test_salary_positive()
    print("\nTodos los tests pasaron.")
