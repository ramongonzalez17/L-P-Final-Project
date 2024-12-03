import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
file_path = "./data/player_data.csv"  # Replace with the path to your CSV file
df = pd.read_csv(file_path)

# Step 2: Verify the data
print("Data Preview:")
print(df.head())

# Step 3: Standardize the performance metrics
scaler = StandardScaler()
performance_metrics = df[["Rating", "Goals+Assist", "Age"]]
scaled_metrics = scaler.fit_transform(performance_metrics)

# Step 4: Perform PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_metrics)
pca_df = pd.DataFrame(principal_components, columns=["PC1", "PC2"])

# Append PCA results to the original dataframe
df = pd.concat([df, pca_df], axis=1)

# Step 5: Run Linear Regression: Salary vs Performance Metrics
X = df[["Rating", "Goals+Assist", "Age"]]
y = df["Salaries(euros)"]
regressor = LinearRegression()
regressor.fit(X, y)

# Display regression results
print("\nRegression Coefficients:", regressor.coef_)
print("Regression Intercept:", regressor.intercept_)

# Step 6: Visualize PCA Components
plt.figure(figsize=(8, 6))
plt.scatter(pca_df["PC1"], pca_df["PC2"], alpha=0.8)

"""
for i, player in enumerate(df["Player"]):
    plt.annotate(player, (pca_df["PC1"][i], pca_df["PC2"][i]))
"""
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Results")
plt.grid()
plt.show()

# Final output: PCA-transformed data and regression analysis
print("\nPCA-Transformed Data:")
print(df[["Player", "Salaries(euros)", "PC1", "PC2"]])
