import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


SUCCESS_COLOR = '#4bb543'
FAIL_COLOR = '#ff3333'

MOEDA = 'litecoin'

def process_df(df):
    years = []
    months = []
    days = []

    for date in df['Date']:
        year, month, day = date.split('-')
        years.append(int(year))
        months.append(int(month))
        days.append(int(day))

    df['Year'] = years
    df['Month'] = months
    df['Day'] = days

    return df

def get_dataframe():
    PATH = f'datasets/coins/{MOEDA}.csv'
    df = pd.read_csv(PATH, sep=',')
    df = process_df(df)

    return df

def get_data():
    df = get_dataframe()

    df = df.query("Year == 2018 and Month == 1")

    labels = df['Day']

    all_data = [[row['High'], row['Open'], row['Low']] for index, row in df.iterrows()]
    
    return all_data, labels, len(all_data)

def plot():
    all_data, labels, size = get_data()

    fig, ax = plt.subplots()

    boxplot = ax.boxplot(all_data, vert=True, widths=0.9, showcaps=False, whiskerprops={'visible': False})

    ax.set_title(f'Variação de preço da moeda {MOEDA}')

    ax.set_xlabel('Mês')
    ax.set_ylabel('Valor')

    ax.set_xticklabels(labels)

    plt.setp(boxplot['medians'], color='#aaa')

    for data, box in zip(all_data, boxplot['boxes']):
        color = SUCCESS_COLOR if data[0] > data[1]*1.05 else FAIL_COLOR
        box.set_color(color)

    plt.show()

plot()




