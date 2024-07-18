import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('/Users/vandana/Downloads/Heart Disease data/Heart Disease data.csv')

# Strip whitespace from column names
data.columns = data.columns.str.strip()

# Display the first few rows of the data
print(data.head())

# Display basic information about the dataset
print(data.info())

# Display summary statistics
print(data.describe())

# Check for missing values
print(data.isnull().sum())

# Display the column names
print("Column names:", data.columns)

# Convert categorical variables to numerical (if necessary)
data = pd.get_dummies(data, columns=['sex', 'thal'], drop_first=True)

# Display the first few rows of the data
print(data.head())

# Display the column names and their data types
print(data.dtypes)

# Display the exact column names to identify any issues
for column in data.columns:
    print(f"'{column}'")

# Display the column names to verify
print(data.columns)

# Visualize the distribution of age
plt.figure(figsize=(10, 6))
sns.histplot(data['age'], kde=True, bins=30)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Visualize heart disease rates by gender
plt.figure(figsize=(10, 6))
sns.countplot(x='sex_1', data=data)
plt.title('Heart Disease by Gender')
plt.xlabel('Gender (0: Female, 1: Male)')
plt.ylabel('Count')
plt.show()

# Visualize the relationship between age and maximum heart rate achieved
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='thalach', hue='sex_1', data=data)
plt.title('Age vs. Maximum Heart Rate Achieved')
plt.xlabel('Age')
plt.ylabel('Maximum Heart Rate Achieved')
plt.show()

# Heatmap to see correlation between different attributes
plt.figure(figsize=(12, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
