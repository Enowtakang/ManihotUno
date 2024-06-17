import pandas as pd
import numpy as np


"""
1. Load raw data
"""
data_path = "path/to/file"
data_filename = "1extractedData.csv"
both = data_path + data_filename
data = pd.read_csv(both)


"""
2. Impute missing data
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

o_1_variables = pdi_variables + cos_variables + iccp_variables + reactions_variables + dp_variables


def random_imputations():
    for col in o_1_variables:
        data[col].fillna(
            np.random.choice([0, 1]), inplace=True)

    choices = ["1=Disagree", "2=Don't know", "3=Agree"]

    for col2 in opinions_variables:
        data[col2].fillna(
            np.random.choice(choices), inplace=True)

    """save the data"""
    filename = '2_all_Data_OS2.csv'
    both2 = data_path + filename
    data.to_csv(
        both2, index_label=False, index=False)


random_imputations()
