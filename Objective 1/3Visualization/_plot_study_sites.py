import pandas as pd
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

"""
1. Specify path to 'datasets' folder
    Also specify path to 'plots' folder
"""
# ptd = path to datasets
ptd = "C:/Users/HP/PycharmProjects/V_C_PhD/2Datasets/"
# ptp = path to plot of study site
ptp = "C:/Users/HP/PycharmProjects/V_C_PhD/Visualizations/study_site/"

"""
2. Visualize/Plot study sites
"""


def plot_study_sites():
    """gps data"""
    gps_data = 'gps_data.csv'

    """Load data"""
    data = pd.read_csv(ptd + gps_data)
    # print(data.head())

    """Load latitudes, longitudes, and altitudes"""
    lats = data['_GPS COORDINATE_latitude']
    lons = data['_GPS COORDINATE_longitude']
    village_names = data['0.4c Village']

    """Set up the map projection 
    (PlateCarree for lat/lon coordinates)"""
    projection = ccrs.PlateCarree()

    """Create a map centered on Cameroon"""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(
        111,
        projection=projection)
    ax.set_extent([8, 17, 1, 14])

    """Add cartopy features 
    (borders, lakes, coastline, rivers, etc.)"""
    ax.add_feature(
        cfeature.BORDERS,
        edgecolor='black', linewidth=1)
    ax.add_feature(
        cfeature.LAKES, alpha=0.5)
    ax.add_feature(cfeature.LAND)
    ax.add_feature(
        cfeature.COASTLINE,
        edgecolor='black', linewidth=1)
    ax.add_feature(
        cartopy.feature.RIVERS,
        edgecolor='blue', linewidth=0.5)

    """Plot survey respondent locations as points"""
    ax.scatter(
        lons, lats,
        color='red', marker='o',
        transform=projection)

    """Annotate Regions of Cameroon"""
    ax.text(12.8055, 6.9182,
            'Adamawa', transform=projection, fontsize=12, color='blue')
    ax.text(11.7068, 4.6298,
            'Centre',transform=projection, fontsize=12, color='blue')
    ax.text(13.9144, 3.9505,
            'East', transform=projection, fontsize=12, color='blue')
    ax.text(14.6588, 10.6316,
            'Far North', transform=projection, fontsize=12, color='blue')
    ax.text(10.0807, 4.1612,
            'Littoral', transform=projection, fontsize=12, color='blue')
    ax.text(13.9144, 8.5809,
            'North', transform=projection, fontsize=10, color='blue')
    ax.text(10.4397, 6.4704,
            'North-West', transform=projection, fontsize=12, color='blue')
    ax.text(11.7068, 2.7203,
            'South', transform=projection, fontsize=12, color='blue')
    ax.text(9.3673, 5.1573,
            'South-West', transform=projection, fontsize=12, color='blue')
    ax.text(10.8000, 5.4638,
            'West', transform=projection, fontsize=12, color='blue')

    # YAOUNDE and DOUALA
    ax.text(11.5202, 3.8617,
            'Yaoundé', transform=projection, fontsize=10, color='black')
    ax.text(9.786072, 4.061536,
            'Douala', transform=projection, fontsize=10, color='black')

    # NEIGHBORING COUNTRIES
    ax.text(8.6753, 9.0820,
            'NIGERIA', transform=projection, fontsize=15, color='green')

    """Save the map as a PNG file"""
    image_name = 'study_sites_cameroon.png'
    file = ptp + image_name
    plt.savefig(file, dpi=2000, bbox_inches='tight')


# plot_study_sites()
