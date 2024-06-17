import pandas as pd


"""
1. Load raw data
"""
raw_data_path = "path/to/file"
raw_data_filename = "raw_data.xlsx"
both = raw_data_path + raw_data_filename
raw_data = pd.read_excel(both, engine='openpyxl')
raw_data.columns = raw_data.columns.str.strip()


"""
2. Extract data for specific objective 2
    - Version 1 
"""
renamed_columns_dictionary = {
    "0.4a Region / Province": "v6",
    "IV.1 What diseases and pests do you frequently see in your cassava fields?/1=Fungal": "v339",
    "IV.1 What diseases and pests do you frequently see in your cassava fields?/2= Bacterial": "v340",
    "IV.1 What diseases and pests do you frequently see in your cassava fields?/3= Viral (CMD, CBSD)": "v341",
    "IV.1 What diseases and pests do you frequently see in your cassava fields?/4= Mite damage and cassava pests": "v342",
    "IV.1 What diseases and pests do you frequently see in your cassava fields?/5= Whiteflies": "v343",

    "IV.6 What is the cause of the symptoms seen in the second photo?/1=A virus": "v352",
    "IV.6 What is the cause of the symptoms seen in the second photo?/2= The whitefly": "v353",
    "IV.6 What is the cause of the symptoms seen in the second photo?/3= The use of infected cuttings": "v354",
    "IV.6 What is the cause of the symptoms seen in the second photo?/4=Lack of rain": "v355",
    "IV.6 What is the cause of the symptoms seen in the second photo?/5=Soil moisture": "v356",
    "IV.6 What is the cause of the symptoms seen in the second photo?/6=Mineral deficiency": "v357",

    "IV.9 What is the impact of the appearance of these symptoms (CMD) on cassava plants / yield? /1=Poor plant growth": "v370",
    "IV.9 What is the impact of the appearance of these symptoms (CMD) on cassava plants / yield? /2= Decrease in yield": "v371",
    "IV.9 What is the impact of the appearance of these symptoms (CMD) on cassava plants / yield? /3=Lack of healthy plant material": "v372",
    "IV.9 What is the impact of the appearance of these symptoms (CMD) on cassava plants / yield? /4=Other (Specify)": "v373",

    "IV.10 How do you react when your cassava plants show the symptoms shown in photo 2?/1= Removal of infected plants": "v377",
    "IV.10 How do you react when your cassava plants show the symptoms shown in photo 2?/2= Destruction of infected plants": "v378",
    "IV.10 How do you react when your cassava plants show the symptoms shown in photo 2?/3= Replacement of infected plants by healthy cuttings": "v379",
    "IV.10 How do you react when your cassava plants show the symptoms shown in photo 2?/4= Analysis of the plants concerned with the Nuru application": "v380",
    "IV.10 How do you react when your cassava plants show the symptoms shown in photo 2?/5= Consultation with agricultural agents": "v381",
    "IV.10 How do you react when your cassava plants show the symptoms shown in photo 2?/6= Use of inputs": "v382",
    "IV.10 How do you react when your cassava plants show the symptoms shown in photo 2?/7= I do nothing": "v383",

    "IV.11 What do you think can be done to prevent or combat the onset of these symptoms/disease?/1= Use of healthy plant material": "v387",
    "IV.11 What do you think can be done to prevent or combat the onset of these symptoms/disease?/2= Regular monitoring of fields (removal, destruction, and replacement of infected plants)": "v388",
    "IV.11 What do you think can be done to prevent or combat the onset of these symptoms/disease?/3= Regular cleaning of the fields": "v389",
    "IV.11 What do you think can be done to prevent or combat the onset of these symptoms/disease?/ 4= Respect of the planting density (1mx1m)": "v390",
    "IV.11 What do you think can be done to prevent or combat the onset of these symptoms/disease?/5= Other (Specify)": "v391",

    "FP1. Cassava viral diseases are caused by poor hygiene on the field": "v412",
    "FP2. Viral symptoms observed on cassava leaves result from the application of herbicides.": "v413",
    "FP3. Older plants are more attacked by cassava viral diseases": "v414",
    "FP4. Late planting can lead to cassava viral diseases": "v415",
    "FP5. Drought and high temperatures can lead to cassava viral diseases.": "v416",
    "FP6. Planting in muddy or waterlogged soils causes infections.": "v417",
    "FP7. Poor aeration promotes cassava viral diseases": "v418",
    "FP8. A late harvest can lead to cassava viral diseases.": "v419",
    "FP9. Cassava viral diseases are caused by the use of poor-quality planting": "v420",
    "FP10. Cassava viral diseases can be managed by breaking the affected part": "v421",
    "FP11. The management practices can easily be integrated into the traditional farming system": "v422",
    "FP12. The management practices taught by the agricultural officers are complex to understand": "v423",
    "FP13. The use of integrated approaches to viral diseases control in cassava is more expensive than using chemicals.": "v424",
    "FP14. Chemicals are effective in controlling cassava viral diseases": "v425",
    "FP15. No cassava variety is resistant to viral diseases": "v426",
    "FP16. There is no control for cassava viral diseases": "v427",
    "FP17. The plant infected by cassava viral diseases always recovers at the beginning of the rains": "v428",
    "FP18. The management practices of cassava viral diseases are not culturally accepted in my community": "v429",
    "FP19. The use of cassava diseases management technologies helps to reduce the incidence of cassava viral diseases.": "v430",
    "FP20. The use of cassava disease management technologies increases productivity": "v431",
    "FP21. The management technologies are accessible at all times": "v432",
    "FP22. Cassava viral diseases prevent rooting": "v433",
    "FP23. Whenever cassava plants are attacked by viral diseases, it results in poor quality tubers": "v434",
    "FP24. Viral diseases of cassava can lead to 100% yield loss if left untreated.": "v435",
    "FP25. Cassava viral diseases result in loss of planting material": "v436"
}

"""
3. list of 'pests and diseases identification' variables
"""
# 5 variables
pdi_variables = ["v339", "v340", "v341", "v342", "v343"]

"""
4. list of 'causes of symptoms' variables
"""
# 6 variables
cos_variables = [
    "v352", "v353", "v354", "v355", "v356", "v357"]

"""
5. list of 'impact of cmd on cassava plants' variables
"""
# 4 variables
iccp_variables = ["v370", "v371", "v372", "v373", ]


"""
6. list of 'resctions' variables
"""
# 7 variables
reactions_variables = [
    "v377", "v378", "v379", "v380", "v381", "v382", "v383", ]


"""
7. list of 'disease prevention' variables
"""
# 5 variables
dp_variables = ["v387", "v388", "v389", "v390", "v391"]


"""
list of 'opinions' variables
"""
# 25 variables
opinions_variables = [
    "v412", "v413", "v414", "v415", "v416", "v417",
    "v418", "v419", "v420", "v421", "v422", "v423",
    "v424", "v425", "v426", "v427", "v428", "v429",
    "v430", "v431", "v432", "v433", "v434", "v435",
    "v436"]


"""
v6 variable
"""
v6 = ["v6"]


def extract_data():
    raw_data.rename(
        columns=renamed_columns_dictionary,
        inplace=True)

    """extract selected variables"""
    data = raw_data[
        v6 + pdi_variables + cos_variables + iccp_variables + reactions_variables + dp_variables + opinions_variables]

    """convert data in 'v6' to lowercase"""
    data['v6'] = data['v6'].str.lower()

    """select only rows which contain selected regions"""
    regions = ['adamaoua', 'centre', 'est', 'sud']
    data = data[data['v6'].isin(regions)]

    """save the data subset"""
    filename = '1extractedData.csv'
    both2 = raw_data_path + filename
    data.to_csv(
        both2, index_label=False, index=False)


extract_data()
