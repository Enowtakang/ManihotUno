import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


"""
1. Load data / define data subsets
"""
# ptf = path to file
ptf = "C:/Users/HP/PycharmProjects/V_C_PhD/2Datasets/sp_obj_1/"
# fn is file name
fn = 'all_data_v2.csv'
# load/read data
data = pd.read_csv(ptf + fn)
# print(len(data))
# print(data.head())
# specify the quantitative variables
quantitative_variables = ['v6', 'v28', 'v41', 'v72', 'v82']
data = data[quantitative_variables]
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
2. Define a function to plot a correlation heatmap
    - Then use it to plot all 5 correlation heatmaps
"""


def annotated_corr_heatmap(dataset, filename, cmap):
    corr_matrix = dataset.corr()
    # Generate the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        corr_matrix, annot=True,
        # YlGnBu, Blues, coolwarm, BuPu, Greens
        cmap=cmap, center=0)
    path = "C:/Users/HP/PycharmProjects/V_C_PhD/5Visualizations/sp_obj_1/"
    file = path + filename
    plt.savefig(file, dpi=2000, bbox_inches='tight')


"""plot for general data"""


def plot_general_data():
    file_name_all = '1_corr_heatmap_GENERAL.png'
    annotated_corr_heatmap(
        dataset=data,
        filename=file_name_all,
        cmap='coolwarm')


# plot_general_data()


"""plot for ADAMAWA"""


def plot_adamawa():
    file_name_all = '2_corr_heatmap_ADAMAWA.png'
    annotated_corr_heatmap(
        dataset=adamaoua_data,
        filename=file_name_all,
        cmap='YlGnBu')


# plot_adamawa()


"""plot for CENTER"""


def plot_center():
    file_name_all = '3_corr_heatmap_CENTER.png'
    annotated_corr_heatmap(
        dataset=center_data,
        filename=file_name_all,
        cmap='Blues')


# plot_center()


"""plot for EAST"""


def plot_east():
    file_name_all = '4_corr_heatmap_EAST.png'
    annotated_corr_heatmap(
        dataset=est_data,
        filename=file_name_all,
        cmap='BuPu')


# plot_east()


"""plot for SOUTH"""


def plot_south():
    file_name_all = '5_corr_heatmap_SOUTH.png'
    annotated_corr_heatmap(
        dataset=sud_data,
        filename=file_name_all,
        cmap='Greens')


# plot_south()
