import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('water_potability.csv')

# Select numeric features relevant to water quality
features = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity']

# Drop rows with missing values for simplicity
df = data[features].dropna()

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Find optimal clusters with Elbow Method
inertia = []
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.plot(range(1, 10), inertia, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal Clusters')
plt.show()

# From elbow plot, pick k=3 (for example)
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

df['Cluster'] = clusters

# Visualize clusters for two features
sns.scatterplot(data=df, x='ph', y='Sulfate', hue='Cluster', palette='Set1')
plt.title('Water Quality Clusters')
plt.show()
