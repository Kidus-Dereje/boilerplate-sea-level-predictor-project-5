import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r, p, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    def pred_1(x):
        return slope * x + intercept
    
    years_extended = np.arange(df['Year'].min(), 2051)
    model = list(map(pred_1, years_extended))
    
    plt.plot(years_extended, model)
    
    # Create second line of best fit
    slope_2, intercept_2, r, p, std_err = linregress(df['Year'][120:], df['CSIRO Adjusted Sea Level'][120:])
    
    def pred_2(x):
        return slope_2 * x + intercept_2
    
    years_extended_2 = np.arange(2000, 2051)
    model_2 = list(map(pred_2, years_extended_2))
    
    plt.plot(years_extended_2, model_2, color='r')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()