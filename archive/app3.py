import pandas as pd
from dash import Dash, dcc, html
from datetime import date

data = (
    pd.read_excel("10-6.xlsx", header=None, sheet_name=["ST10A","ST10B","ST20A","ST20B","ST30A","ST30B","ST40A","ST40B","ST50A",
    "ST50B","ST60A","ST60B","ST71","ST72","ST80","ST90","ST91","ST92","ST100","ST110","ST120"])
    #pd.read_csv("10-6.csv", header=None,skiprows=[0,3899,221,950,2288,3333])
)

df = pd.DataFrame.from_dict(data["ST10A"])
df.drop([0,1,3332,3333])
dfraw = pd.DataFrame.copy(df)
print(df[1])
dfsplit = pd.DataFrame.from_dict(data["ST10A"])
df.drop([0,3333])

# Function to convert time string to seconds
def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

# Apply the function to the 'time' column
df[1] = df[1].dt.time
df = df.astype({1:'string'})
df[1] = df[1].apply(time_to_seconds)
df[2] = df[2].dt.time
df = df.astype({2:'string'})
df[2] = df[2].apply(time_to_seconds)
print(df)
dfsplit[2] = df[2].subtract(df[1])
#dfsplit[2] = pd.to_datetime(dfsplit[2], unit='s').dt.strftime("%H:%M:%S")

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Machine Operation Analysis"),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfraw[1].dt.time,
                        "y": dfsplit[2],
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
