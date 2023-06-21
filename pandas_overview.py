# github.com/BrunoSilvestre00/mini-curso-python
import pandas as pd

def prints(*args):
    print('-'*40)
    print(*args)
    print('-'*40)

def create_dataframe():
    alunos_dict = [
        {
            'nome': 'A',
            'idade': 12,
            'semestre': 2,
            'semestre_final': 8,
        },
        {
            'nome': 'B',
            'idade': 15,
            'semestre': 1,
            'semestre_final': 6,
        },
        {
            'nome': 'C',
            'idade': 18,
            'semestre': 3,
            'semestre_final': 8,
        },
        {
            'nome': 'D',
            'idade': 15,
            'semestre': 6,
            'semestre_final': 6,
        }
    ]

    df = pd.DataFrame(alunos_dict)

    return df


def filter_df(df):
    prints(df['nome'])

    prints(df[['nome', 'idade']])

    prints(df['idade'] < 18)

    index = [True, False, True, False]

    prints(df[index])

    prints(df[df['idade'] < 18])

    prints(df[df['idade'].isin([15, 18])])

    prints(df.query('semestre == semestre_final'))

    prints(df.query('semestre_final == 8'))


def group_by(df):
    group = df.groupby(by=['semestre_final'])

    prints(group.groups)

    prints(group.count())

    prints(group.sum())

    prints(group.max())

    prints(group.min())

    mean_age = df[['semestre_final', 'idade']]

    group = mean_age.groupby("semestre_final")

    prints(group.mean())

    prints(group.prod())

    print(group.std()) # devio padrão


def convert(df):
    df.to_csv('teste.csv', sep=';', index=True)
    df.to_json('teste.json')


def read_df():
    df1 = pd.read_csv('teste.csv', sep=';')
    prints(df1)

    df2 = pd.read_json('teste.json')
    prints(df2)


    df = pd.read_csv('idade_entrou.csv', sep='|')
    prints(df)

def manipulate():

    def f(idade, semestre):
        anos = semestre//2
        return idade - anos

    df1 = pd.read_csv('teste.csv', sep=';')

    df = df1.drop('Unnamed: 0', axis='columns')

    prints(df)

    for index, row in df.iterrows():
        print(row)

    idade_entrou = [f(row['idade'], row['semestre'])  for _, row in df.iterrows()]

    df['idade_entrou'] = idade_entrou

    prints(df)

    df.to_csv('idade_entrou.csv', sep='|', index=False)


def operation(df):
    prints(df)

    df['idade_x10'] = df['idade']*10
    
    df['idade_+10'] = df['idade']+10

    df['idade_sum'] = df['idade_x10'] + df['idade_+10']

    prints(df)

    prints(df[['idade_x10', 'idade_+10']].describe())


    print('='*60)
    print(df['idade'].sum())
    print(sum(df['idade']))
    print('='*60)

    print('='*60)
    print(df['idade'].count())
    print(len(df['idade']))
    print('='*60)

    print('='*60)
    print(df['idade'].max())
    print(max(df['idade']))
    print('='*60)


def main():
    df = create_dataframe()

    # create
    # filter

    # convert
    # read
    # usa esses dois pra manipular csv

    # manipulate

    # operation
    # mostra as funções de agregação

    # groupby


    operation(df)

if __name__ == '__main__':
    main()