import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('Luqman.csv')

# Box plot
plt.figure(figsize=(10, 6))
df.boxplot(column='F1 Score', by='Size', grid=False)
plt.title('Box Plot of F1 Score for Different Size Levels for Dataset2 with SAM - Bounding Box')
plt.suptitle('')  # Remove default title created by pandas
plt.xlabel('Size Level')
plt.ylabel('F1 Score')
plt.show()