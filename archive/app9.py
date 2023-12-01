import pandas as pd
from dash import Dash, Input, Output, dcc, html
from datetime import date

#Load the data from the excel sheet, all 21 sheets, assign them sheet names, drop all columns but B, C, and D, and skip row 1 due to invalid data
data = (
    pd.read_excel("11-1.xlsx", header=None, usecols="B:D", skiprows=1, sheet_name=["ST10A","ST10B","ST20A","ST20B","ST30A","ST30B","ST40A","ST40B","ST50A",
    "ST50B","ST60A","ST60B","ST71","ST72","ST80","ST90","ST91","ST92","ST100","ST110","ST120"])
)
#Create all data frames contained in the excel sheet
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

dfST10A[2] = dfST10A[2].subtract(dfST10A[1])
dfST20A[2] = dfST20A[2].subtract(dfST20A[1])
dfST30A[2] = dfST30A[2].subtract(dfST30A[1])
dfST40A[2] = dfST40A[2].subtract(dfST40A[1])
dfST50A[2] = dfST50A[2].subtract(dfST50A[1])
dfST60A[2] = dfST60A[2].subtract(dfST60A[1])
dfST10B[2] = dfST10B[2].subtract(dfST10B[1])
dfST20B[2] = dfST20B[2].subtract(dfST20B[1])
dfST30B[2] = dfST30B[2].subtract(dfST30B[1])
dfST40B[2] = dfST40B[2].subtract(dfST40B[1])
dfST50B[2] = dfST50B[2].subtract(dfST50B[1])
dfST60B[2] = dfST60B[2].subtract(dfST60B[1])
dfST71[2] = dfST71[2].subtract(dfST71[1])
dfST72[2] = dfST72[2].subtract(dfST72[1])
dfST80[2] = dfST80[2].subtract(dfST80[1])
dfST90[2] = dfST90[2].subtract(dfST90[1])
dfST91[2] = dfST91[2].subtract(dfST91[1])
dfST92[2] = dfST92[2].subtract(dfST92[1])
dfST100[2] = dfST100[2].subtract(dfST100[1])
dfST110[2] = dfST110[2].subtract(dfST110[1])
dfST120[2] = dfST120[2].subtract(dfST120[1])

#Set the cutoff point for outlier data in the positive y direction
#outlier = 600
#dfST10A = dfST10A[dfST10A[1] <= outlier]
#dfST20A = dfST20A[dfST20A[1] <= outlier]
#dfST30A = dfST30A[dfST30A[1] <= outlier]
#dfST40A = dfST40A[dfST40A[1] <= outlier]
#dfST50A = dfST50A[dfST50A[1] <= outlier]
#dfST60A = dfST60A[dfST60A[1] <= outlier]
#dfST10B = dfST10B[dfST10B[1] <= outlier]
#dfST20B = dfST20B[dfST20B[1] <= outlier]
#dfST30B = dfST30B[dfST30B[1] <= outlier]
#dfST40B = dfST40B[dfST40B[1] <= outlier]
#dfST50B = dfST50B[dfST50B[1] <= outlier]
#dfST60B = dfST60B[dfST60B[1] <= outlier]
#dfST71 = dfST71[dfST71[1] <= outlier]
#dfST72 = dfST72[dfST72[1] <= outlier]
#dfST80 = dfST80[dfST80[1] <= outlier]
#dfST90 = dfST90[dfST90[1] <= outlier]
#dfST91 = dfST91[dfST91[1] <= outlier]
#dfST92 = dfST92[dfST92[1] <= outlier]
#dfST92 = dfST92[dfST92[1] <= outlier]
#dfST100 = dfST100[dfST100[1] <= outlier]
#dfST110 = dfST110[dfST110[1] <= outlier]
#dfST120 = dfST120[dfST120[1] <= outlier]

#Set the cutoff point for the undesired data in the negative y direction
#baseline = 15
#dfST10A = dfST10A[dfST10A[1] > baseline]
#dfST20A = dfST20A[dfST20A[1] > baseline]
#dfST30A = dfST30A[dfST30A[1] > baseline]
#dfST40A = dfST40A[dfST40A[1] > baseline]
#dfST50A = dfST50A[dfST50A[1] > baseline]
#dfST60A = dfST60A[dfST60A[1] > baseline]
#dfST10B = dfST10B[dfST10B[1] > baseline]
#dfST20B = dfST20B[dfST20B[1] > baseline]
#dfST30B = dfST30B[dfST30B[1] > baseline]
#dfST40B = dfST40B[dfST40B[1] > baseline]
#dfST50B = dfST50B[dfST50B[1] > baseline]
#dfST60B = dfST60B[dfST60B[1] > baseline]
#dfST71 = dfST71[dfST71[1] > baseline]
#dfST72 = dfST72[dfST72[1] > baseline]
#dfST80 = dfST80[dfST80[1] > baseline]
#dfST90 = dfST90[dfST90[1] > baseline]
#dfST91 = dfST91[dfST91[1] > baseline]
#dfST92 = dfST92[dfST92[1] > baseline]
#dfST100 = dfST100[dfST100[1] > baseline]
#dfST110 = dfST110[dfST110[1] > baseline]
#dfST120 = dfST120[dfST120[1] > baseline]

machines = ["Station 10A", "Station 20A", "Station 30A", "Station 40A", "Station 50A", "Station 60A", "Station 10B", "Station 20B", "Station 30B", "Station 40B", "Station 50B",
            "Station 60B", "Station 71", "Station 72", "Station 80", "Station 90", "Station 91", "Station 92", "Station 100", "Station 110", "Station 120"]
            
timeHours = ["6 AM" , "7 AM", "8 AM", "9 AM", "10 AM", "12 PM", "1 PM", "2 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM", "8 PM", "9 PM", "10 PM", "11 PM", "12 AM"]

dropLowerThan = ["0 Seconds", "5 Seconds", "10 Seconds", "15 Seconds", "20 Seconds", "25 Seconds", "30 Seconds", "35 Seconds", "40 Seconds", "45 Seconds", "50 Seconds", "55 Seconds", "60 Seconds"]

dropHigherThan = ["1 hr", "30 min", "15 min", "10 min", "5 min"]

#print(dfST10A)

#Convert 
#df = df.astype({1:'string'})
#df[1] = df[1].apply(time_to_seconds)
#df[2] = df[2].dt.time
#df = df.astype({2:'string'})
#df[2] = df[2].apply(time_to_seconds)
#print(dfST10A)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    children="M.O.D.I.T. Analytics", className="header-title"
                ),
                html.P(
                    children=(
                        "Analyze the machine performance data and the"
                        " productivity codes per hour"
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Machine", className="menu-title"),
                        dcc.Dropdown(
                            id="machine-filter",
                            options=[
                                {"label": machine, "value": machine}
                                for machine in machines
                            ],
                            value="Station 10A",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(
                            children="Time Start", className="menu-title"
                        ),
                        dcc.Dropdown(
                            id="time-start-filter",
                            options=[
                                {"label": timestart, "value": timestart}
                                for timestart in timeHours
                            ],
                            value="6 AM",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(
                            children="Time End", className="menu-title"
                        ),
                        dcc.Dropdown(
                            id="time-end-filter",
                            options=[
                                {"label": timeend, "value": timeend}
                                for timeend in timeHours
                            ],
                            value="12 AM",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(
                            children="Drop Values Lower Than", className="menu-title"
                        ),
                        dcc.Dropdown(
                            id="lower-end-filter",
                            options=[
                                {"label": droplower, "value": droplower}
                                for droplower in dropLowerThan
                            ],
                            value="0 Seconds",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(
                            children="Drop Values Higher Than", className="menu-title"
                        ),
                        dcc.Dropdown(
                            id="higher-end-filter",
                            options=[
                                {"label": drophigher, "value": drophigher}
                                for drophigher in dropHigherThan
                            ],
                            value="1 hr",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="machine-performance-chart",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="machine-throughput",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

@app.callback(
    Output("machine-performance-chart", "figure"),
    Output("machine-throughput", "figure"),
    Input("machine-filter", "value"),
    Input("time-start-filter", "value"),
    Input("time-end-filter", "value"),
    Input("lower-end-filter", "value"),
    Input("higher-end-filter", "value"),
)

def update_charts(machine, timeStart, timeEnd, lowerEnd, higherEnd):
    #Machine selection
    if machine == "Station 10A":
        filtered_data = dfST10A.copy()
    elif machine == "Station 20A":
        filtered_data = dfST20A.copy()
    elif machine == "Station 30A":
        filtered_data = dfST30A.copy()
    elif machine == "Station 40A":
        filtered_data = dfST40A.copy()
    elif machine == "Station 50A":
        filtered_data = dfST50A.copy()
    elif machine == "Station 60A":
        filtered_data = dfST60A.copy()
    elif machine == "Station 10B":
        filtered_data = dfST10B.copy()
    elif machine == "Station 20B":
        filtered_data = dfST20B.copy()
    elif machine == "Station 30B":
        filtered_data = dfST30B.copy()
    elif machine == "Station 40B":
        filtered_data = dfST40B.copy()
    elif machine == "Station 50B":
        filtered_data = dfST50B.copy()
    elif machine == "Station 60B":
        filtered_data = dfST60B.copy()
    elif machine == "Station 71":
        filtered_data = dfST71.copy()
    elif machine == "Station 72":
        filtered_data = dfST72.copy()
    elif machine == "Station 80":
        filtered_data = dfST80.copy()
    elif machine == "Station 90":
        filtered_data = dfST90.copy()
    elif machine == "Station 91":
        filtered_data = dfST91.copy()
    elif machine == "Station 92":
        filtered_data = dfST92.copy()
    elif machine == "Station 100":
        filtered_data = dfST100.copy()
    elif machine == "Station 110":
        filtered_data = dfST110.copy()
    else:
        filtered_data = dfST120.copy()
        
    #Codes per hour filter
    codesSixSeven = len(filtered_data[(filtered_data[1] < 25200) & (filtered_data[1] >= 21600) & (filtered_data[3] == "1 - Productive")])
    codesSevenEight = len(filtered_data[(filtered_data[1] < 28800) & (filtered_data[1] >= 25200) & (filtered_data[3] == "1 - Productive")])
    codesEightNine = len(filtered_data[(filtered_data[1] < 32400) & (filtered_data[1] >= 28800) & (filtered_data[3] == "1 - Productive")])
    codesNineTen = len(filtered_data[(filtered_data[1] < 36000) & (filtered_data[1] >= 32400) & (filtered_data[3] == "1 - Productive")])
    codesTenEleven = len(filtered_data[(filtered_data[1] < 39600) & (filtered_data[1] >= 36000) & (filtered_data[3] == "1 - Productive")])
    codesElevenTwelve = len(filtered_data[(filtered_data[1] < 43200) & (filtered_data[1] >= 39600) & (filtered_data[3] == "1 - Productive")])
    codesTwelveThirteen = len(filtered_data[(filtered_data[1] < 46800) & (filtered_data[1] >= 43200) & (filtered_data[3] == "1 - Productive")])
    codesThirteenFourteen = len(filtered_data[(filtered_data[1] < 50400) & (filtered_data[1] >= 46800) & (filtered_data[3] == "1 - Productive")])
    codesFourteenFifteen = len(filtered_data[(filtered_data[1] < 54000) & (filtered_data[1] >= 50400) & (filtered_data[3] == "1 - Productive")])
    codesFifteenSixteen = len(filtered_data[(filtered_data[1] < 57600) & (filtered_data[1] >= 54000) & (filtered_data[3] == "1 - Productive")])
    codesSixteenSeventeen = len(filtered_data[(filtered_data[1] < 61200) & (filtered_data[1] >= 57600) & (filtered_data[3] == "1 - Productive")])
    codesSeventeenEighteen = len(filtered_data[(filtered_data[1] < 64800) & (filtered_data[1] >= 61200) & (filtered_data[3] == "1 - Productive")])
    codesEighteenNineteen = len(filtered_data[(filtered_data[1] < 68400) & (filtered_data[1] >= 64800) & (filtered_data[3] == "1 - Productive")])
    codesNineteenTwenty = len(filtered_data[(filtered_data[1] < 72000) & (filtered_data[1] >= 68400) & (filtered_data[3] == "1 - Productive")])
    codesTwentyTwentyone = len(filtered_data[(filtered_data[1] < 75600) & (filtered_data[1] >= 72000) & (filtered_data[3] == "1 - Productive")])
    codesTwentyoneTwentytwo = len(filtered_data[(filtered_data[1] < 79200) & (filtered_data[1] >= 75600) & (filtered_data[3] == "1 - Productive")])
    codesTwentytwoTwentythree = len(filtered_data[(filtered_data[1] < 82800) & (filtered_data[1] >= 79200) & (filtered_data[3] == "1 - Productive")])
    codesTwentythreeTwentyfour = len(filtered_data[(filtered_data[1] < 86400) & (filtered_data[1] >= 82800) & (filtered_data[3] == "1 - Productive")])
        
    #Lower bound filter
    if lowerEnd == "0 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 0]
    elif lowerEnd == "5 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 5]
    elif lowerEnd == "10 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 10]
    elif lowerEnd == "15 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 15]
    elif lowerEnd == "20 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 20]
    elif lowerEnd == "25 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 25]
    elif lowerEnd == "30 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 30]
    elif lowerEnd == "35 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 35]
    elif lowerEnd == "40 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 40]
    elif lowerEnd == "45 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 45]
    elif lowerEnd == "50 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 50]
    elif lowerEnd == "55 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 55]
    elif lowerEnd == "60 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 60]
    else:
        filtered_data = filtered_data[filtered_data[2] > 0]
    
    #Upper bound filter
    if higherEnd == "1 hr":
        filtered_data = filtered_data[filtered_data[2] <= 3600]
    elif machine == "30 min":
        filtered_data = filtered_data[filtered_data[2] <= 1800]
    elif machine == "15 min":
        filtered_data = filtered_data[filtered_data[2] <= 900]
    elif machine == "10 min":
        filtered_data = filtered_data[filtered_data[2] <= 600]
    else:
        filtered_data = filtered_data[filtered_data[2] <= 300]
    
    #Time start filter
    if timeStart == "6 AM":
        filtered_data = filtered_data[filtered_data[1] >= 21600]
    elif timeStart == "7 AM":
        filtered_data = filtered_data[filtered_data[1] >= 25200]
    elif timeStart == "8 AM":
        filtered_data = filtered_data[filtered_data[1] >= 28800]
    elif timeStart == "9 AM":
        filtered_data = filtered_data[filtered_data[1] >= 32400]
    elif timeStart == "10 AM":
        filtered_data = filtered_data[filtered_data[1] >= 36000]
    elif timeStart == "11 AM":
        filtered_data = filtered_data[filtered_data[1] >= 39600]
    elif timeStart == "12 PM":
        filtered_data = filtered_data[filtered_data[1] >= 43200]
    elif timeStart == "1 PM":
        filtered_data = filtered_data[filtered_data[1] >= 46800]
    elif timeStart == "2 PM":
        filtered_data = filtered_data[filtered_data[1] >= 50400]
    elif timeStart == "3 PM":
        filtered_data = filtered_data[filtered_data[1] >= 54000]
    elif timeStart == "4 PM":
        filtered_data = filtered_data[filtered_data[1] >= 57600]
    elif timeStart == "5 PM":
        filtered_data = filtered_data[filtered_data[1] >= 61200]
    elif timeStart == "6 PM":
        filtered_data = filtered_data[filtered_data[1] >= 64800]
    elif timeStart == "7 PM":
        filtered_data = filtered_data[filtered_data[1] >= 68400]
    elif timeStart == "8 PM":
        filtered_data = filtered_data[filtered_data[1] >= 72000]
    elif timeStart == "9 PM":
        filtered_data = filtered_data[filtered_data[1] >= 75600]
    elif timeStart == "10 PM":
        filtered_data = filtered_data[filtered_data[1] >= 79200]
    elif timeStart == "11 PM":
        filtered_data = filtered_data[filtered_data[1] >= 82800]
    else:
        filtered_data = filtered_data[filtered_data[1] >= 86400]
    
    #Time end filter
    if timeEnd == "6 AM":
        filtered_data = filtered_data[filtered_data[1] <= 21600]
    elif timeEnd == "7 AM":
        filtered_data = filtered_data[filtered_data[1] <= 25200]
    elif timeEnd == "8 AM":
        filtered_data = filtered_data[filtered_data[1] <= 28800]
    elif timeEnd == "9 AM":
        filtered_data = filtered_data[filtered_data[1] <= 32400]
    elif timeEnd == "10 AM":
        filtered_data = filtered_data[filtered_data[1] <= 36000]
    elif timeEnd == "11 AM":
        filtered_data = filtered_data[filtered_data[1] <= 39600]
    elif timeEnd == "12 PM":
        filtered_data = filtered_data[filtered_data[1] <= 43200]
    elif timeEnd == "1 PM":
        filtered_data = filtered_data[filtered_data[1] <= 46800]
    elif timeEnd == "2 PM":
        filtered_data = filtered_data[filtered_data[1] <= 50400]
    elif timeEnd == "3 PM":
        filtered_data = filtered_data[filtered_data[1] <= 54000]
    elif timeEnd == "4 PM":
        filtered_data = filtered_data[filtered_data[1] <= 57600]
    elif timeEnd == "5 PM":
        filtered_data = filtered_data[filtered_data[1] <= 61200]
    elif timeEnd == "6 PM":
        filtered_data = filtered_data[filtered_data[1] <= 64800]
    elif timeEnd == "7 PM":
        filtered_data = filtered_data[filtered_data[1] <= 68400]
    elif timeEnd == "8 PM":
        filtered_data = filtered_data[filtered_data[1] <= 72000]
    elif timeEnd == "9 PM":
        filtered_data = filtered_data[filtered_data[1] <= 75600]
    elif timeEnd == "10 PM":
        filtered_data = filtered_data[filtered_data[1] <= 79200]
    elif timeEnd == "11 PM":
        filtered_data = filtered_data[filtered_data[1] <= 82800]
    else:
        filtered_data = filtered_data[filtered_data[1] <= 86400]
        
    
    
    
    machine_performance_chart = {
        "data": [
            {
                "x": filtered_data[4],
                "y": filtered_data[2],
                "type": "lines",
                #"hovertemplate": "$%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Time Spent On Machine Process",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"ticksuffix": " Seconds", "fixedrange": True},
            "colorway": ["#17B897"],
        },
    }

    machine_throughput = {
        "data": [
                {'x': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                'y': [codesSixSeven, codesSevenEight, codesEightNine, codesNineTen, codesTenEleven, codesElevenTwelve, codesTwelveThirteen, codesThirteenFourteen, codesFourteenFifteen,
                codesFifteenSixteen, codesSixteenSeventeen, codesSeventeenEighteen, codesEighteenNineteen, codesNineteenTwenty, codesTwentyTwentyone, codesTwentyoneTwentytwo, codesTwentytwoTwentythree,
                codesTwentythreeTwentyfour], 'type': 'bar', 'name': 'SF'},
        ],
        "layout": {
            "title": {"text": "Productivity Per Hour For This Machine", "x": 0.05, "xanchor": "left"},
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#E12D39"],
        },
    }
    return machine_performance_chart, machine_throughput



if __name__ == "__main__":
    app.run_server(debug=True)
