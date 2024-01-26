import pandas as pd

# Example data
data = {
    'Client': ['A','A','A', 'B', 'B', 'C', 'C', 'D', 'D'],
    'Country': ['USA','India', 'USA', 'Canada', 'Canada', 'UK', 'UK', 'UK', 'USA'],
    'Sector': ['Finance', 'Finance', 'IT', 'IT', 'Healthcare', 'Healthcare', 'IT', 'IT', 'IT'],
    'Observation Category': ['Category1', 'Category2', 'Category1', 'Category2', 'Category1', 'Category2', 'Category2', 'Category1', 'Category2'],
    'Observation Classification': ['Class1', 'Class2', 'Class1', 'Class2', 'Class1', 'Class2', 'Class2', 'Class1', 'Class2'],
    'Incident': [1, 0, 1, 1, 0, 1, 1, 1, 0]
}



df = pd.DataFrame(data)

# Group by 'Client' and 'Country', and calculate the required statistics
table_data = df.groupby(['Client', 'Country'])['Incident'].agg(['count']).reset_index()

# Create new columns as per your request
table_data['Number of 1s'] = df.groupby(['Client', 'Country'])['Incident'].sum().values
table_data['Number of 0s'] = table_data['count'] - table_data['Number of 1s']
table_data['(Number of 0s + Number of 1s)'] = table_data['count']
table_data['Total'] = table_data['Number of 1s'] + table_data['Number of 0s']
table_data['Ratio'] = table_data['Number of 1s'] / table_data['Total']

# Drop unnecessary columns
table_data.drop(['count'], axis=1, inplace=True)

# Sort by ratio in descending order
table_data.sort_values(by='Ratio', ascending=False, inplace=True)

# Displaying the table with highlighting
styled_table = table_data.style.background_gradient(cmap='RdYlGn_r', subset=['Ratio']).format({
    'Number of 1s': '{:.0f}',
    'Number of 0s': '{:.0f}',
    '(Number of 0s + Number of 1s)': '{:.0f}',
    'Total': '{:.0f}',
    'Ratio': '{:.2%}'
})

display(styled_table)