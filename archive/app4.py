import pandas as pd
from dash import Dash, dcc, html
from datetime import date

#Load the data from the excel sheet, all 21 sheets, assign them sheet names, drop all columns but B, C, and D, and skip row 1 due to invalid data
data = (
    pd.read_excel("10-6.xlsx", header=None, usecols="B:D", skiprows=1, sheet_name=["ST10A","ST10B","ST20A","ST20B","ST30A","ST30B","ST40A","ST40B","ST50A",
    "ST50B","ST60A","ST60B","ST71","ST72","ST80","ST90","ST91","ST92","ST100","ST110","ST120"])
)

#Create a list of all data frames contained in the excel sheet
dfST10A = pd.DataFrame.from_dict(data["ST10A"])
dfST10B = pd.DataFrame.from_dict(data["ST10B"])
dfST20A = pd.DataFrame.from_dict(data["ST20A"])
dfST20B = pd.DataFrame.from_dict(data["ST20B"])
dfST30A = pd.DataFrame.from_dict(data["ST30A"])
dfST30B = pd.DataFrame.from_dict(data["ST30B"])
dfST40A = pd.DataFrame.from_dict(data["ST40A"])
dfST40B = pd.DataFrame.from_dict(data["ST40B"])
dfST50A = pd.DataFrame.from_dict(data["ST50A"])
dfST50B = pd.DataFrame.from_dict(data["ST50B"])
dfST60A = pd.DataFrame.from_dict(data["ST60A"])
dfST60B = pd.DataFrame.from_dict(data["ST60B"])
dfST71 = pd.DataFrame.from_dict(data["ST71"])
dfST72 = pd.DataFrame.from_dict(data["ST72"])
dfST80 = pd.DataFrame.from_dict(data["ST80"])
dfST90 = pd.DataFrame.from_dict(data["ST90"])
dfST91 = pd.DataFrame.from_dict(data["ST91"])
dfST92 = pd.DataFrame.from_dict(data["ST92"])
dfST100 = pd.DataFrame.from_dict(data["ST100"])
dfST110 = pd.DataFrame.from_dict(data["ST110"])
dfST120 = pd.DataFrame.from_dict(data["ST120"])

list_of_df = [
dfST10A,
dfST10B,
dfST20A,
dfST20B,
dfST30A,
dfST30B,
dfST40A,
dfST40B,
dfST50A,
dfST50B,
dfST60A,
dfST60B,
dfST71,
dfST72,
dfST80,
dfST90,
dfST91,
dfST92,
dfST100,
dfST110,
dfST120]

#For each dataframe, drop the last row since it does not represent true data
#In addition, copy the 1st column to the 4th column (overwrite) for the purposes of timestamps on the X axis
for df in list_of_df:
    df.drop(df.tail(1).index,inplace=True)
    df[4] = df[1].dt.time

#dfraw = pd.DataFrame.copy(df)

#Caveman debugging print data
#print(df[1])

# Function to convert time string to seconds
def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

#Apply the function to the 'time' column
#df[1] = df[1].dt.time

#For each dataframe in the list
#Convert columns 1 & 2 to time format
#Convert time format to type string
#Apply time to seconds function to each data point
for df in list_of_df:
    df[1] = df[1].dt.time
    df = df.astype({1:'string'})
    df[1] = df[1].apply(time_to_seconds)
    df[2] = df[2].dt.time
    df = df.astype({2:'string'})
    df[2] = df[2].apply(time_to_seconds)

#Convert 
#df = df.astype({1:'string'})
#df[1] = df[1].apply(time_to_seconds)
#df[2] = df[2].dt.time
#df = df.astype({2:'string'})
#df[2] = df[2].apply(time_to_seconds)
#print(df)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Machine Operation Analysis"),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": list_of_df[1][4],
                        "y": list_of_df[1][2].subtract(list_of_df[1][1]),
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
                "layout": {"title": "10-6 ST20A Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST30A Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST40A Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST50A Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST60A Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST10B Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST20B Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST30B Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST40B Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST50B Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST60B Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST71 Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST72 Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST80 Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST90 Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST91 Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST92 Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST100 Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST110 Timestamp vs Duration"},
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
                "layout": {"title": "10-6 ST120 Timestamp vs Duration"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
