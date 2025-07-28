import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Remember to run: git lfs pull 
# to fetch large datasets from GitHub LFS (Large File Storage)

# Load datasets
artists_df = pd.read_csv('Data/artists.csv')
tracks_df = pd.read_csv('Data/tracks.csv')

# Display first few rows of each DataFrame
print("Artists DataFrame:")
print(artists_df.head())

print("\nTracks DataFrame:")
print(tracks_df.head())

# Check for duplicated rows in tracks_df
duplicated_rows = tracks_df.duplicated().sum()

if duplicated_rows == 0:
    print("\n✅ No duplicated rows found in 'tracks_df'. All rows are unique.")
else:
    print(f"\n⚠️ Found {duplicated_rows} duplicated rows in 'tracks_df'. Dropping duplicates...")
    tracks_df = tracks_df.drop_duplicates()
    print(f"Duplicates removed. Remaining rows: {tracks_df.shape[0]}")

audio_features = ['danceability', 'energy', 'loudness', 'speechiness', 
                  'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']

plt.figure(figsize=(12, 8))
sns.heatmap(tracks_df[audio_features].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Between Audio Features')
plt.show()

plt.figure(figsize=(10, 7))
plt.hexbin(tracks_df['danceability'], tracks_df['popularity'], gridsize=50, cmap='viridis', mincnt=1)
plt.colorbar(label='Number of Tracks')
plt.xlabel('Danceability')
plt.ylabel('Popularity')
plt.title('Density of Tracks by Danceability and Popularity')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(tracks_df['loudness'], kde=True, bins=50)
plt.title('Distribution of Track Loudness (dB)')
plt.xlabel('Loudness (dB)')
plt.ylabel('Number of Tracks')
plt.grid(axis='y', alpha=0.75)
plt.show()