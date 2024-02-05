import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df is your DataFrame with the calculated columns

# Plotting a histogram
plt.figure(figsize=(10, 6))
ax = sns.histplot(df['Incident Rate'], bins=20, kde=True, color='blue')

# Highlighting specific values
highlight_values = [8.79, 6.95]
for value in highlight_values:
    ax.annotate(f'{value}', xy=(value, 0), xytext=(value, 5),
                arrowprops=dict(facecolor='red', shrink=0.05),
                color='red', fontsize=10, ha='center')

plt.title('Incident Rate Distribution')
plt.xlabel('Incident Rate')
plt.ylabel('Frequency')
plt.show()
