from Database.models import *
from Database.database import engine, Base
from sqlalchemy import create_engine, text, inspect
import pandas as pd
import logging
import glob
from os import path
import os 

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logging.basicConfig()


def drop_table_with_cascade(table_name):
    try:
        with engine.connect() as connection:
            connection.execute(text(f"DROP TABLE IF EXISTS {table_name} CASCADE"))
            logger.info(f"Successfully dropped table: {table_name}")
    except Exception as e:
        logger.error(f"Failed to drop table {table_name}: {e}")


def load_csv_to_table(table_name, csv_path):
    try:
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)
        logger.info(f"Successfully loaded {table_name}")
    except pd.errors.ParserError as e:
        logger.error(f"Failed to parse {csv_path}: {e}")
    except Exception as e:
        logger.error(f"Failed to load table {table_name}: {e}")


def validate_table_schema(table_name):
    inspector = inspect(engine)
    try:
        columns = inspector.get_columns(table_name)
        logger.info(f"Schema for table {table_name}: {columns}")
    except Exception as e:
        logger.error(f"Failed to validate schema for table {table_name}: {e}")


# Drop and recreate tables
drop_table_with_cascade("results")
Base.metadata.create_all(bind=engine)
logger.info("Tables have been recreated.")

# Check if Data folder exists
if not path.exists("Data"):
    logger.error("Data folder not found. Please ensure the folder exists.")
    exit(1)

# Specify the path to the folder, using "*" to match all files
folder_path = "Data/*.csv"

# Use glob to get a list of file paths in the specified folder
files = glob.glob(folder_path)
base_names = [path.splitext(path.basename(file))[0] for file in files]

# Load each CSV into its corresponding database table
for table in base_names:
    try:
        load_csv_to_table(table, path.join("Data", f"{table}.csv"))
    except Exception as e:
        logger.error(f"Failed to ingest table {table}: {e}")

# Validate schema for the results table
validate_table_schema("results")

logger.info("Tables are populated.")
