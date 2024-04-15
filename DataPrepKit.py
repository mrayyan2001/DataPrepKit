import pandas as pd
import numpy as np


def read_data(file_name: str, file_type: str):
    if file_type.lower() == "csv":
        return pd.read_csv(file_name)
    elif file_type.lower() == "excel":
        return pd.read_excel(file_name)
    elif file_type.lower() == "json":
        return pd.read_json(file_name)
    else:
        raise ValueError("try one from these types: csv, excel, and json")


def summary(data_frame: pd.DataFrame):
    print(data_frame.describe())
    print("most freq\n", data_frame.mode())


def handle_missing_values(data_frame: pd.DataFrame, way: str, value=None):
    if way == "fill":
        if value == None:
            raise ValueError("Enter the value")
        data_frame.fillna(value, inplace=True)
    elif way == "drop":
        data_frame.dropna(inplace=True)
    else:
        raise ValueError("enter a correct way.")


def encoding(column: pd.Series):
    keys = column.unique()
    return column.apply(lambda x: np.where(keys == x)[0][0])
