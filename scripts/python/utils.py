import datetime

from database import get_engine


def send_to_db(data_df, index_label):
    engine = get_engine()
    # Use theindex of the data frame as id of the table
    data_df.to_sql(
        'HealthcareData',
        engine,
        schema='dbo',
        if_exists='append',
        index=True,
        index_label=index_label
    )
