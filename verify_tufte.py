import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Set Tufte style context
sns.set_context("talk")
sns.set_style("white")

def plot_slopegraph():
    print("Testing Slopegraph...")
    # Data
    df = pd.DataFrame({
        'Country': ['A', 'B', 'C', 'D', 'E'],
        '1990': [10, 30, 20, 50, 40],
        '2010': [15, 25, 40, 45, 60]
    })
    
    # Setup plot
    fig, ax = plt.subplots(figsize=(6, 8))
    
    # Plot lines
    for i in range(len(df)):
        # Color logic: Green if up, Red if down (Tufte principle: maximize data ink, but color can be used for meaning)
        # Here we just use grey/black for Tufte minimalism
        ax.plot([1990, 2010], [df.loc[i, '1990'], df.loc[i, '2010']], color='black', marker='o', linewidth=1)
        
        # Labels
        ax.text(1990 - 2, df.loc[i, '1990'], f"{df.loc[i, 'Country']} {df.loc[i, '1990']}", ha='right', va='center', fontsize=12)
        ax.text(2010 + 2, df.loc[i, '2010'], f"{df.loc[i, '2010']} {df.loc[i, 'Country']}", ha='left', va='center', fontsize=12)

    # Tufte axes: Remove spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    # Ticks
    ax.set_xticks([1990, 2010])
    ax.set_yticks([]) # No y-axis numbers, data is on the labels
    
    plt.title("Slopegraph: Changes from 1990 to 2010", loc='left')
    plt.close() # Don't show, just run
    print("Slopegraph OK")

def plot_sparkline():
    print("Testing Sparkline...")
    # Data: A random walk
    np.random.seed(42)
    data = np.cumsum(np.random.randn(50))
    
    fig, ax = plt.subplots(figsize=(4, 1))
    ax.plot(data, color='blue', linewidth=1)
    
    # Mark the last point
    ax.plot(len(data)-1, data[-1], marker='o', color='red', markersize=4)
    ax.text(len(data), data[-1], f"{data[-1]:.1f}", color='red', fontsize=10, va='center')

    # Remove all axes for sparkline effect
    ax.axis('off')
    
    plt.close()
    print("Sparkline OK")

if __name__ == "__main__":
    try:
        plot_slopegraph()
        plot_sparkline()
        print("All Tests Passed")
    except Exception as e:
        print(f"Test Failed: {e}")
