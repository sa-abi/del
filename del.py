import pandas as pd
import numpy as np
from scipy.stats import zscore

# Assuming df is your DataFrame with columns 'Sector', 'Client', and 'Incident Rate'

# Step 1: Calculate incident rate mean and standard deviation for each sector
sector_stats = df.groupby('Sector')['Incident Rate'].agg(['mean', 'std']).reset_index()
sector_stats.columns = ['Sector', 'Incident Rate Mean', 'Incident Rate Std']

# Step 2: Merge the calculated statistics back to the original DataFrame
df = pd.merge(df, sector_stats, on='Sector', how='left')

# Step 3: Calculate zscore and is_outlier columns
df['Incident Rate Zscore'] = df.groupby('Sector')['Incident Rate'].transform(lambda x: zscore(x))
df['Is Outlier'] = np.abs(df['Incident Rate Zscore']) > 2

# Display the resulting DataFrame
print(df)
