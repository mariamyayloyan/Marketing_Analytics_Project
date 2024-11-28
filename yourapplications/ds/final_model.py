import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd

# Define your engine (assuming it's already defined in Database.database)
from yourapplications.etl import *

from sqlalchemy import create_engine
from sqlalchemy import inspect  # Import the SQLAlchemy inspector

def fetch_table_as_dataframe(table_name):
    """
    Fetch data from a specific database table and return it as a Pandas DataFrame.

    Args:
        table_name (str): The name of the table to fetch data from.

    Returns:
        pd.DataFrame: The table data as a DataFrame.
    """
    query = f"SELECT * FROM {table_name}"  # SQL query to select all data
    with engine.connect() as connection:
        df = pd.read_sql_query(query, connection)
        print(f"Fetched {len(df)} rows from table '{table_name}'.")
        return df


customer_df = fetch_table_as_dataframe("customer")
location_df = fetch_table_as_dataframe("location")
plan_df = fetch_table_as_dataframe("plan")
application_df = fetch_table_as_dataframe("application")
price_df = fetch_table_as_dataframe("price")
notification_df = fetch_table_as_dataframe("notification")
subscription_df = fetch_table_as_dataframe("subscription")

