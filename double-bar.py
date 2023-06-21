import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


COLORS = ['#fa0', '#0fa', '#0af']

def get_dataframe():
    PATH = 'datasets/sports/messi_vs_ronaldo_stats.csv'
    df = pd.read_csv(PATH, sep=';')
    return df

def get_data():
    df = get_dataframe()

    df = df.sort_values(by='year')
    size = len(df)

    messi_performance = df['messi_goals'].div(df['messi_games']) * 100
    ronaldo_performance = df['ronaldo_goals'].div(df['ronaldo_games']) * 100

    labels = list(map(str, df['year']))

    return messi_performance, ronaldo_performance, labels, size


def plot():
    messi, ronaldo, labels, size = get_data()

    x = np.arange(size)

    WIDTH = 0.35

    fig, ax = plt.subplots()

    barras_1 = ax.bar(x - WIDTH/2, messi, width=WIDTH, color=COLORS[0], label='Messi', edgecolor='#000')
    barras_2 = ax.bar(x + WIDTH/2, ronaldo, width=WIDTH, color=COLORS[1], label='Ronaldo', edgecolor='#000')

    ax.bar_label(barras_1, fmt="%.2f")
    ax.bar_label(barras_2, fmt="%.2f")

    ax.set_ylabel('Performance %')
    ax.set_xlabel('Ano')
    ax.set_title('Comparação de performance entre Messi e CR7')
    ax.set_xticks(x+WIDTH//2)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.grid(True, axis="y", linestyle=':')
    plt.show()

plot()
