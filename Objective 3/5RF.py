import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import (
    r2_score, mean_absolute_error, mean_squared_error,
    max_error, root_mean_squared_error,
    mean_absolute_percentage_error,
    mean_gamma_deviance, mean_poisson_deviance,
    mean_tweedie_deviance, mean_pinball_loss)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import PartialDependenceDisplay
from sklearn.tree import plot_tree
from sklearn.preprocessing import StandardScaler


"""
1. Load raw data, specify 'results path' 
    and name feature and target columns
"""
data_path = "C:/Users/HP/PycharmProjects/V_C_PhD/Specific Objective 2/_Data/"
data_filename = "data_os2.csv"
both = data_path + data_filename
data = pd.read_csv(both)
# results path
results_path = "C:/Users/HP/PycharmProjects/V_C_PhD/Specific Objective 2/Results/"
# name feature and target columns
feature_columns = ['v341', 'v370', 'v371', 'v372', 'v377',
                   'v378', 'v379', 'v382', 'v398']

target_column1 = 'v215'
target_column2 = 'v216'

epochs = 100

"""
2. Train-Test Splitting
"""
X = data[feature_columns]
y = data[target_column2]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

"""
3. Initialize and fit RF regression model
"""
model = RandomForestRegressor(
    n_estimators=100, random_state=32)
model.fit(X_train, y_train)

# plot_model


def plot_the_model():
    plt.figure(figsize=(4, 4))
    plot_tree(
        model.estimators_[0],
        feature_names=X.columns, filled=True)
    filename = '3_model_plot.png'
    full_path = results_path + filename
    plt.savefig(full_path, dpi=2000, bbox_inches='tight')


# plot_the_model()


"""
4. Predict on the test dataset
"""
y_pred = model.predict(X_test)

"""
5. Calculate evaluation metrics
"""


def calculate_evaluation_metrics():
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = root_mean_squared_error(y_test, y_pred)
    mape = mean_absolute_percentage_error(y_test, y_pred)
    me = max_error(y_test, y_pred)
    mpl = mean_pinball_loss(y_test, y_pred)
    mgd = mean_gamma_deviance(y_test, y_pred)
    mpd = mean_poisson_deviance(y_test, y_pred)
    mtd = mean_tweedie_deviance(y_test, y_pred)

    metrics_df = pd.DataFrame(
        {
            "Metric": [
                'r2', 'mse', 'mae', 'rmse', 'mape', 'me',
                'mpl', 'mgd', 'mpd', 'mtd'],
            "Value": [r2, mse, mae, rmse, mape, me,
                      mpl, mgd, mpd, mtd]})

    filename = '3_model_evaluation_metrics.csv'
    full_path = results_path + filename
    metrics_df.to_csv(
        full_path, index=False, index_label=False)


"""
6. Plot feature importance scores
"""
feature_importance_scores = model.feature_importances_
print(feature_importance_scores)
print("Feature Importance Scores:")
for feature, importance in zip(
        X.columns, feature_importance_scores):
    print(f"{feature}: {importance:.4f}")


def plot_feature_importance_scores():
    plt.figure(figsize=(8, 6))
    sns.barplot(x=feature_importance_scores, y=X.columns)
    plt.xlabel('Feature Importance')
    plt.ylabel('Features')

    filename = '4_feature_importance_plots.png'
    full_path = results_path + filename
    plt.savefig(full_path, dpi=2000, bbox_inches='tight')


"""
7. Plot partial dependence scores
"""
features_of_interest = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def plot_partial_dependence_scores():
    display = PartialDependenceDisplay.from_estimator(
        model, X,
        features_of_interest,
        feature_names=X.columns)
    display.plot()

    filename = '5_partial_dependence_plots.png'
    full_path = results_path + filename
    plt.savefig(full_path, dpi=2000, bbox_inches='tight')


"""
8. Plot residuals
"""
residuals = y_test - y_pred


def plot_residuals():
    plt.figure(figsize=(8, 6))
    plt.scatter(y_pred, residuals, alpha=0.5)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.xlabel('Predicted Values')
    plt.ylabel('Residuals')

    filename = '6_residuals_plots.png'
    full_path = results_path + filename
    plt.savefig(full_path, dpi=2000, bbox_inches='tight')


calculate_evaluation_metrics()
plot_feature_importance_scores()
plot_partial_dependence_scores()
plot_residuals()
