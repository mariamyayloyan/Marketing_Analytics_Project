from final_model import *
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import dendrogram, linkage
import seaborn as sns
import matplotlib.pyplot as plt

"""
This module implements clustering techniques using K-Means and Hierarchical Clustering.
"""

""" Preparing data for clustering """
X_clustering = X_full.copy()

""" K-Means Clustering """

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

""" Visualizing K-Means Clusters using PCA """
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

""" Hierarchical Clustering """

# Plotting the Dendrogram
linked = linkage(X_clustering, method='ward')

plt.figure(figsize=(10, 7))
dendrogram(linked, truncate_mode='lastp', p=10, leaf_rotation=45, leaf_font_size=10)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Number of Points in Node (Cluster Size)")
plt.ylabel("Distance")
plt.grid()
plt.show()

""" Applying Agglomerative Clustering """

optimal_clusters_hierarchical = 4
hierarchical_clustering = AgglomerativeClustering(n_clusters=optimal_clusters_hierarchical)
cluster_labels_hierarchical = hierarchical_clustering.fit_predict(X_clustering)

X_clustering['Cluster_Hierarchical'] = cluster_labels_hierarchical

""" Visualizing Hierarchical Clusters using PCA """
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

def update_results_with_clusters(results_df: pd.DataFrame) -> None:
    """
       Update the results table with cluster assignments.

       Args:
           results_df (pd.DataFrame): The DataFrame containing the results to update.

       Returns:
           None
       """
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