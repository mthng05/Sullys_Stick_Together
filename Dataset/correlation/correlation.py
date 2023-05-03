import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

# data = pd.read_csv('my_data2020.csv')
data = pd.read_csv('my_data2021.csv')

location = ['Vietnam', 'Brazil', 'India', 'United States', 'China']
for i in location:
    country_data = data[data['location'] == i]

    # Calculate correlation matrix
    matrix = country_data.corr(numeric_only=True)

    # plot heatmap
    fig, ax = plt.subplots(figsize=(6, 6))
    fig.subplots_adjust(left = 0.3, bottom = 0.3)
    sns.heatmap(matrix, annot=True, cmap='Set3')
    # plt.title('Correlation Matrix of ' + i + ' in 2020')
    # plt.title('Correlation Matrix of ' + i + ' in 2021')
    # plt.savefig(i + '_2020.png')
    plt.savefig(i + '_2021.png')
    plt.show()
    
# --------------------------------------------
# # Select top 2 attributes with highest correlation
# data = pd.read_csv('my_data2020.csv')
# # data = pd.read_csv('my_data2021.csv')

# # Group data by location
# groups = data.groupby('location')

# # Create empty dictionary to store correlations for each location
# correlations = {}

# # Loop through each location and calculate correlation matrix
# for name, group in groups:
#     matrix = group.corr(numeric_only=True)

#     # Get correlations with new_cases column
#     corr_pairs = matrix['new_cases'].drop(['new_cases'])
    
#     # Select top 2 attributes with highest correlation
#     top_attributes = corr_pairs.abs().nlargest(2).index.tolist()

#     # Add top attributes to dictionary
#     correlations[name] = top_attributes

# # Create DataFrame from top attributes
# df = pd.DataFrame.from_dict(correlations, orient='index', columns=['attribute_1', 'attribute_2'])

# print(df)





