from Database.models import *
from Database.database import engine, Base
import pandas as pd
import logging
import glob
from os import path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def drop_table_with_cascade(table_name):
    """
    Drop a table with CASCADE if it exists.

    Args:
        table_name (str): Name of the table to drop.
    """
    try:
        with engine.connect() as connection:
            connection.execute(text(f"DROP TABLE IF EXISTS {table_name} CASCADE"))
            logger.info(f"Successfully dropped table: {table_name}")
    except Exception as e:
        logger.error(f"Failed to drop table {table_name}: {e}")


def load_csv_to_table(table_name, csv_path):
    """
     Load data from a CSV file into a database table.

     Args:
     - table_name: Name of the database table.
     - csv_path: Path to the CSV file containing data.

     Returns:
     - None
     """
    try:
        df = pd.read_csv(csv_path)

        # Use replace to overwrite the table (for testing)
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)
        logger.info(f"Successfully loaded {table_name}")
    except pd.errors.ParserError as e:
        logger.error(f"Failed to parse {csv_path}: {e}")
    except Exception as e:
        logger.error(f"Failed to load table {table_name}: {e}")



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

logger.info("Tables are populated.")