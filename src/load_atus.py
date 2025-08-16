import pandas as pd
import os

def load_atus_data():
    data_path = os.path.join("..", "data", "atus", "atus_data_processed.csv")
    return pd.read_csv(data_path)

if __name__ == "__main__":
    df = load_atus_data()
    print(df.head())