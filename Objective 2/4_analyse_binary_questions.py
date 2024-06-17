import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


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
2. Identify response patterns / data clusters 
        and visualize them
"""
results_path = "path/to/file"


def plot_patterns(df, filename):
    patterns = df.drop_duplicates()
    num_patterns = len(patterns)
    print(f'Number of distinct patterns: {num_patterns}')

    kmeans = KMeans(
        n_clusters=num_patterns, random_state=0).fit(df)

    pca = PCA(2)
    df_pca = pca.fit_transform(df)

    # Create a DataFrame for the cluster plot
    plot_df = pd.DataFrame(df_pca, columns=['PC1', 'PC2'])
    plot_df['cluster'] = kmeans.labels_

    # Plotting the clusters
    plt.figure(figsize=(10, 8))
    sns.scatterplot(
        data=plot_df, x='PC1', y='PC2', hue='cluster',
        palette='viridis', legend='full')

    # Annotate each cluster centroid
    centroids = pca.transform(kmeans.cluster_centers_)
    for i, (x, y) in enumerate(centroids):
        plt.text(
            x, y, f'Pattern {i}', fontsize=12,
            ha='center', va='center',
            bbox=dict(facecolor='white',
                      alpha=0.5, boxstyle='round,pad=0.5'))

    # plt.title('Cluster Analysis of Response Patterns')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend(title='Cluster')

    """save the plot"""
    file = results_path + filename
    plt.savefig(file, dpi=2000, bbox_inches='tight')


# plot_patterns(datasets[0], '3a_pests_and_diseases_identification.png')
# plot_patterns(datasets[1], '3b_causes_of_symptoms.png')
# plot_patterns(datasets[2], '3c_impact_of_CMD_on_cassava_plants.png')
# plot_patterns(datasets[3], '3d_reactions_to_CMD_symptoms.png')
# plot_patterns(datasets[4], '3e_CMD_prevention.png')
