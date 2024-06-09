import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns


"""
1. Load raw data and specify 'results path'
"""
data_path = "C:/Users/HP/PycharmProjects/V_C_PhD/Specific Objective 2/_Data/"
data_filename = "data_os2.csv"
both = data_path + data_filename
data = pd.read_csv(both)

# results path
results_path = "C:/Users/HP/PycharmProjects/V_C_PhD/Specific Objective 2/Results/"


"""
3. Create data subsets for each region
"""
# isolate the qualitative columns
qualitative_columns = [
    'v6', 'v341', 'v370', 'v371', 'v372',
    'v377', 'v378', 'v379', 'v382', 'v398']
data = data[qualitative_columns]
# list the regions
regions = [['adamaoua'], ['centre'], ['est'], ['sud']]
# isolate the data for each region
adamaoua_data = data[data['v6'].isin(regions[0])]
center_data = data[data['v6'].isin(regions[1])]
est_data = data[data['v6'].isin(regions[2])]
sud_data = data[data['v6'].isin(regions[3])]
# drop 'v6'
data = data.drop(['v6'], axis=1)
adamaoua_data = adamaoua_data.drop(['v6'], axis=1)
center_data = center_data.drop(['v6'], axis=1)
est_data = est_data.drop(['v6'], axis=1)
sud_data = sud_data.drop(['v6'], axis=1)


"""
4. Write a function to do the analysis given a dataset
"""


def analyse_with_chi_square(
        dataset, filename_viz, filename_tab, cmap):
    """Create an empty DataFrame to store p-values"""
    p_values_df = pd.DataFrame(
        index=dataset.columns,
        columns=dataset.columns)

    """Calculate chi-square test for each pair of variables"""
    for col1 in dataset.columns:
        for col2 in dataset.columns:
            if col1 != col2:
                contingency_table = pd.crosstab(
                    dataset[col1], dataset[col2])
                chi2, p_value, _, _ = stats.chi2_contingency(
                    contingency_table)
                p_values_df.loc[col1, col2] = p_value

    """Create a heatmap of p-values and save it"""
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        p_values_df.astype(float),
        annot=True, cmap=cmap, cbar=True)

    file = results_path + filename_viz
    plt.savefig(file, dpi=2000, bbox_inches='tight')

    """Save p-value table"""
    file2 = results_path + filename_tab
    p_values_df.to_csv(file2)


"""Plot and Analyse for combined dataset and for ALL regions"""


def final_analysis(number):
    datasets = [data, adamaoua_data,
                center_data, est_data,
                sud_data]

    analyse_with_chi_square(
        dataset=datasets[0],
        filename_viz=f"{number}__chi_square_PLOT_GENERAL.png",
        filename_tab=f"{number}__chi_square_TAB_GENERAL.csv",
        cmap='Accent')

    analyse_with_chi_square(
        dataset=datasets[1],
        filename_viz=f"{number}__chi_square_PLOT_ADAMAWA.png",
        filename_tab=f"{number}__chi_square_TAB_ADAMAWA.csv",
        cmap='Set1')

    analyse_with_chi_square(
        dataset=datasets[2],
        filename_viz=f"{number}__chi_square_PLOT_CENTER.png",
        filename_tab=f"{number}__chi_square_TAB_CENTER.csv",
        cmap='Dark2')

    analyse_with_chi_square(
        dataset=datasets[3],
        filename_viz=f"{number}__chi_square_PLOT_EST.png",
        filename_tab=f"{number}__chi_square_TAB_EST.csv",
        cmap='tab20')

    analyse_with_chi_square(
        dataset=datasets[4],
        filename_viz=f"{number}__chi_square_PLOT_SUD.png",
        filename_tab=f"{number}__chi_square_TAB_SUD.csv",
        cmap='tab20b')


final_analysis(number=2)
