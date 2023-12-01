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


#For each dataframe, drop the last row since it does not represent true data
#In addition, copy the 1st column to the 4th column (overwrite) for the purposes of timestamps on the X axis

dfST10A.drop(dfST10A.tail(1).index,inplace=True)
dfST10A[4] = dfST10A[1].dt.time

dfST10B.drop(dfST10B.tail(1).index,inplace=True)
dfST10B[4] = dfST10B[1].dt.time

dfST20A.drop(dfST20A.tail(1).index,inplace=True)
dfST20A[4] = dfST20A[1].dt.time

dfST20B.drop(dfST20B.tail(1).index,inplace=True)
dfST20B[4] = dfST20B[1].dt.time

dfST30A.drop(dfST30A.tail(1).index,inplace=True)
dfST30A[4] = dfST30A[1].dt.time

dfST30B.drop(dfST30B.tail(1).index,inplace=True)
dfST30B[4] = dfST30B[1].dt.time

dfST40A.drop(dfST40A.tail(1).index,inplace=True)
dfST40A[4] = dfST40A[1].dt.time

dfST40B.drop(dfST40B.tail(1).index,inplace=True)
dfST40B[4] = dfST40B[1].dt.time

dfST50A.drop(dfST50A.tail(1).index,inplace=True)
dfST50A[4] = dfST50A[1].dt.time

dfST50B.drop(dfST50B.tail(1).index,inplace=True)
dfST50B[4] = dfST50B[1].dt.time

dfST60A.drop(dfST60A.tail(1).index,inplace=True)
dfST60A[4] = dfST60A[1].dt.time

dfST60B.drop(dfST60B.tail(1).index,inplace=True)
dfST60B[4] = dfST60B[1].dt.time

dfST71.drop(dfST71.tail(1).index,inplace=True)
dfST71[4] = dfST71[1].dt.time

dfST72.drop(dfST72.tail(1).index,inplace=True)
dfST72[4] = dfST72[1].dt.time

dfST80.drop(dfST80.tail(1).index,inplace=True)
dfST80[4] = dfST80[1].dt.time

dfST90.drop(dfST90.tail(1).index,inplace=True)
dfST90[4] = dfST90[1].dt.time

dfST91.drop(dfST91.tail(1).index,inplace=True)
dfST91[4] = dfST91[1].dt.time

dfST92.drop(dfST92.tail(1).index,inplace=True)
dfST92[4] = dfST92[1].dt.time

dfST100.drop(dfST100.tail(1).index,inplace=True)
dfST100[4] = dfST100[1].dt.time

dfST110.drop(dfST110.tail(1).index,inplace=True)
dfST110[4] = dfST110[1].dt.time

dfST120.drop(dfST120.tail(1).index,inplace=True)
dfST120[4] = dfST120[1].dt.time

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

#df[1] = df[1].dt.time
#df = df.astype({1:'string'})
#df[1] = df[1].apply(time_to_seconds)
#df[2] = df[2].dt.time
#df = df.astype({2:'string'})
#df[2] = df[2].apply(time_to_seconds)

dfST10A[1] = dfST10A[1].dt.time
dfST10A = dfST10A.astype({1:'string'})
dfST10A[1] = dfST10A[1].apply(time_to_seconds)
dfST10A[2] = dfST10A[2].dt.time
dfST10A = dfST10A.astype({2:'string'})
dfST10A[2] = dfST10A[2].apply(time_to_seconds)

dfST10B[1] = dfST10B[1].dt.time
dfST10B = dfST10B.astype({1:'string'})
dfST10B[1] = dfST10B[1].apply(time_to_seconds)
dfST10B[2] = dfST10B[2].dt.time
dfST10B = dfST10B.astype({2:'string'})
dfST10B[2] = dfST10B[2].apply(time_to_seconds)

dfST20A[1] = dfST20A[1].dt.time
dfST20A = dfST20A.astype({1:'string'})
dfST20A[1] = dfST20A[1].apply(time_to_seconds)
dfST20A[2] = dfST20A[2].dt.time
dfST20A = dfST20A.astype({2:'string'})
dfST20A[2] = dfST20A[2].apply(time_to_seconds)

dfST20B[1] = dfST20B[1].dt.time
dfST20B = dfST20B.astype({1:'string'})
dfST20B[1] = dfST20B[1].apply(time_to_seconds)
dfST20B[2] = dfST20B[2].dt.time
dfST20B = dfST20B.astype({2:'string'})
dfST20B[2] = dfST20B[2].apply(time_to_seconds)

dfST30A[1] = dfST30A[1].dt.time
dfST30A = dfST30A.astype({1:'string'})
dfST30A[1] = dfST30A[1].apply(time_to_seconds)
dfST30A[2] = dfST30A[2].dt.time
dfST30A = dfST30A.astype({2:'string'})
dfST30A[2] = dfST30A[2].apply(time_to_seconds)

dfST30B[1] = dfST30B[1].dt.time
dfST30B = dfST30B.astype({1:'string'})
dfST30B[1] = dfST30B[1].apply(time_to_seconds)
dfST30B[2] = dfST30B[2].dt.time
dfST30B = dfST30B.astype({2:'string'})
dfST30B[2] = dfST30B[2].apply(time_to_seconds)

dfST40A[1] = dfST40A[1].dt.time
dfST40A = dfST40A.astype({1:'string'})
dfST40A[1] = dfST40A[1].apply(time_to_seconds)
dfST40A[2] = dfST40A[2].dt.time
dfST40A = dfST40A.astype({2:'string'})
dfST40A[2] = dfST40A[2].apply(time_to_seconds)

dfST40B[1] = dfST40B[1].dt.time
dfST40B = dfST40B.astype({1:'string'})
dfST40B[1] = dfST40B[1].apply(time_to_seconds)
dfST40B[2] = dfST40B[2].dt.time
dfST40B = dfST40B.astype({2:'string'})
dfST40B[2] = dfST40B[2].apply(time_to_seconds)

dfST50A[1] = dfST50A[1].dt.time
dfST50A = dfST50A.astype({1:'string'})
dfST50A[1] = dfST50A[1].apply(time_to_seconds)
dfST50A[2] = dfST50A[2].dt.time
dfST50A = dfST50A.astype({2:'string'})
dfST50A[2] = dfST50A[2].apply(time_to_seconds)

dfST50B[1] = dfST50B[1].dt.time
dfST50B = dfST50B.astype({1:'string'})
dfST50B[1] = dfST50B[1].apply(time_to_seconds)
dfST50B[2] = dfST50B[2].dt.time
dfST50B = dfST50B.astype({2:'string'})
dfST50B[2] = dfST50B[2].apply(time_to_seconds)

dfST60A[1] = dfST60A[1].dt.time
dfST60A = dfST60A.astype({1:'string'})
dfST60A[1] = dfST60A[1].apply(time_to_seconds)
dfST60A[2] = dfST60A[2].dt.time
dfST60A = dfST60A.astype({2:'string'})
dfST60A[2] = dfST60A[2].apply(time_to_seconds)

dfST60B[1] = dfST60B[1].dt.time
dfST60B = dfST60B.astype({1:'string'})
dfST60B[1] = dfST60B[1].apply(time_to_seconds)
dfST60B[2] = dfST60B[2].dt.time
dfST60B = dfST60B.astype({2:'string'})
dfST60B[2] = dfST60B[2].apply(time_to_seconds)

dfST71[1] = dfST71[1].dt.time
dfST71 = dfST71.astype({1:'string'})
dfST71[1] = dfST71[1].apply(time_to_seconds)
dfST71[2] = dfST71[2].dt.time
dfST71 = dfST71.astype({2:'string'})
dfST71[2] = dfST71[2].apply(time_to_seconds)

dfST72[1] = dfST72[1].dt.time
dfST72 = dfST72.astype({1:'string'})
dfST72[1] = dfST72[1].apply(time_to_seconds)
dfST72[2] = dfST72[2].dt.time
dfST72 = dfST72.astype({2:'string'})
dfST72[2] = dfST72[2].apply(time_to_seconds)

dfST80[1] = dfST80[1].dt.time
dfST80 = dfST80.astype({1:'string'})
dfST80[1] = dfST80[1].apply(time_to_seconds)
dfST80[2] = dfST80[2].dt.time
dfST80 = dfST80.astype({2:'string'})
dfST80[2] = dfST80[2].apply(time_to_seconds)

dfST90[1] = dfST90[1].dt.time
dfST90 = dfST90.astype({1:'string'})
dfST90[1] = dfST90[1].apply(time_to_seconds)
dfST90[2] = dfST90[2].dt.time
dfST90 = dfST90.astype({2:'string'})
dfST90[2] = dfST90[2].apply(time_to_seconds)

dfST91[1] = dfST91[1].dt.time
dfST91 = dfST91.astype({1:'string'})
dfST91[1] = dfST91[1].apply(time_to_seconds)
dfST91[2] = dfST91[2].dt.time
dfST91 = dfST91.astype({2:'string'})
dfST91[2] = dfST91[2].apply(time_to_seconds)

dfST92[1] = dfST92[1].dt.time
dfST92 = dfST92.astype({1:'string'})
dfST92[1] = dfST92[1].apply(time_to_seconds)
dfST92[2] = dfST92[2].dt.time
dfST92 = dfST92.astype({2:'string'})
dfST92[2] = dfST92[2].apply(time_to_seconds)

dfST100[1] = dfST100[1].dt.time
dfST100 = dfST100.astype({1:'string'})
dfST100[1] = dfST100[1].apply(time_to_seconds)
dfST100[2] = dfST100[2].dt.time
dfST100 = dfST100.astype({2:'string'})
dfST100[2] = dfST100[2].apply(time_to_seconds)

dfST110[1] = dfST110[1].dt.time
dfST110 = dfST110.astype({1:'string'})
dfST110[1] = dfST110[1].apply(time_to_seconds)
dfST110[2] = dfST110[2].dt.time
dfST110 = dfST110.astype({2:'string'})
dfST110[2] = dfST110[2].apply(time_to_seconds)

dfST120[1] = dfST120[1].dt.time
dfST120 = dfST120.astype({1:'string'})
dfST120[1] = dfST120[1].apply(time_to_seconds)
dfST120[2] = dfST120[2].dt.time
dfST120 = dfST120.astype({2:'string'})
dfST120[2] = dfST120[2].apply(time_to_seconds)

dfST10A[1] = dfST10A[2].subtract(dfST10A[1])
dfST20A[1] = dfST20A[2].subtract(dfST20A[1])
dfST30A[1] = dfST30A[2].subtract(dfST30A[1])
dfST40A[1] = dfST40A[2].subtract(dfST40A[1])
dfST50A[1] = dfST50A[2].subtract(dfST50A[1])
dfST60A[1] = dfST60A[2].subtract(dfST60A[1])
dfST10B[1] = dfST10B[2].subtract(dfST10B[1])
dfST20B[1] = dfST20B[2].subtract(dfST20B[1])
dfST30B[1] = dfST30B[2].subtract(dfST30B[1])
dfST40B[1] = dfST40B[2].subtract(dfST40B[1])
dfST50B[1] = dfST50B[2].subtract(dfST50B[1])
dfST60B[1] = dfST60B[2].subtract(dfST60B[1])
dfST71[1] = dfST71[2].subtract(dfST71[1])
dfST72[1] = dfST72[2].subtract(dfST72[1])
dfST80[1] = dfST80[2].subtract(dfST80[1])
dfST90[1] = dfST90[2].subtract(dfST90[1])
dfST91[1] = dfST91[2].subtract(dfST91[1])
dfST92[1] = dfST92[2].subtract(dfST92[1])
dfST100[1] = dfST100[2].subtract(dfST100[1])
dfST110[1] = dfST110[2].subtract(dfST110[1])
dfST120[1] = dfST120[2].subtract(dfST120[1])

# df_filtered = df[df['Age'] >= 25]
dfST10A = dfST10A[dfST10A[1] <= 600]
dfST20A = dfST20A[dfST20A[1] <= 600]
dfST30A = dfST30A[dfST30A[1] <= 600]
dfST40A = dfST40A[dfST40A[1] <= 600]
dfST50A = dfST50A[dfST50A[1] <= 600]
dfST60A = dfST60A[dfST60A[1] <= 600]
dfST10B = dfST10B[dfST10B[1] <= 600]
dfST20B = dfST20B[dfST20B[1] <= 600]
dfST30B = dfST30B[dfST30B[1] <= 600]
dfST40B = dfST40B[dfST40B[1] <= 600]
dfST50B = dfST50B[dfST50B[1] <= 600]
dfST60B = dfST60B[dfST60B[1] <= 600]
dfST71 = dfST71[dfST71[1] <= 600]
dfST72 = dfST72[dfST72[1] <= 600]
dfST80 = dfST80[dfST80[1] <= 600]
dfST90 = dfST90[dfST90[1] <= 600]
dfST91 = dfST91[dfST91[1] <= 600]
dfST92 = dfST92[dfST92[1] <= 600]
dfST92 = dfST92[dfST92[1] <= 600]
dfST100 = dfST100[dfST100[1] <= 600]
dfST110 = dfST110[dfST110[1] <= 600]
dfST120 = dfST120[dfST120[1] <= 600]

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
                        "x": dfST10A[4],
                        "y": dfST10A[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST10A Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST20A[4],
                        "y": dfST20A[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST20A Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST30A[4],
                        "y": dfST30A[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST30A Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST40A[4],
                        "y": dfST40A[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST40A Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST50A[4],
                        "y": dfST50A[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST50A Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST60A[4],
                        "y": dfST60A[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST60A Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST10B[4],
                        "y": dfST10B[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST10B Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST20B[4],
                        "y": dfST20B[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST20B Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST30B[4],
                        "y": dfST30B[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST30B Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST40B[4],
                        "y": dfST40B[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST40B Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST50B[4],
                        "y": dfST50B[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST50B Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST60B[4],
                        "y": dfST60B[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST60B Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST71[4],
                        "y": dfST71[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST71 Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST72[4],
                        "y": dfST72[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST72 Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST80[4],
                        "y": dfST80[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST80 Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST90[4],
                        "y": dfST90[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST90 Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST91[4],
                        "y": dfST91[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST91 Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST92[4],
                        "y": dfST92[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST92 Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST100[4],
                        "y": dfST100[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST100 Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST110[4],
                        "y": dfST110[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST110 Timestamp vs Duration"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": dfST120[4],
                        "y": dfST120[1],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "ST120 Timestamp vs Duration"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
