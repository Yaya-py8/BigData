import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
 #Remember to run git lfs pull to get the dataset since they're large and can't be kept in github.

artists_df = pd.read_csv('Data/artists.csv')
tracks_df = pd.read_csv('Data/tracks.csv')

print(artists_df.head())
print(tracks_df.head())