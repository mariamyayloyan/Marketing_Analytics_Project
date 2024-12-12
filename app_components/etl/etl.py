from Database.models import *
from Database.database import engine, Base
from sqlalchemy import create_engine, text, inspect
import pandas as pd
import logging
import glob
from os import path
import os


""" Configure logging """
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logging.basicConfig()


def drop_all_foreign_keys():
    """
    Drops all foreign key constraints in the database schema.
    Logs any failures.
    """
    try:
        with engine.connect() as connection:
            inspector = inspect(engine)
            for table_name in inspector.get_table_names():
                for fk in inspector.get_foreign_keys(table_name):
                    fk_name = fk.get('name')
                    if fk_name:
                        connection.execute(text(f"ALTER TABLE {table_name} DROP CONSTRAINT IF EXISTS {fk_name} CASCADE"))
                        logger.info(f"Successfully dropped foreign key {fk_name} on table {table_name}")
    except Exception as e:
        logger.error(f"Failed to drop foreign keys: {e}")


def drop_table_with_cascade(table_name):
    """
    Drops a specified table with CASCADE option.

    Args:
        table_name (str): Name of the table to drop.

    Logs:
        - Success message if the table is dropped.
        - Error message if the operation fails.
    """
    try:
        with engine.connect() as connection:
            connection.execute(text(f"DROP TABLE IF EXISTS {table_name} CASCADE"))
            logger.info(f"Successfully dropped table: {table_name}")
    except Exception as e:
        logger.error(f"Failed to drop table {table_name}: {e}")


def load_csv_to_table(table_name, csv_path):
    """
    Loads data from a CSV file into a specified database table.

    Args:
        table_name (str): Name of the target table.
        csv_path (str): Path to the CSV file.

    Logs:
        - Success message if data is loaded successfully.
        - Error message if loading or parsing fails.
    """
    try:
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)
        logger.info(f"Successfully loaded {table_name}")
    except pd.errors.ParserError as e:
        logger.error(f"Failed to parse {csv_path}: {e}")
    except Exception as e:
        logger.error(f"Failed to load table {table_name}: {e}")


def validate_table_schema(table_name):
    """
    Validates and logs the schema of a specified table.

    Args:
        table_name (str): Name of the table to validate.

    Logs:
        - Table schema if validation succeeds.
        - Error message if validation fails.
    """
    inspector = inspect(engine)
    try:
        columns = inspector.get_columns(table_name)
        logger.info(f"Schema for table {table_name}: {columns}")
    except Exception as e:
        logger.error(f"Failed to validate schema for table {table_name}: {e}")


""" Drop and recreate tables """

# Drop all foreign keys first
drop_all_foreign_keys()

# Drop dependent tables in the correct order
dependent_tables = ["results", "subscription", "price", "notification", "plan", "customer", "location", "application"]
for table in dependent_tables:
    drop_table_with_cascade(table)

# Recreate tables
Base.metadata.create_all(bind=engine)
logger.info("Tables have been recreated.")

""" Check if Data folder exists """
if not path.exists("Data"):
    logger.error("Data folder not found. Please ensure the folder exists.")
    exit(1)

""" Specify the path to the folder """
folder_path = "Data/*.csv"

""" Use glob to get a list of file paths in the specified folder """
files = glob.glob(folder_path)
base_names = [path.splitext(path.basename(file))[0] for file in files]

""" Load each CSV into its corresponding database table """
for table in base_names:
    try:
        load_csv_to_table(table, path.join("Data", f"{table}.csv"))
    except Exception as e:
        logger.error(f"Failed to ingest table {table}: {e}")

""" Validate schema for the results table """
validate_table_schema("results")

logger.info("Tables are populated.")
