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
adamaoua_data = adamaoua_data.drop(['v6'], axis=1)
center_data = center_data.drop(['v6'], axis=1)
est_data = est_data.drop(['v6'], axis=1)
sud_data = sud_data.drop(['v6'], axis=1)


"""
2. Pair plot
"""


def pair_plot(dataset, filename):
    sns.pairplot(dataset, hue="v6", diag_kind="hist")
    path = "C:/Users/HP/PycharmProjects/V_C_PhD/5Visualizations/sp_obj_1/"
    file = path + filename
    plt.savefig(file, dpi=2000, bbox_inches='tight')


"""plot pair plot with ALL regions"""
# pair_plot(dataset=data, filename='6_pair_plot_GENERAL.png')


def pair_plot_no_hue(dataset, filename):
    sns.pairplot(dataset, diag_kind="hist")
    path = "C:/Users/HP/PycharmProjects/V_C_PhD/5Visualizations/sp_obj_1/"
    file = path + filename
    plt.savefig(file, dpi=2000, bbox_inches='tight')


"""plot pair plots per region"""


def plot_pair_plots_no_hue():
    pair_plot_no_hue(
        dataset=adamaoua_data, filename='7_pair_plot_ADAMAWA.png')
    pair_plot_no_hue(
        dataset=center_data, filename='8_pair_plot_CENTER.png')
    pair_plot_no_hue(
        dataset=est_data, filename='9_pair_plot_EAST.png')
    pair_plot_no_hue(
        dataset=sud_data, filename='10_pair_plot_SOUTH.png')


# plot_pair_plots_no_hue()
