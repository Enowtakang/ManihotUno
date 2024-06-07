import pandas as pd


"""
1. Load data
"""
# ptf = path to file
ptf = "C:/Users/HP/PycharmProjects/V_C_PhD/2Datasets/sp_obj_1/"
# fn is file name
fn = 'all_data_v2.csv'

data = pd.read_csv(ptf + fn)
# print(len(data))
# print(data.head())

"""
2. Summary statistics
    - Create a function to generate summary statistics
        given 'data' and a 'results filename'.
     
"""
quantitative_variables = ['v28', 'v41', 'v72', 'v82']

summary_stats = []


def summary_statistics(dataframe, file_name):
    for variable in quantitative_variables:
        mean_value = dataframe[variable].mean()
        median_value = dataframe[variable].median()
        range_value = (
                dataframe[variable].max(
                ) - dataframe[variable].min())

        dataset = {
            'Variable': variable,
            'Mean': round(mean_value, 1),
            'Median': round(median_value, 1),
            'Range': round(range_value, 1)}

        summary_stats.append(dataset)

    summary_df = pd.DataFrame(summary_stats)

    path = "C:/Users/HP/PycharmProjects/V_C_PhD/6Results_Tabular/sp_obj_1/"

    summary_df.to_csv(
        path + file_name, index_label=True, index=True)


"""
3. Perform descriptive statistics: 
        - for ALL of the data 
        - per region
"""
# list the regions
regions = [['adamaoua'], ['centre'], ['est'], ['sud']]

# isolate the data for each region
adamaoua_data = data[data['v6'].isin(regions[0])]
center_data = data[data['v6'].isin(regions[1])]
est_data = data[data['v6'].isin(regions[2])]
sud_data = data[data['v6'].isin(regions[3])]


def generate_results():
    # All the data
    file_general = '1_descriptive_stats_GENERAL.csv'
    summary_statistics(data, file_general)

    # adamaoua
    file_adamaoua = '1b_descriptive_stats_ADAMAOUA.csv'
    summary_statistics(adamaoua_data, file_adamaoua)

    # center
    file_center = '1c_descriptive_stats_CENTER.csv'
    summary_statistics(center_data, file_center)

    #est
    file_est = '1d_descriptive_stats_EST.csv'
    summary_statistics(est_data, file_est)

    # sud
    file_sud = '1e_descriptive_stats_SUD.csv'
    summary_statistics(sud_data, file_sud)


# generate_results()
