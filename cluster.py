import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Step 1: Load the dataset from the CSV file
file_path = "./data/player_data.csv"  # Replace with the path to your CSV file
df = pd.read_csv(file_path)

# Step 2: Standardize the performance metrics
scaler = StandardScaler()
performance_metrics = df[["Rating", "Goals+Assist", "Age"]]  # Features to be used for PCA
scaled_metrics = scaler.fit_transform(performance_metrics)

# Step 3: Perform PCA
pca = PCA(n_components=2)  # Reduce to 2 principal components
principal_components = pca.fit_transform(scaled_metrics)
pca_df = pd.DataFrame(principal_components, columns=["PC1", "PC2"])

# Step 4: Perform K-Means Clustering on the PCA-transformed data
kmeans = KMeans(n_clusters=3, random_state=42)  # Adjust `n_clusters` as needed
pca_df["Cluster"] = kmeans.fit_predict(pca_df[["PC1", "PC2"]])

# Step 5: Visualize the clustering results
plt.figure(figsize=(8, 6))
colors = ["red", "blue", "green"]  # Colors for clusters
for cluster in range(3):  # Number of clusters
    cluster_points = pca_df[pca_df["Cluster"] == cluster]
    plt.scatter(cluster_points["PC1"], cluster_points["PC2"], label=f"Cluster {cluster}", alpha=0.8)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("K-Means Clustering on PCA Components")
plt.legend()
plt.grid()
plt.show()

# Step 6: Merge the clusters with the original dataset
df["Cluster"] = kmeans.labels_

# Step 7: Save the clustered data to a new CSV file
output_file_path = "clustered_data.csv"  # Specify the output file path
df.to_csv(output_file_path, index=False)

# Display the first few rows of the clustered data
print("Clustered Data Preview:")
print(df.head())
# Preview the clustered data in the console
clustered_preview = df[["Player", "Rating", "Goals+Assist", "Salaries(euros)", "Age", "Cluster"]]
print("\nClustered Data Preview:")
print(clustered_preview.head(250))  # Show the first 20 rows (or adjust as needed)
# Save the full clustered data to a new CSV file
output_file_path = "clustered_players.csv"  # Specify the desired output file name
df.to_csv(output_file_path, index=False)

print(f"\nClustered data has been saved to {output_file_path}")
