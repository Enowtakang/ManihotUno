import pandas as pd


"""
1. Load raw data
"""
raw_data_path = "C:/Users/HP/PycharmProjects/V_C_PhD/Specific Objective 2/_Data/"
raw_data_filename = "raw_data.xlsx"
both = raw_data_path + raw_data_filename
raw_data = pd.read_excel(both, engine='openpyxl')
raw_data.columns = raw_data.columns.str.strip()

"""
2. Extract data for specific objective 2
    - Version 1 
"""


def extract_data_for_specific_objective_2():
    raw_data.rename(
        columns={
            "0.4a Region / Province": 'v6',
            "II.39b How much did you raise by selling the cassava cuttings (bag/kg/ trucks, etc)?": "v215",
            "II.40 How much did you raise from the selling of cassava root last cropping season?": "v216",
            "IV.1 What diseases and pests do you frequently see in your cassava fields?/3= Viral (CMD, CBSD)": "v341",
            "IV.9 What is the impact of the appearance of these symptoms (CMD) on cassava plants / yield? /1=Poor plant growth": "v370",
            "IV.9 What is the impact of the appearance of these symptoms (CMD) on cassava plants / yield? /2= Decrease in yield": "v371",
            "IV.9 What is the impact of the appearance of these symptoms (CMD) on cassava plants / yield? /3=Lack of healthy plant material": "v372",
            "IV.10 How do you react when your cassava plants show the symptoms shown in photo 2?/1= Removal of infected plants": "v377",
            "IV.10 How do you react when your cassava plants show the symptoms shown in photo 2?/2= Destruction of infected plants": "v378",
            "IV.10 How do you react when your cassava plants show the symptoms shown in photo 2?/3= Replacement of infected plants by healthy cuttings": "v379",
            "IV.10 How do you react when your cassava plants show the symptoms shown in photo 2?/6= Use of inputs": "v382",
            "IV.12 Are you experiencing difficulties in monitoring the fields on a regular basis?/4= Late appearance of symptoms": "v398"},
        inplace=True)

    """list of quantitative variables"""
    quantitative_variables = ['v6', 'v215', 'v216']

    """list of qualitative variables"""
    qualitative_variables = [
        'v341', 'v370', 'v371', 'v372',
        'v377', 'v378', 'v379', 'v382', 'v398']

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
    filename = 'all_data_v1.csv'
    both2 = raw_data_path + filename
    data.to_csv(
        both2, index_label=False, index=False)


extract_data_for_specific_objective_2()
