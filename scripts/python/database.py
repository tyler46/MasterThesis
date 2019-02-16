from decouple import config
from sqlalchemy import create_engine


DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST', default='localhost')
DB_NAME = config('DB_NAME')


def get_url():
    return f'mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?driver=SQL+Server+Native+Client+11.0'  # noqa


def get_engine():
    return create_engine(get_url())
