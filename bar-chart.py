import pandas as pd
import matplotlib.pyplot as plt

COLORS = ['#fa0', '#0fa', '#0af']

def get_dataframe():
    PATH = 'datasets/games/best_selling_consoles.csv'
    df = pd.read_csv(PATH, sep=';')
    return df

def get_data():
    df = get_dataframe()

    df = df.sort_values(by='released_year')
    size = len(df)

    labels = [f'{df["console_name"][i]} - {df["units_sold"][i]}' for i in range(size)]

    return df['units_sold'], df['released_year'], labels, size

def plot():
    values, xticks, labels, size = get_data()

    plt.bar(xticks, values, color=COLORS)
   
    plt.xlabel('Ano de lançamento')
    plt.ylabel('Unidades vendidas (milhões)')
    plt.xticks(xticks, rotation=45)

    for i in range(size):
        plt.text(xticks[i], values[i]+1, labels[i], horizontalalignment='center')

    plt.show()


plot()