import pandas as pd


"""
1. Load raw data
"""
# prd = path_raw_data
prd = "C:/Users/HP/PycharmProjects/V_C_PhD/2Datasets/"
# frdwc = file_raw_data_with_columns
frdwc = 'raw_data_with_columns.csv'
both = prd + frdwc
raw_data = pd.read_csv(both)
# print(raw_data.head())

"""
2. Create GPS Data subset
"""


def extract_gps_data():
    columns = [
        'Latitude hemisphere',
        'Degrees - latitude',
        'Longitude hemisphere',
        'Degrees - longitude',
        'GPS COORDINATE',
        '_GPS COORDINATE_latitude',
        '_GPS COORDINATE_longitude',
        '_GPS COORDINATE_altitude',
        '_GPS COORDINATE_precision',
        '0.4c Village'
    ]
    # fn = file_name
    fn = 'gps_data.csv'
    raw_data[columns].to_csv(
        prd + fn, index=False, index_label=False)


# extract_gps_data()


"""
3. Extract data for specific objective 1
    - Version 1
"""


def extract_data_for_specific_objective_1():
    # code the selected questions
    raw_data.rename(
        columns={
            '0.4a Region / Province': 'v6',
            'I.4 How old are you?': 'v28',
            'I.9 How many members of your household are actively involved in farming?': 'v41',
            'II.4 What is the total area of land owned?(ha)(english unit)': 'v72',
            'II.8 What area is sown to cassava?(ha)(English Unit)': 'v82',

            # "I.1 Are you the head of the household?": 'v24',
            "I.3 Sex of respondent": 'v27',
            "I.7a Are you able to read and write correctly?": 'v31',
            "I.7b What is your highest level of education?": 'v32',
            "I. 12 Do you have your own smartphone?": 'v48',
            "I. 13 Do you have access to internet ?": 'v49',
            # "III.1a In the context of cassava production, are you supervised by an agricultural service?": 'v244',
            "III.21. Do you belong to a farmers' association?": 'v325',
            "VII.1 Did you consume some of the cassava harvested during the previous season?": 'v495',
            "VII.3 Does the income from cassava contribute to the household's other food costs?": 'v497',
            "VII.5 Does the income from cassava help to cover your household's health needs?": 'v499',
            'VII.7 Does the income from cassava help to cover the schooling needs of the members of your household?': 'v501',
            'VII.9 Do you take part in community activities?': 'v503',
            'VII.12 Over the last five years, have you acquired any assets from your cassava income?': 'v512'},
        inplace=True)

    """list of quantitative variables"""
    quantitative_variables = [
        'v6', 'v28', 'v41', 'v72', 'v82']

    """list of qualitative variables"""
    qualitative_variables = [
        'v27', 'v31', 'v32', 'v48', 'v49',
        'v325', 'v495', 'v497', 'v499',
        'v501', 'v503', 'v512']

    """extract selected variables"""
    data = raw_data[
        quantitative_variables + qualitative_variables]

    """convert data in 'v6' to lowercase"""
    data['v6'] = data['v6'].str.lower()
    # print(data.head())
    # print('Yes', len(data))

    """select only rows which contain selected regions"""
    regions = ['adamaoua', 'centre', 'est', 'sud']
    data = data[data['v6'].isin(regions)]
    # print('Yes', len(data))

    """save the data subset"""
    # ptf = path to file
    ptf = "C:/Users/HP/PycharmProjects/V_C_PhD/2Datasets/sp_obj_1/"
    # fn is file name
    fn = 'all_data_v1.csv'
    data.to_csv(
        ptf + fn, index_label=False, index=False)


# extract_data_for_specific_objective_1()


"""
4. 
"""
