"""
This script will:
    print the number of distinct patterns,
    save the characteristics of each cluster
        in a DataFrame named characteristics_df, and
        display a heatmap showing these characteristics.

Each row in the heatmap represents a cluster, and
    each column represents a question.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


"""
1. Load datasets
"""
# filenames
pests_and_diseases_identification = '3a_pests_and_diseases_identification.csv'
causes_of_symptoms = '3b_causes_of_symptoms.csv'
impact_of_CMD_on_cassava_plants = '3c_impact_of_CMD_on_cassava_plants.csv'
reactions_to_CMD_symptoms = '3d_reactions_to_CMD_symptoms.csv'
CMD_prevention = '3e_CMD_prevention.csv'


def load_dataset(filename):
    data_path = "path/to/file"
    filepath = data_path + filename
    return pd.read_csv(filepath)


# load datasets
pdi = load_dataset(pests_and_diseases_identification)
cos = load_dataset(causes_of_symptoms)
iccp = load_dataset(impact_of_CMD_on_cassava_plants)
reactions = load_dataset(reactions_to_CMD_symptoms)
cmd_prevention = load_dataset(CMD_prevention)

datasets = [pdi, cos, iccp, reactions, cmd_prevention]


"""
2. Save pattern data and plot pattern characteristics
"""
results_path = "path/to/file"


def s_p_p_p_cs(
        dataFrame,
        filename_df_xtics,
        filename_plot_xtics):
    """
    s_p_p_p_cs = save patterns and plot pattern characteristics
    """
    """
    Identify distinct patterns 
    (assuming binary responses 0.0 and 1.0)
    """
    patterns = dataFrame.drop_duplicates()
    num_patterns = len(patterns)
    print(f'Number of distinct patterns: {num_patterns}')

    """
    Perform KMeans clustering
    """
    kmeans = KMeans(
        n_clusters=num_patterns,
        random_state=0).fit(dataFrame)

    """
    Assign clusters back to the original dataframe
    """
    dataFrame['cluster'] = kmeans.labels_

    """
    Group by cluster to get the characteristics of each pattern
    """
    cluster_characteristics = dataFrame.groupby(
        'cluster').mean().reset_index()

    """
    Save the characteristics to a new dataframe
    """
    characteristics_df = pd.DataFrame(cluster_characteristics)
    # save
    file_xtics = results_path + filename_df_xtics
    characteristics_df.to_csv(
        file_xtics, index=False, index_label=False)

    """
    Plotting the characteristics of each cluster
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(characteristics_df.drop(
        'cluster', axis=1), annot=True, cmap='BuPu')
    # plt.title('Characteristics of Each Cluster/Response Pattern')
    plt.xlabel('Questions')
    plt.ylabel('Cluster Number')
    # save
    file_plot_path = results_path + filename_plot_xtics
    plt.savefig(
        file_plot_path, dpi=2000, bbox_inches='tight')


# s_p_p_p_cs(
#     datasets[0],
#     filename_df_xtics="3a_pests_and_diseases_identification.csv",
#     filename_plot_xtics="3a_pests_and_diseases_identification.png")

# s_p_p_p_cs(
#     datasets[1],
#     filename_df_xtics='3b_causes_of_symptoms.csv',
#     filename_plot_xtics='3b_causes_of_symptoms.png')

# s_p_p_p_cs(
#     datasets[2],
#     filename_df_xtics='3c_impact_of_CMD_on_cassava_plants.csv',
#     filename_plot_xtics='3c_impact_of_CMD_on_cassava_plants.png')

# s_p_p_p_cs(
#     datasets[3],
#     filename_df_xtics='3d_reactions_to_CMD_symptoms.csv',
#     filename_plot_xtics='3d_reactions_to_CMD_symptoms.png')

# s_p_p_p_cs(
#     datasets[4],
#     filename_df_xtics='3e_CMD_prevention.csv',
#     filename_plot_xtics='3e_CMD_prevention.png')
