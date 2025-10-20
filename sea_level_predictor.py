import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Scatter
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Line of best fit (all data, extended to 2050)
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_all = np.arange(df["Year"].min(), 2051)
    ax.plot(years_all, res_all.slope * years_all + res_all.intercept, label="Best fit: 1880–present")

    # Line of best fit (from 2000, extended to 2050)
    df_2000 = df[df["Year"] >= 2000]
    res_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    years_2000 = np.arange(2000, 2051)
    ax.plot(years_2000, res_2000.slope * years_2000 + res_2000.intercept, label="Best fit: 2000–present", color="orange")

    # Labels & title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # Save & return
    fig.savefig("sea_level_plot.png")
    return fig
