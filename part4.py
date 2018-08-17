# wiesliam
# Imports -- you may add others but do not need to
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import pandas as pd


plotly.tools.set_credentials_file(username='wiesliam', api_key='q7nkkIw92jnXD4npzQ84')

# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets


noun_data = pd.read_csv('noun_data.csv')
table = ff.create_table(noun_data.head())

contents = [go.Bar(x= noun_data['Noun'], y= noun_data['Number'])]
layout = go.Layout(title="Part 1 Most Common Nouns")
final = go.Figure(data=contents, layout=layout)

py.image.save_as(final, filename="part4_viz_image.png")

