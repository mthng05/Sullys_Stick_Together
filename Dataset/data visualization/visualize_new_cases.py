import pandas as pd
import plotly
import plotly.express as px

data = pd.read_csv('owid-covid-data.csv')

# Filter data for the year 2020
data = data[(data['date'] >= '2020-01-01') & (data['date'] <= '2020-12-31')]

# Filter data for the year 2021
# data = data[(data['date'] >= '2021-01-01') & (data['date'] <= '2021-12-31')]

color_scale_limits = [0, 100000]

fig = px.choropleth(data, locations="iso_code",
                    color="new_cases",
                    hover_name="location",
                    animation_frame="date",
                    projection="natural earth",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    range_color=color_scale_limits)
fig.show()


