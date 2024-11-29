import pandas as pd
import numpy as np
import sqlalchemy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

from yourapplications.etl.Database.database import *

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
        #print(f"Fetched {len(df)} rows from table '{table_name}'.")
        return df



customer = fetch_table_as_dataframe("customer")
location = fetch_table_as_dataframe("location")
plan = fetch_table_as_dataframe("plan")
application = fetch_table_as_dataframe("application")
price = fetch_table_as_dataframe("price")
notification = fetch_table_as_dataframe("notification")
subscription = fetch_table_as_dataframe("subscription")
results = fetch_table_as_dataframe("results")

"""Merging tables"""
merged_table = customer.merge(subscription, on='customer_id', how='inner')
merged_table = merged_table.merge(application, left_on='application_id', right_on='app_id', how='inner')
merged_table = merged_table.merge(location, on='location_id', how='inner')
merged_table = merged_table.merge(price, left_on='price_id', right_on='id', how='inner')
merged_table = merged_table.merge(notification, on='notification_id', how='inner')
merged_table = merged_table.merge(plan, left_on='plan_type_id', right_on='plan_id', how='inner')
#merged_table = merged_table.merge(results, on='customer_id', how='inner')
#print(merged_table.head())


""" Cleaning  and labeling data"""

# Defining subscription duration

merged_table['start_date'] = pd.to_datetime(merged_table['start_date'])
merged_table['end_date'] = pd.to_datetime(merged_table['end_date'])

merged_table['subscription_duration'] = (merged_table['end_date'] - merged_table['start_date']).dt.days

columns_to_drop = ['first_name', 'last_name', 'location_id', 'birth_date','customer_id','email', 'app_id', 'plan_type_id','application_id_y','area_name','id_x',  'id_y', 'start_date','end_date', 'plan_id_x', 'plan_id_y', 'notification_id','application_id_x','price_id' ]
merged_table = merged_table.drop(columns=columns_to_drop)


categorical_columns = merged_table.select_dtypes(include=['object', 'category']).columns
label_encoder = LabelEncoder()

for col in categorical_columns:
    merged_table[col] = label_encoder.fit_transform(merged_table[col])


""" Predicting status activity (churn rate)"""

# churn rate = (Number of Canceled/Expired Users) / (Total Users)

merged_table['is_churned'] = merged_table['status'].apply(lambda x: 1 if x in [1, 2] else 0)

# as our active status = 0, canceled = 1, expired = 2
# to find churn rate we need canced/exprired percantage

churn_rate = merged_table['is_churned'].mean()
print(f"Churn Rate: {churn_rate:.2%}")


""" Model building """

# Define features  and target
X = merged_table.drop(columns=['status', 'is_churned'])
y = merged_table['is_churned']

#Splitting into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

log_reg_model = LogisticRegression(random_state=42, max_iter=1000)

# Fit the model on training data
log_reg_model.fit(X_train, y_train)

# Predict on the test set
y_pred = log_reg_model.predict(X_test)
y_proba = log_reg_model.predict_proba(X_test)[:, 1]  # Probabilities for the positive class

# Print model coefficients
coefficients = pd.DataFrame(
    {"Feature": X_train.columns, "Coefficient": log_reg_model.coef_[0]}
)
print("Model Coefficients:")
print(coefficients.sort_values(by="Coefficient", ascending=False))


""" Updating results table with predictions"""

# Calculate churn probabilities for all customers
X_full = merged_table.drop(columns=['status', 'is_churned'])
y_proba_full = log_reg_model.predict_proba(X_full)[:, 1]

results['churn_probability'] = y_proba_full

# Define function to update results table in the database
def update_results_table(results_df):
    try:
        with engine.connect() as connection:
            # Write to the database, updating existing rows
            results_df.to_sql('results', con=connection, if_exists='replace', index=False)
            print("Results table updated successfully!")
    except Exception as e:
        print(f"Failed to update results table: {e}")

update_results_table(results)

""" Checking results"""

updated_results = fetch_table_as_dataframe("results")
print(updated_results.head())

