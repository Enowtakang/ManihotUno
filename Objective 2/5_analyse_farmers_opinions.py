import pandas as pd
import matplotlib.pyplot as plt


"""
1. Load dataset
"""
data_path = "path/to/file"
filename = "3f_farmers_opinions_on_CMD_and_its_management.csv"
filepath = data_path + filename
data = pd.read_csv(filepath)


"""
2. Create an empty list to store cross-tab dataframes
"""
cross_tab_list = []


"""
3. Perform cross-tabulation for each combination of 
    questions and store in the list
"""
opinions_variables = [
    "v412", "v413", "v414", "v415", "v416", "v417",
    "v418", "v419", "v420", "v421", "v422", "v423",
    "v424", "v425", "v426", "v427", "v428", "v429",
    "v430", "v431", "v432", "v433", "v434", "v435",
    "v436"]

results_path = "path/to/file"


def plot_bars(dataset):
    # Create a 5x5 grid of subplots
    fig, axes = plt.subplots(
        nrows=5,
        ncols=5,
        figsize=(10, 10))

    # Flatten the 2D array of axes for easy iteration
    axes = axes.flatten()

    for i, col in enumerate(dataset.columns):
        # Get percentage counts for each response
        counts = dataset[col].value_counts(
            normalize=True) * 100

        bars = axes[i].bar(
            counts.index,
            counts.values,
            tick_label=["1", "2", "3"])
        axes[i].set_title(col)
        # Set y-axis limit to percentage scale
        axes[i].set_ylim(0, 100)

        # Annotate bars with the percentage values
        for bar in bars:
            yval = bar.get_height()
            axes[i].annotate(
                f'{yval:.2f}%',
                (bar.get_x() + bar.get_width() / 2, yval),
                va='bottom', ha='center')

    plt.tight_layout()

    """save the plot"""
    filename_plot = "3f_farmers_opinions_on_CMD_and_its_management_BARs.png"
    filepath_plot = results_path + filename_plot
    plt.savefig(filepath_plot, dpi=2000, bbox_inches='tight')


plot_bars(dataset=data)
