import pandas as pd
import numpy as np


"""
1. Load raw data
"""
data_path = "C:/Users/HP/PycharmProjects/V_C_PhD/Specific Objective 2/_Data/"
data_filename = "all_data_v1.csv"
both = data_path + data_filename
data = pd.read_csv(both)


"""
2. Impute missing data
"""


def impute_missing_data():
    quantitative_columns = ['v215', 'v216']
    qualitative_columns = [
        'v341', 'v370', 'v371', 'v372', 'v377', 'v378',
        'v379', 'v382', 'v398']
    for col in quantitative_columns:
        data[col] = np.where(
            data[col] < 40000, np.random.randint(
                50000, 700001), data[col])
        data[col].fillna(np.random.randint(
            50000, 700001), inplace=True)
    for col in qualitative_columns:
        data[col].fillna(
            np.random.choice([0, 1]), inplace=True)

    """save the data"""
    filename = 'data_os2.csv'
    both2 = data_path + filename
    data.to_csv(
        both2, index_label=False, index=False)


impute_missing_data()
