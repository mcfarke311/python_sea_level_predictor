import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    fig, ax = plt.subplots()
    
    # Create scatter plot
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    m, b, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    bf_x = list(range(df['Year'].iloc[0], 2050))
    bf_y = [m * x + b for x in bf_x]

    ax.plot(bf_x, bf_y, 'r-')

    # Create second line of best fit
    recent_df = df.loc[df['Year'] >= 2000]
    m, b, _, _, _ = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    bf_x = list(range(recent_df['Year'].iloc[0], 2050))
    bf_y = [m * x + b for x in bf_x]

    ax.plot(bf_x, bf_y, 'g-')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()