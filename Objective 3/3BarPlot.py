import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
4. Create the bar plot  function
"""


def plot_bar(dataset, filename):
    """calculate counts and percentages"""
    percent_df = pd.DataFrame()
    for col in dataset.columns:
        ones_count = dataset[col].sum()
        zeros_count = len(dataset) - ones_count
        total_count = len(dataset)

        ones_percentage = (ones_count / total_count) * 100
        zeros_percentage = (zeros_count / total_count) * 100

        percent_df[col] = [ones_percentage, zeros_percentage]

    """Transpose the DataFrame"""
    percent_df = percent_df.T
    """Rename columns for clarity"""
    percent_df.columns = ['YES', 'NO']

    """create subplots"""
    fig, ax = plt.subplots(1, 2,
                           figsize=(12, 6))

    """Bar plot for YES"""
    sns.barplot(data=percent_df, x=percent_df.index,
                y='YES', color='blue', label='YES', ax=ax[0])
    ax[0].set_xlabel('Variables')
    ax[0].set_ylabel('Percentage')
    # ax[0].set_title('Percentage of 1s for Each Variable')

    """Bar plot for NO"""
    sns.barplot(data=percent_df, x=percent_df.index,
                y='NO', color='orange', label='NO', ax=ax[1])
    ax[1].set_xlabel('Variables')
    ax[1].set_ylabel('Percentage')
    # ax[1].set_title('Percentage of 0s for Each Variable')

    """Add value annotations"""
    for i, row in percent_df.iterrows():
        ax[0].annotate(
            f"{row['YES']:.2f}%", (i, row['YES']),
            ha='center', va='bottom', color='black')
        ax[1].annotate(
            f"{row['NO']:.2f}%", (i, row['NO']),
            ha='center', va='top', color='black')

    plt.tight_layout()

    """save the plot"""
    file = results_path + filename
    plt.savefig(file, dpi=2000, bbox_inches='tight')


"""Plot for combined dataset and for ALL regions"""


def final_variable_plots(number):
    datasets = [data, adamaoua_data,
                center_data, est_data,
                sud_data]
    plot_bar(dataset=datasets[0],
             filename=f'{number}__bar_plot_GENERAL.png')

    plot_bar(dataset=datasets[1],
             filename=f'{number}_bar_plot_ADAMAWA.png')

    plot_bar(dataset=datasets[2],
             filename=f'{number}_bar_plot_CENTER.png')

    plot_bar(dataset=datasets[3],
             filename=f'{number}_bar_plot_EAST.png')

    plot_bar(dataset=datasets[4],
             filename=f'{number}_bar_plot_SOUTH.png')


final_variable_plots(number=1)
