import pandas as pd
import matplotlib.pyplot as plt

COLORS = ['#fa0', '#0fa', '#0af']

def get_dataframe():
    PATH = 'datasets/games/chess_games.csv'
    df = pd.read_csv(PATH, sep=',')
    return df

def get_data():
    df = get_dataframe()

    groups = df.groupby('winner').groups

    winners = groups.keys()
    games = [len(groups[k]) for k in winners]

    total_games = sum(games)

    labels = [f'{w} {(g/total_games)*100:.2f}%' for w, g in zip(winners, games)]

    return games, labels

def plot():
    values, labels = get_data()
    plt.pie(values, labels=labels, colors=COLORS)
    plt.show()

plot()
