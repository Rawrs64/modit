import pandas as pd
from dash import Dash, dcc, html

data = (
    pd.read_csv("10-6.csv", header=None,skiprows=[0,3899])
    #pd.read_csv("10-6.csv", header=None,skiprows=[0,3899,221,950,2288,3333])
)
data2 = (
    #pd.read_csv("10-6.csv", header=None,skiprows=[0,3899])
    pd.read_csv("10-6.csv", header=None,skiprows=[0,3899,221,950,2288,3333])
)

df = pd.DataFrame.copy(data)
dfsplit = pd.DataFrame.copy(data)
df2 = pd.DataFrame.copy(data2)
dfsplit2 = pd.DataFrame.copy(data2)

# Function to convert time string to seconds
def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

# Apply the function to the 'time' column
df[1] = df[1].apply(time_to_seconds)
df[2] = df[2].apply(time_to_seconds)
dfsplit[2] = df[2].subtract(df[1])
df2[1] = df2[1].apply(time_to_seconds)
df2[2] = df2[2].apply(time_to_seconds)
dfsplit2[2] = df2[2].subtract(df2[1])
#dfsplit[2] = pd.to_datetime(dfsplit[2], unit='s').dt.strftime("%H:%M:%S")

print(data)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Machine Operation Analysis"),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data[1],
                        "y": dfsplit[2],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "10-6 ST10A Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data2[1],
                        "y": dfsplit2[2],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "10-6 ST10A Timestamp vs Duration"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
