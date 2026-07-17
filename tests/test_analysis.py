import pandas as pd
import pytest
import os

@pytest.fixture
def df():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    csv_path = os.path.join(base_dir, "customer_shopping_behavior.csv")
    return pd.read_csv(csv_path)

def test_data_loads(df):
    assert len(df) > 0, "CSV is empty"

def test_required_columns(df):
    required = ["Customer ID", "Age", "Gender",
                "Category", "Purchase Amount (USD)"]
    for col in required:
        assert col in df.columns, f"Missing column: {col}"

def test_no_null_customer_id(df):
    assert df["Customer ID"].isnull().sum() == 0

def test_purchase_amount_positive(df):
    assert (df["Purchase Amount (USD)"] > 0).all()

def test_age_range(df):
    assert df["Age"].min() >= 0
    assert df["Age"].max() <= 120