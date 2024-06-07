import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns


"""
1. Load all of the data
"""
ptf = "C:/Users/HP/PycharmProjects/V_C_PhD/2Datasets/sp_obj_1/"
fn = 'all_data_v2.csv'
data = pd.read_csv(ptf + fn)


"""
2. Segment the data per region
"""
# specify the qualitative variables
qualitative_variables = [
    'v6', 'v27', 'v31', 'v48', 'v49', 'v325',
    'v495', 'v497', 'v499', 'v501', 'v503', 'v512']
data = data[qualitative_variables]

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
Write a function to do the analysis given a dataset
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

    path = "C:/Users/HP/PycharmProjects/V_C_PhD/5Visualizations/sp_obj_1/"
    file = path + filename_viz
    plt.savefig(file, dpi=2000, bbox_inches='tight')

    """Save p-value table"""
    path2 = "C:/Users/HP/PycharmProjects/V_C_PhD/6Results_Tabular/"
    file2 = path2 + filename_tab
    p_values_df.to_csv(file2)


"""Plot and Analyse for combined dataset and for ALL regions"""


def final_analysis(number_viz, number_tab):
    datasets = [data, adamaoua_data,
                center_data, est_data,
                sud_data]

    analyse_with_chi_square(
        dataset=datasets[0],
        filename_viz=f"{number_viz}__chi_square_PLOT_GENERAL.png",
        filename_tab=f"{number_tab}__chi_square_TAB_GENERAL.csv",
        cmap='Accent')

    analyse_with_chi_square(
        dataset=datasets[1],
        filename_viz=f"{number_viz}__chi_square_PLOT_ADAMAWA.png",
        filename_tab=f"{number_tab}__chi_square_TAB_ADAMAWA.csv",
        cmap='Set1')

    analyse_with_chi_square(
        dataset=datasets[2],
        filename_viz=f"{number_viz}__chi_square_PLOT_CENTER.png",
        filename_tab=f"{number_tab}__chi_square_TAB_CENTER.csv",
        cmap='Dark2')

    analyse_with_chi_square(
        dataset=datasets[3],
        filename_viz=f"{number_viz}__chi_square_PLOT_EST.png",
        filename_tab=f"{number_tab}__chi_square_TAB_EST.csv",
        cmap='tab20')

    analyse_with_chi_square(
        dataset=datasets[4],
        filename_viz=f"{number_viz}__chi_square_PLOT_SUD.png",
        filename_tab=f"{number_tab}__chi_square_TAB_SUD.csv",
        cmap='tab20b')


final_analysis(number_viz=21, number_tab=2)
