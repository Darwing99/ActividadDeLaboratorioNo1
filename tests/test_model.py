import sys
sys.path.append(".")

from src.data.loader import load_raw_data
from src.features.engineering import add_salary_range, add_salary_zscore


def test_salary_range_feature():
    df = load_raw_data()
    df = add_salary_range(df)
    assert "Rango_Salarial" in df.columns
    assert df["Rango_Salarial"].isnull().sum() == 0
    print("OK - Feature Rango_Salarial")


def test_zscore_feature():
    df = load_raw_data()
    df = add_salary_zscore(df)
    assert "Salario_ZScore" in df.columns
    assert abs(df["Salario_ZScore"].mean()) < 0.01
    print("OK - Feature Salario_ZScore")


if __name__ == "__main__":
    test_salary_range_feature()
    test_zscore_feature()
    print("\nTodos los tests de features pasaron.")
