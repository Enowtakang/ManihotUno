import pandas as pd


"""
1. Load data
"""
# ptf = path to file
ptf = "C:/Users/HP/PycharmProjects/V_C_PhD/2Datasets/sp_obj_1/"
# fn is file name
fn = 'all_data_v1.csv'

data = pd.read_csv(ptf + fn)
# print(len(data))
# print(data.head())


"""
2. remove all rows with missing values
"""
data.dropna(inplace=True)
# print(len(data))


"""
3. remove all spaces between characters 
    in all categorical columns, then save the data
"""
qualitative_variables = [
        'v27', 'v31', 'v32', 'v48', 'v49',
        'v325', 'v495', 'v497', 'v499',
        'v501', 'v503', 'v512']


def remove_spaces_and_save_data():
    for variable in qualitative_variables:
        data[variable] = data[variable].str.replace(' ', '')
        data[variable] = data[variable].str.replace('  ', '')

    fn2 = 'all_data_v2.csv'
    data.to_csv(ptf + fn2, index=False, index_label=False)


# remove_spaces_and_save_data()
