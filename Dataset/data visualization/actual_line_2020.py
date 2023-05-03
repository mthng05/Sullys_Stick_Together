import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.backends.backend_pdf
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Lenovo\Covid-19\dataset\my_data2020.csv')

# Group by month and aggregate the new cases column
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

#loop contry
country_list = df['location'].unique()

# Create a PDF file object
pdf_pages = matplotlib.backends.backend_pdf.PdfPages('actual_line_2020.pdf')

# Loop through each country in the country list
for country in country_list:
    # Create a new figure for each country
    fig = plt.figure()

    # Filter the 'df' dataframe for the current country
    new_df = df.loc[df['location'] == country].copy()
        
    # Group by month and aggregate the new cases column
    new_df = new_df.groupby(new_df['date'].dt.month)['new_cases'].sum().reset_index()

    # Create a scatter plot for the current country
    plt.plot(new_df['date'], new_df['new_cases'])
    plt.xlabel('Month' + ' ' + country)
    plt.ylabel('New Cases')

    # Add the current figure to the PDF file
    pdf_pages.savefig(fig, bbox_inches='tight')

    # Close the current figure
    plt.close()

# Close the PDF file
pdf_pages.close()