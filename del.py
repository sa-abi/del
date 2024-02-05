import pandas as pd

# Sample DataFrame with outputs
outputs_data = {'client': ['Client1', 'Client2', 'Client3'],
                'sector': ['Sector1', 'Sector2', 'Sector3']}
outputs_df = pd.DataFrame(outputs_data)

# Sample DataFrame with client, sector, and date
data = {'client': ['Client1', 'Client1', 'Client1', 'Client2', 'Client2', 'Client2', 'Client3', 'Client3', 'Client3'],
        'sector': ['Sector1', 'Sector1', 'Sector1', 'Sector2', 'Sector2', 'Sector2', 'Sector3', 'Sector3', 'Sector3'],
        'date': ['2024-02-01', '2024-02-02', '2024-02-03', '2024-02-01', '2024-02-02', '2024-02-03', '2024-02-01', '2024-02-02', '2024-02-03']}

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])

# Set a threshold for spike detection (you can adjust this based on your requirements)
threshold = 2

# Initialize an empty list to store results
results = []

# Loop through each unique client and sector combination
for index, row in outputs_df.iterrows():
    client = row['client']
    sector = row['sector']

    # Filter the main DataFrame for the specific client and sector
    client_sector_df = df[(df['client'] == client) & (df['sector'] == sector)]

    # Calculate the count for the last five days
    recent_count = client_sector_df['date'].value_counts().sort_index().tail(5).sum()

    # Determine if there is a spike
    is_spike = recent_count > threshold

    # Record the results in a dictionary
    result_dict = {'client': client,
                   'sector': sector,
                   'recent_date': client_sector_df['date'].max(),
                   'is_spike': is_spike,
                   'spike_count': recent_count}

    # Append the dictionary to the results list
    results.append(result_dict)

# Create a new DataFrame from the results list
output_results_df = pd.DataFrame(results)

# Display the final results
print(output_results_df)
