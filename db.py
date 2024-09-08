from sqlalchemy import create_engine
import pandas as pd

from config import DATABASE_URL


def get_engine():
    engine = create_engine(DATABASE_URL)
    return engine


def execute_query(query):
    engine = get_engine()
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    return result