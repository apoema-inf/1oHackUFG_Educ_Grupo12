import pandas as pd
from sqlalchemy import create_engine


def main():
    file_name = 'new_data.csv'
    df = create_final_df(file_name)
    df = change_column_names(df)
    save_df_to_database(df)


def save_df_to_database(df):
    engine = create_database_engine_for_pandas()
    df.to_sql('pesquisas', con=engine, if_exists='append', index=False)


def create_database_engine_for_pandas():
    url = get_django_database_credentials_url()
    engine = create_engine(url, echo=False)
    return engine


def get_django_database_credentials_url():
    database_url = 'sqlite:///test.db'
    return database_url


def change_column_names(df):
    df.columns = ['codigo', 'unidade', 'titulo', 'area_de_conhecimento', 'vinculacao',
                  'financiada', 'participacao', 'periodo_de_vigencia']
    return df

def create_final_df(file):
    df = pd.read_csv(file, sep=';')
    return df

main()
