import pandas as pd
import numpy as np
import sqlalchemy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from dotenv import load_dotenv

import sys
import os

# Add the parent directory of `app_components` to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))  # Path to `app_components/ds`
project_root = os.path.abspath(os.path.join(current_dir, ".."))  # Path to `app_components`
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from database import *

load_dotenv(".env")

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL)

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

from final_model import *
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import dendrogram, linkage
import seaborn as sns
import matplotlib.pyplot as plt


# Prepare data for clustering
X_clustering = X_full.copy()

# K-Means Clustering

# Elbow Method
inertia = []
k_values = range(1, 11)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_clustering)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia, marker='o', linestyle='--')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.grid()
plt.show()

# Choosing an optimal number of clusters
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
cluster_labels_kmeans = kmeans.fit_predict(X_clustering)


# Silhouette Score for K-Means
silhouette_scores_kmeans = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    cluster_labels = kmeans.fit_predict(X_clustering)
    score = silhouette_score(X_clustering, cluster_labels)
    silhouette_scores_kmeans.append(score)
    print(f"K-Means Silhouette Score for k={k}: {score:.3f}")

# Adding cluster labels to the DataFrame
X_clustering['Cluster_KMeans'] = cluster_labels_kmeans

# Visualizing K-Means Clusters using PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_clustering.drop(columns=['Cluster_KMeans']))
X_clustering_pca = pd.DataFrame(X_pca, columns=['PCA1', 'PCA2'])
X_clustering_pca['Cluster_KMeans'] = cluster_labels_kmeans

plt.figure(figsize=(8, 5))
sns.scatterplot(data=X_clustering_pca, x='PCA1', y='PCA2', hue='Cluster_KMeans', palette='tab10', s=50)
plt.title("K-Means Clusters Visualization (PCA)")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.grid()
plt.legend()
plt.show()

# Hierarchical Clustering

# Plotting the Dendrogram
linked = linkage(X_clustering, method='ward')

plt.figure(figsize=(10, 7))
dendrogram(linked, truncate_mode='lastp', p=10, leaf_rotation=45, leaf_font_size=10)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Number of Points in Node (Cluster Size)")
plt.ylabel("Distance")
plt.grid()
plt.show()

# Applying Agglomerative Clustering
optimal_clusters_hierarchical = 4
hierarchical_clustering = AgglomerativeClustering(n_clusters=optimal_clusters_hierarchical)
cluster_labels_hierarchical = hierarchical_clustering.fit_predict(X_clustering)

X_clustering['Cluster_Hierarchical'] = cluster_labels_hierarchical

# Visualizing Hierarchical Clusters using PCA
X_clustering_pca['Cluster_Hierarchical'] = cluster_labels_hierarchical

plt.figure(figsize=(8, 5))
sns.scatterplot(data=X_clustering_pca, x='PCA1', y='PCA2', hue='Cluster_Hierarchical', palette='tab10', s=50)
plt.title(f"Hierarchical Clusters Visualization (PCA, n_clusters={optimal_clusters_hierarchical})")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.grid()
plt.legend()
plt.show()

""" We will proceed with 4 clusters and K-means clustering"""

customer_clusters = customer.copy()
customer_clusters['Cluster_KMeans'] = cluster_labels_kmeans

# Display customers and their clusters
print("Customers with their K-Means:")
print(customer_clusters[['customer_id', 'Cluster_KMeans']])

"""Printing clustering summary """
X_clustering['Cluster'] = cluster_labels_kmeans
cluster_summary = X_clustering.groupby('Cluster').mean().reset_index()
print(cluster_summary)

cluster_summary.to_csv('cluster_summary.csv', index=False)



""" Updating results table with cluster_numbers"""

results['cluster_number'] = cluster_labels_kmeans

def update_results_with_clusters(results_df):
    try:
        with engine.connect() as connection:
            results_df.to_sql('results', con=connection, if_exists='replace', index=False)
            print("Results table updated successfully with cluster numbers!")
    except Exception as e:
        print(f"Failed to update results table: {e}")

# Update the database
update_results_with_clusters(results)

# Verify the updated results
updated_results = fetch_table_as_dataframe("results")
print(updated_results.head())

