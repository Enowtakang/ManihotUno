import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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
    'v6', 'v27', 'v31', 'v32', 'v48', 'v49', 'v325',
    'v495', 'v497', 'v499', 'v501', 'v503', 'v512']
data = data[qualitative_variables]

# list the regions
regions = [['adamaoua'], ['centre'], ['est'], ['sud']]

# isolate the data for each region
adamaoua_data = data[data['v6'].isin(regions[0])]
center_data = data[data['v6'].isin(regions[1])]
est_data = data[data['v6'].isin(regions[2])]
sud_data = data[data['v6'].isin(regions[3])]


"""
Define function to create the desired plot, 
    given the dataset, the variable and the desired filename
"""


def plot_bar(dataset, variable, filename):
    """calculate percentages"""
    total_count = len(dataset)

    total_yes_count = len(dataset[dataset[variable] == '1=Yes'])
    total_no_count = len(dataset[dataset[variable] == '2=No'])

    male_yes_count = len(
        dataset[(dataset['v27'] == '1=Male') & (
                dataset[variable] == '1=Yes')])

    male_no_count = len(
        dataset[(dataset['v27'] == '1=Male') & (
                dataset[variable] == '2=No')])

    female_yes_count = len(
        dataset[(dataset['v27'] == '2=Female') & (
                dataset[variable] == '1=Yes')])

    female_no_count = len(
        dataset[(dataset['v27'] == '2=Female') & (
                dataset[variable] == '2=No')])

    total_yes_percent = (total_yes_count / total_count) * 100
    total_no_percent = (total_no_count / total_count) * 100
    male_yes_percent = (male_yes_count / total_count) * 100
    female_yes_percent = (female_yes_count / total_count) * 100
    male_no_percent = (male_no_count / total_count) * 100
    female_no_percent = (female_no_count / total_count) * 100

    """Create a bar plot"""
    plt.figure(figsize=(8, 6))
    sns.barplot(x=[
        'Everyone (Yes)', 'Everyone (No)', 'Males (Yes)',
        'Males (No)', 'Females (Yes)', 'Females (No)'],
                y=[total_yes_percent, total_no_percent,
                   male_yes_percent, male_no_percent,
                   female_yes_percent, female_no_percent])
    plt.xlabel(variable)
    plt.ylabel('Percentage of People')
    plt.ylim(0, 100)

    """Annotate the bars with percentages"""
    for i, value in enumerate(
            [total_yes_percent, total_no_percent,
             male_yes_percent, male_no_percent,
             female_yes_percent, female_no_percent]):

        plt.text(
            i, value + 2,
            f'{value:.1f}%',
            ha='center',
            va='bottom')

    """save the figure"""
    path = "C:/Users/HP/PycharmProjects/V_C_PhD/5Visualizations/sp_obj_1/"
    file = path + filename
    plt.savefig(file, dpi=2000, bbox_inches='tight')


"""Plot for combined dataset and for ALL regions"""


def final_variable_plots(number, variable):
    datasets = [data, adamaoua_data,
                center_data, est_data,
                sud_data]
    plot_bar(dataset=datasets[0], variable=variable,
             filename=f'{number}__bar_plot_GENERAL_{variable}.png')

    plot_bar(dataset=datasets[1], variable=variable,
             filename=f'{number}_bar_plot_ADAMAWA_{variable}.png')

    plot_bar(dataset=datasets[2], variable=variable,
             filename=f'{number}_bar_plot_CENTER_{variable}.png')

    plot_bar(dataset=datasets[3], variable=variable,
             filename=f'{number}_bar_plot_EAST_{variable}.png')

    plot_bar(dataset=datasets[4], variable=variable,
             filename=f'{number}_bar_plot_SOUTH_{variable}.png')


# final_variable_plots(number='11', variable='v31')
# final_variable_plots(number='12', variable='v48')
# final_variable_plots(number='13', variable='v49')
# final_variable_plots(number='14', variable='v325')
# final_variable_plots(number='15', variable='v495')
# final_variable_plots(number='16', variable='v497')
# final_variable_plots(number='17', variable='v499')
# final_variable_plots(number='18', variable='v501')
# final_variable_plots(number='19', variable='v503')
# final_variable_plots(number='20', variable='v512')
