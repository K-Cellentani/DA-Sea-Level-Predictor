import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.figure(figsize=(12, 8))
    plt.scatter(x, y)

    # Create first line of best fit
    years_extended = np.arange(1880, 2051, 1)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    line = [slope*xi + intercept for xi in years_extended]
    plt.plot(years_extended, line, color = 'orange', label="1880 Regression", linewidth=1)


    # Create second line of best fit
    df_best = df.loc[df['Year'] > 1999]
    best_x = df_best['Year']
    best_y = df_best['CSIRO Adjusted Sea Level']
    best_extended = np.arange(2000, 2051, 1)
    bslope, bintercept, br_value, bp_value, bstd_err = stats.linregress(best_x, best_y)
    best_line = [bslope*xi + bintercept for xi in best_extended]
    plt.plot(best_extended, best_line, color = 'red', label="2000 Regression", linewidth=1)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()