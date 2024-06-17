import pandas as pd


"""
1. Load data
"""
data_path = "path/to/file"
data_filename = "2_all_Data_OS2.csv"
both = data_path + data_filename
data = pd.read_csv(both)


"""
2. 'make data subsets' function
"""
pdi_variables = ["v339", "v340", "v341", "v342", "v343"]

cos_variables = [
    "v352", "v353", "v354", "v355", "v356", "v357"]

iccp_variables = ["v370", "v371", "v372", "v373", ]

reactions_variables = [
    "v377", "v378", "v379", "v380", "v381", "v382", "v383", ]

dp_variables = ["v387", "v388", "v389", "v390", "v391"]

opinions_variables = [
    "v412", "v413", "v414", "v415", "v416", "v417",
    "v418", "v419", "v420", "v421", "v422", "v423",
    "v424", "v425", "v426", "v427", "v428", "v429",
    "v430", "v431", "v432", "v433", "v434", "v435",
    "v436"]


def make_data_subset(columns, filename):
    filepath = data_path + filename
    data[columns].to_csv(
        filepath, index=False, index_label=False)


"""
3. Make data subsets
"""
make_data_subset(
    pdi_variables,
    '3a_pests_and_diseases_identification.csv')

make_data_subset(
    cos_variables,
    '3b_causes_of_symptoms.csv')

make_data_subset(
    iccp_variables,
    '3c_impact_of_CMD_on_cassava_plants.csv')

make_data_subset(
    reactions_variables,
    '3d_reactions_to_CMD_symptoms.csv')

make_data_subset(
    dp_variables,
    '3e_CMD_prevention.csv')

make_data_subset(
    opinions_variables,
    '3f_farmers_opinions_on_CMD_and_its_management.csv')
