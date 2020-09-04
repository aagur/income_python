# Get this figure: fig = py.get_figure("https://plot.ly/~wenbo5565/2/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~wenbo5565/2/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="plot from API", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~wenbo5565/2/").get_data()[0]["y"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "type": "heatmap", 
  "x": ["True:1", "True:0"], 
  "y": ["Predict 0", "Predict 1"], 
  "z": [
    [1752, 193348], [224267, 2009]
}
data = Data([trace1])
layout = {
  "title": "Confusion Matrix", 
  "xaxis": {"title": "True Class"}, 
  "yaxis": {"title": "Predicted Class"}
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)