import pandas as pd
import matplotlib.pyplot as plt

COLORS = ['#fa0', '#0fa', '#0af']

def get_dataframe():
    PATH = 'datasets/games/chess_games.csv'
    df = pd.read_csv(PATH, sep=',')
    return df

def get_data():
    df = get_dataframe()

    grouper = df[['winner', 'game_id']].groupby('winner')

    winners = grouper.groups.keys()
    games = grouper.count()['game_id']

    total_games = games.sum()

    def f(w, g):
        return f'{w} {(g/total_games)*100:.2f}%'

    labels = [f(*a) for a in zip(winners, games)]

    return games, labels

def plot():
    values, labels = get_data()
    plt.pie(values, labels=labels, colors=COLORS)
    plt.show()

plot()
