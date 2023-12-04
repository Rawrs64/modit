import pandas as pd
import dash
from dash import Dash, Input, Output, dcc, html, exceptions, State
import plotly.graph_objs as go
from datetime import date
import datetime

is_input_received = False
data = None

def load_excel_data():
    global is_input_received, data

    if not is_input_received:
        file_name_without_extension = input("Please enter the excel worksheet name (without the '.xlsx' extension): ")
        file_name = f"{file_name_without_extension}.xlsx"
        print("Loading data...")
        try:
            data = pd.read_excel(file_name, header=None, usecols="B:D", skiprows=1, 
                                 sheet_name=["ST10A","ST10B","ST20A","ST20B","ST30A","ST30B","ST40A","ST40B","ST50A",
                                             "ST50B","ST60A","ST60B","ST71","ST72","ST80","ST90","ST91","ST92","ST100","ST110","ST120"])
            is_input_received = True
            print("Data loaded successfully")
            print("Loading application...")
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Please check the file name and try again.")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
    else:
        print("Data already loaded")


load_excel_data()

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


# Function to convert time string to seconds
def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

#Apply the function to the 'time' column
#df[1] = df[1].dt.time

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

#By subtracting columns, you get the duration of the status code
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

#List of strings for the selection of the primary machine to examine
machines = ["Station 10A", "Station 20A", "Station 30A", "Station 40A", "Station 50A", "Station 60A", "Station 10B", "Station 20B", "Station 30B", "Station 40B", "Station 50B",
            "Station 60B", "Station 71", "Station 72", "Station 80", "Station 90", "Station 91", "Station 92", "Station 100", "Station 110", "Station 120"]

#List of strings for the selection of the throughout comparison machine filter
machines_throughput_names = ["Station 10A", "Station 20A", "Station 30A", "Station 40A", "Station 50A", "Station 60A", "Station 10B", "Station 20B", "Station 30B", "Station 40B", "Station 50B",
            "Station 60B", "Station 71", "Station 72", "Station 80", "Station 90", "Station 91", "Station 92", "Station 100", "Station 110", "Station 120"]

#List of strings for the time start selection filter
timeHours = ["6 AM" , "7 AM", "8 AM", "9 AM", "10 AM", "12 PM", "1 PM", "2 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM", "8 PM", "9 PM", "10 PM", "11 PM", "12 AM"]

#List of strings for dropping nominal data filter (any duration below the selected amount)
dropLowerThan = ["0 Seconds", "5 Seconds", "10 Seconds", "15 Seconds", "20 Seconds", "25 Seconds", "30 Seconds", "35 Seconds", "40 Seconds", "45 Seconds", "50 Seconds", "55 Seconds", "60 Seconds"]

#List of strings for dropping outlier data filter (any duration above the selected amount)
dropHigherThan = ["1 hr", "30 min", "15 min", "10 min", "5 min"]

#Default app name
app = Dash(__name__)

#HTML layout of the website
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                #Primary title header
                html.H1(
                    children="M.O.D.I.T. Analytics", className="header-title"
                ),
                #Secondary title subheader
                html.P(
                    children=(
                        "Analyze the machine performance data and the"
                        " throughput per hour"
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
                    #Layout of the primary machine filter
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
                        html.Div(children="Machine To Compare Throughput", className="menu-title"),
                        dcc.Dropdown(
                            id="machine-filter-throughput",
                            options=[
                                {"label": machine_throughput, "value": machine_throughput}
                                for machine_throughput in machines_throughput_names
                            ],
                            value="Station 10B",
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
                html.Button('Apply Preset Filters', id='preset-filter-button')
            ],
            className="menu",
        ),
        
        # Tabs for switching between graphs
        dcc.Tabs(id='tabs', value='tab-1', children=[
            dcc.Tab(label='Single Machine Performace', value='tab-1'),
            dcc.Tab(label='Machine Throughput Comparison', value='tab-2'),
            dcc.Tab(label='Performance For All Machines', value='tab-3'),
        ]),

        # Placeholder for the content of the selected tab
        html.Div(id='tabs-content')
    ]
)

def seconds_to_datetime(seconds):
    #Convert seconds since midnight into a datetime object
    base_date = datetime.date.today()
    time_of_day = datetime.timedelta(seconds=seconds)
    return datetime.datetime.combine(base_date, (datetime.datetime.min + time_of_day).time())

machinesLines = []



@app.callback(
    [Output("machine-filter", 'value'), 
     Output("machine-filter-throughput", 'value'),
     Output("time-start-filter", 'value'),
     Output("time-end-filter", 'value'),
     Output("lower-end-filter", 'value'),
     Output("higher-end-filter", 'value'),
    ],
    [Input('preset-filter-button', 'n_clicks')],
)
def apply_preset_filters(n_clicks):
    if n_clicks is None:
        # No clicks yet, don't update the filters
        raise dash.exceptions.PreventUpdate

    # Preset filter values here
    preset_machine_filter = "Station 50A"
    preset_machine_throughput_filter = "Station 50B"
    preset_time_start_filter = "12 PM"
    preset_time_end_filter = "3 PM"
    preset_lower_end_filter = "15 Seconds"
    preset_higher_end_filter = "5 min"

    return [preset_machine_filter, 
            preset_machine_throughput_filter, 
            preset_time_start_filter,
            preset_time_end_filter,
            preset_lower_end_filter,
            preset_higher_end_filter]

@app.callback(
    Output('tabs-content', 'children'),
    [Input('tabs', 'value'),
     Input("machine-filter", "value"),
     Input("machine-filter-throughput", "value"),
     Input("time-start-filter", "value"),
     Input("time-end-filter", "value"),
     Input("lower-end-filter", "value"),
     Input("higher-end-filter", "value")]
)

def update_charts(tab, machine, machine_throughput, timeStart, timeEnd, lowerEnd, higherEnd):
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
        
    hover_text_copy = filtered_data.copy()
        
    #Machine throughput comparison selection
    if machine_throughput == "Station 10A":
        filtered_data_throughput = dfST10A.copy()
    elif machine_throughput == "Station 20A":
        filtered_data_throughput = dfST20A.copy()
    elif machine_throughput == "Station 30A":
        filtered_data_throughput = dfST30A.copy()
    elif machine_throughput == "Station 40A":
        filtered_data_throughput = dfST40A.copy()
    elif machine_throughput == "Station 50A":
        filtered_data_throughput = dfST50A.copy()
    elif machine_throughput == "Station 60A":
        filtered_data_throughput = dfST60A.copy()
    elif machine_throughput == "Station 10B":
        filtered_data_throughput = dfST10B.copy()
    elif machine_throughput == "Station 20B":
        filtered_data_throughput = dfST20B.copy()
    elif machine_throughput == "Station 30B":
        filtered_data_throughput = dfST30B.copy()
    elif machine_throughput == "Station 40B":
        filtered_data_throughput = dfST40B.copy()
    elif machine_throughput == "Station 50B":
        filtered_data_throughput = dfST50B.copy()
    elif machine_throughput == "Station 60B":
        filtered_data_throughput = dfST60B.copy()
    elif machine_throughput == "Station 71":
        filtered_data_throughput = dfST71.copy()
    elif machine_throughput == "Station 72":
        filtered_data_throughput = dfST72.copy()
    elif machine_throughput == "Station 80":
        filtered_data_throughput = dfST80.copy()
    elif machine_throughput == "Station 90":
        filtered_data_throughput = dfST90.copy()
    elif machine_throughput == "Station 91":
        filtered_data_throughput = dfST91.copy()
    elif machine_throughput == "Station 92":
        filtered_data_throughput = dfST92.copy()
    elif machine_throughput == "Station 100":
        filtered_data_throughput = dfST100.copy()
    elif machine_throughput == "Station 110":
        filtered_data_throughput = dfST110.copy()
    else:
        filtered_data_throughput = dfST120.copy()
        
        
    dfST10ACpy = dfST10A.copy()
    dfST20ACpy = dfST20A.copy()
    dfST30ACpy = dfST30A.copy()
    dfST40ACpy = dfST40A.copy()
    dfST50ACpy = dfST50A.copy()
    dfST60ACpy = dfST60A.copy()
    dfST10BCpy = dfST10B.copy()
    dfST20BCpy = dfST20B.copy()
    dfST30BCpy = dfST30B.copy()
    dfST40BCpy = dfST40B.copy()
    dfST50BCpy = dfST50B.copy()
    dfST60BCpy = dfST60B.copy()
    dfST71Cpy = dfST71.copy()
    dfST72Cpy = dfST72.copy()
    dfST80Cpy = dfST80.copy()
    dfST90Cpy = dfST90.copy()
    dfST91Cpy = dfST91.copy()
    dfST92Cpy = dfST92.copy()
    dfST100Cpy = dfST100.copy()
    dfST110Cpy = dfST110.copy()
    dfST120Cpy = dfST120.copy()
        
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
    
    #Codes per hour filter for comparison machine
    compareSixSeven = len(filtered_data_throughput[(filtered_data_throughput[1] < 25200) & (filtered_data_throughput[1] >= 21600) & (filtered_data_throughput[3] == "1 - Productive")])
    compareSevenEight = len(filtered_data_throughput[(filtered_data_throughput[1] < 28800) & (filtered_data_throughput[1] >= 25200) & (filtered_data_throughput[3] == "1 - Productive")])
    compareEightNine = len(filtered_data_throughput[(filtered_data_throughput[1] < 32400) & (filtered_data_throughput[1] >= 28800) & (filtered_data_throughput[3] == "1 - Productive")])
    compareNineTen = len(filtered_data_throughput[(filtered_data_throughput[1] < 36000) & (filtered_data_throughput[1] >= 32400) & (filtered_data_throughput[3] == "1 - Productive")])
    compareTenEleven = len(filtered_data_throughput[(filtered_data_throughput[1] < 39600) & (filtered_data_throughput[1] >= 36000) & (filtered_data_throughput[3] == "1 - Productive")])
    compareElevenTwelve = len(filtered_data_throughput[(filtered_data_throughput[1] < 43200) & (filtered_data_throughput[1] >= 39600) & (filtered_data_throughput[3] == "1 - Productive")])
    compareTwelveThirteen = len(filtered_data_throughput[(filtered_data_throughput[1] < 46800) & (filtered_data_throughput[1] >= 43200) & (filtered_data_throughput[3] == "1 - Productive")])
    compareThirteenFourteen = len(filtered_data_throughput[(filtered_data_throughput[1] < 50400) & (filtered_data_throughput[1] >= 46800) & (filtered_data_throughput[3] == "1 - Productive")])
    compareFourteenFifteen = len(filtered_data_throughput[(filtered_data_throughput[1] < 54000) & (filtered_data_throughput[1] >= 50400) & (filtered_data_throughput[3] == "1 - Productive")])
    compareFifteenSixteen = len(filtered_data_throughput[(filtered_data_throughput[1] < 57600) & (filtered_data_throughput[1] >= 54000) & (filtered_data_throughput[3] == "1 - Productive")])
    compareSixteenSeventeen = len(filtered_data_throughput[(filtered_data_throughput[1] < 61200) & (filtered_data_throughput[1] >= 57600) & (filtered_data_throughput[3] == "1 - Productive")])
    compareSeventeenEighteen = len(filtered_data_throughput[(filtered_data_throughput[1] < 64800) & (filtered_data_throughput[1] >= 61200) & (filtered_data_throughput[3] == "1 - Productive")])
    compareEighteenNineteen = len(filtered_data_throughput[(filtered_data_throughput[1] < 68400) & (filtered_data_throughput[1] >= 64800) & (filtered_data_throughput[3] == "1 - Productive")])
    compareNineteenTwenty = len(filtered_data_throughput[(filtered_data_throughput[1] < 72000) & (filtered_data_throughput[1] >= 68400) & (filtered_data_throughput[3] == "1 - Productive")])
    compareTwentyTwentyone = len(filtered_data_throughput[(filtered_data_throughput[1] < 75600) & (filtered_data_throughput[1] >= 72000) & (filtered_data_throughput[3] == "1 - Productive")])
    compareTwentyoneTwentytwo = len(filtered_data_throughput[(filtered_data_throughput[1] < 79200) & (filtered_data_throughput[1] >= 75600) & (filtered_data_throughput[3] == "1 - Productive")])
    compareTwentytwoTwentythree = len(filtered_data_throughput[(filtered_data_throughput[1] < 82800) & (filtered_data_throughput[1] >= 79200) & (filtered_data_throughput[3] == "1 - Productive")])
    compareTwentythreeTwentyfour = len(filtered_data_throughput[(filtered_data_throughput[1] < 86400) & (filtered_data_throughput[1] >= 82800) & (filtered_data_throughput[3] == "1 - Productive")])
        
    #Lower bound filter
    if lowerEnd == "0 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 0]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] > 0]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] > 0]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] > 0]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] > 0]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] > 0]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] > 0]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] > 0]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] > 0]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] > 0]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] > 0]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] > 0]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] > 0]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] > 0]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] > 0]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] > 0]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] > 0]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] > 0]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] > 0]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] > 0]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] > 0]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] > 0]
    elif lowerEnd == "5 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 5]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] > 5]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] > 5]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] > 5]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] > 5]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] > 5]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] > 5]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] > 5]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] > 5]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] > 5]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] > 5]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] > 5]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] > 5]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] > 5]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] > 5]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] > 5]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] > 5]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] > 5]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] > 5]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] > 5]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] > 5]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] > 5]
    elif lowerEnd == "10 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 10]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] > 10]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] > 10]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] > 10]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] > 10]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] > 10]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] > 10]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] > 10]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] > 10]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] > 10]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] > 10]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] > 10]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] > 10]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] > 10]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] > 10]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] > 10]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] > 10]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] > 10]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] > 10]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] > 10]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] > 10]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] > 10]
    elif lowerEnd == "15 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 15]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] > 15]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] > 15]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] > 15]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] > 15]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] > 15]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] > 15]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] > 15]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] > 15]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] > 15]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] > 15]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] > 15]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] > 15]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] > 15]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] > 15]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] > 15]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] > 15]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] > 15]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] > 15]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] > 15]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] > 15]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] > 15]
    elif lowerEnd == "20 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 20]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] > 20]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] > 20]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] > 20]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] > 20]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] > 20]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] > 20]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] > 20]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] > 20]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] > 20]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] > 20]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] > 20]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] > 20]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] > 20]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] > 20]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] > 20]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] > 20]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] > 20]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] > 20]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] > 20]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] > 20]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] > 20]
    elif lowerEnd == "25 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 25]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] > 25]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] > 25]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] > 25]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] > 25]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] > 25]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] > 25]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] > 25]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] > 25]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] > 25]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] > 25]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] > 25]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] > 25]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] > 25]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] > 25]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] > 25]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] > 25]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] > 25]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] > 25]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] > 25]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] > 25]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] > 25]
    elif lowerEnd == "30 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 30]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] > 30]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] > 30]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] > 30]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] > 30]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] > 30]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] > 30]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] > 30]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] > 30]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] > 30]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] > 30]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] > 30]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] > 30]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] > 30]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] > 30]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] > 30]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] > 30]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] > 30]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] > 30]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] > 30]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] > 30]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] > 30]
    elif lowerEnd == "35 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 35]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] > 35]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] > 35]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] > 35]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] > 35]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] > 35]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] > 35]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] > 35]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] > 35]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] > 35]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] > 35]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] > 35]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] > 35]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] > 35]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] > 35]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] > 35]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] > 35]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] > 35]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] > 35]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] > 35]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] > 35]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] > 35]
    elif lowerEnd == "40 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 40]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] > 40]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] > 40]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] > 40]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] > 40]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] > 40]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] > 40]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] > 40]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] > 40]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] > 40]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] > 40]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] > 40]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] > 40]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] > 40]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] > 40]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] > 40]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] > 40]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] > 40]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] > 40]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] > 40]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] > 40]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] > 40]
    elif lowerEnd == "45 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 45]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] > 45]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] > 45]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] > 45]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] > 45]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] > 45]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] > 45]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] > 45]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] > 45]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] > 45]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] > 45]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] > 45]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] > 45]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] > 45]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] > 45]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] > 45]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] > 45]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] > 45]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] > 45]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] > 45]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] > 45]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] > 45]
    elif lowerEnd == "50 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 50]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] > 50]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] > 50]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] > 50]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] > 50]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] > 50]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] > 50]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] > 50]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] > 50]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] > 50]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] > 50]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] > 50]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] > 50]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] > 50]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] > 50]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] > 50]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] > 50]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] > 50]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] > 50]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] > 50]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] > 50]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] > 50]
    elif lowerEnd == "55 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 55]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] > 55]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] > 55]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] > 55]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] > 55]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] > 55]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] > 55]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] > 55]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] > 55]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] > 55]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] > 55]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] > 55]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] > 55]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] > 55]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] > 55]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] > 55]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] > 55]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] > 55]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] > 55]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] > 55]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] > 55]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] > 55]
    elif lowerEnd == "60 Seconds":
        filtered_data = filtered_data[filtered_data[2] > 60]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] > 60]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] > 60]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] > 60]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] > 60]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] > 60]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] > 60]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] > 60]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] > 60]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] > 60]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] > 60]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] > 60]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] > 60]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] > 60]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] > 60]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] > 60]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] > 60]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] > 60]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] > 60]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] > 60]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] > 60]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] > 60]
    else:
        filtered_data = filtered_data[filtered_data[2] > 0]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] > 0]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] > 0]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] > 0]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] > 0]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] > 0]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] > 0]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] > 0]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] > 0]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] > 0]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] > 0]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] > 0]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] > 0]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] > 0]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] > 0]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] > 0]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] > 0]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] > 0]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] > 0]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] > 0]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] > 0]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] > 0]
    
    #Upper bound filter
    if higherEnd == "1 hr":
        filtered_data = filtered_data[filtered_data[2] <= 3600]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] <= 3600]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] <= 3600]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] <= 3600]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] <= 3600]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] <= 3600]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] <= 3600]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] <= 3600]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] <= 3600]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] <= 3600]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] <= 3600]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] <= 3600]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] <= 3600]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] <= 3600]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] <= 3600]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] <= 3600]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] <= 3600]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] <= 3600]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] <= 3600]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] <= 3600]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] <= 3600]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] <= 3600]
    elif machine == "30 min":
        filtered_data = filtered_data[filtered_data[2] <= 1800]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] <= 1800]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] <= 1800]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] <= 1800]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] <= 1800]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] <= 1800]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] <= 1800]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] <= 1800]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] <= 1800]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] <= 1800]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] <= 1800]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] <= 1800]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] <= 1800]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] <= 1800]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] <= 1800]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] <= 1800]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] <= 1800]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] <= 1800]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] <= 1800]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] <= 1800]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] <= 1800]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] <= 1800]
    elif machine == "15 min":
        filtered_data = filtered_data[filtered_data[2] <= 900]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] <= 900]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] <= 900]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] <= 900]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] <= 900]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] <= 900]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] <= 900]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] <= 900]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] <= 900]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] <= 900]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] <= 900]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] <= 900]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] <= 900]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] <= 900]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] <= 900]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] <= 900]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] <= 900]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] <= 900]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] <= 900]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] <= 900]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] <= 900]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] <= 900]
    elif machine == "10 min":
        filtered_data = filtered_data[filtered_data[2] <= 600]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] <= 600]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] <= 600]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] <= 600]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] <= 600]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] <= 600]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] <= 600]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] <= 600]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] <= 600]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] <= 600]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] <= 600]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] <= 600]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] <= 600]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] <= 600]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] <= 600]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] <= 600]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] <= 600]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] <= 600]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] <= 600]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] <= 600]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] <= 600]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] <= 600]
    else:
        filtered_data = filtered_data[filtered_data[2] <= 300]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[2] <= 300]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[2] <= 300]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[2] <= 300]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[2] <= 300]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[2] <= 300]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[2] <= 300]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[2] <= 300]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[2] <= 300]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[2] <= 300]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[2] <= 300]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[2] <= 300]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[2] <= 300]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[2] <= 300]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[2] <= 300]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[2] <= 300]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[2] <= 300]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[2] <= 300]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[2] <= 300]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[2] <= 300]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[2] <= 300]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[2] <= 300]
    
    #Time start filter
    if timeStart == "6 AM":
        filtered_data = filtered_data[filtered_data[1] >= 21600]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 21600]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 21600]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 21600]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 21600]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 21600]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 21600]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 21600]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 21600]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 21600]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 21600]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 21600]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 21600]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 21600]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 21600]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 21600]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 21600]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 21600]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 21600]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 21600]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 21600]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 21600]
        rangeStart = 21600
    elif timeStart == "7 AM":
        filtered_data = filtered_data[filtered_data[1] >= 25200]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 25200]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 25200]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 25200]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 25200]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 25200]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 25200]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 25200]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 25200]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 25200]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 25200]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 25200]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 25200]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 25200]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 25200]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 25200]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 25200]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 25200]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 25200]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 25200]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 25200]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 25200]
        rangeStart = 25200
    elif timeStart == "8 AM":
        filtered_data = filtered_data[filtered_data[1] >= 28800]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 28800]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 28800]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 28800]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 28800]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 28800]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 28800]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 28800]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 28800]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 28800]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 28800]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 28800]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 28800]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 28800]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 28800]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 28800]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 28800]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 28800]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 28800]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 28800]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 28800]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 28800]
        rangeStart = 28800
    elif timeStart == "9 AM":
        filtered_data = filtered_data[filtered_data[1] >= 32400]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 32400]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 32400]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 32400]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 32400]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 32400]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 32400]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 32400]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 32400]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 32400]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 32400]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 32400]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 32400]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 32400]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 32400]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 32400]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 32400]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 32400]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 32400]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 32400]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 32400]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 32400]
        rangeStart = 32400
    elif timeStart == "10 AM":
        filtered_data = filtered_data[filtered_data[1] >= 36000]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 36000]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 36000]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 36000]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 36000]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 36000]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 36000]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 36000]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 36000]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 36000]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 36000]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 36000]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 36000]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 36000]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 36000]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 36000]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 36000]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 36000]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 36000]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 36000]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 36000]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 36000]
        rangeStart = 36000
    elif timeStart == "11 AM":
        filtered_data = filtered_data[filtered_data[1] >= 39600]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 39600]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 39600]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 39600]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 39600]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 39600]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 39600]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 39600]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 39600]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 39600]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 39600]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 39600]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 39600]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 39600]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 39600]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 39600]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 39600]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 39600]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 39600]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 39600]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 39600]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 39600]
        rangeStart = 39600
    elif timeStart == "12 PM":
        filtered_data = filtered_data[filtered_data[1] >= 43200]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 43200]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 43200]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 43200]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 43200]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 43200]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 43200]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 43200]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 43200]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 43200]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 43200]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 43200]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 43200]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 43200]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 43200]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 43200]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 43200]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 43200]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 43200]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 43200]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 43200]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 43200]
        rangeStart = 43200
    elif timeStart == "1 PM":
        filtered_data = filtered_data[filtered_data[1] >= 46800]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 46800]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 46800]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 46800]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 46800]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 46800]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 46800]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 46800]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 46800]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 46800]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 46800]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 46800]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 46800]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 46800]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 46800]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 46800]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 46800]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 46800]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 46800]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 46800]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 46800]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 46800]
        rangeStart =46800
    elif timeStart == "2 PM":
        filtered_data = filtered_data[filtered_data[1] >= 50400]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 50400]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 50400]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 50400]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 50400]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 50400]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 50400]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 50400]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 50400]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 50400]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 50400]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 50400]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 50400]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 50400]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 50400]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 50400]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 50400]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 50400]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 50400]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 50400]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 50400]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 50400]
        rangeStart = 50400
    elif timeStart == "3 PM":
        filtered_data = filtered_data[filtered_data[1] >= 54000]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 54000]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 54000]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 54000]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 54000]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 54000]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 54000]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 54000]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 54000]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 54000]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 54000]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 54000]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 54000]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 54000]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 54000]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 54000]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 54000]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 54000]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 54000]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 54000]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 54000]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 54000]
        rangeStart = 54000
    elif timeStart == "4 PM":
        filtered_data = filtered_data[filtered_data[1] >= 57600]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 57600]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 57600]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 57600]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 57600]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 57600]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 57600]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 57600]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 57600]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 57600]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 57600]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 57600]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 57600]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 57600]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 57600]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 57600]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 57600]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 57600]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 57600]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 57600]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 57600]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 57600]
        rangeStart = 57600
    elif timeStart == "5 PM":
        filtered_data = filtered_data[filtered_data[1] >= 61200]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 61200]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 61200]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 61200]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 61200]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 61200]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 61200]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 61200]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 61200]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 61200]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 61200]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 61200]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 61200]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 61200]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 61200]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 61200]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 61200]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 61200]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 61200]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 61200]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 61200]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 61200]
        rangeStart = 61200
    elif timeStart == "6 PM":
        filtered_data = filtered_data[filtered_data[1] >= 64800]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 64800]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 64800]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 64800]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 64800]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 64800]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 64800]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 64800]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 64800]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 64800]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 64800]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 64800]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 64800]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 64800]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 64800]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 64800]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 64800]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 64800]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 64800]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 64800]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 64800]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 64800]
        rangeStart = 64800
    elif timeStart == "7 PM":
        filtered_data = filtered_data[filtered_data[1] >= 68400]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 68400]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 68400]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 68400]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 68400]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 68400]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 68400]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 68400]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 68400]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 68400]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 68400]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 68400]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 68400]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 68400]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 68400]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 68400]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 68400]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 68400]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 68400]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 68400]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 68400]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 68400]
        rangeStart = 68400
    elif timeStart == "8 PM":
        filtered_data = filtered_data[filtered_data[1] >= 72000]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 72000]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 72000]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 72000]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 72000]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 72000]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 72000]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 72000]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 72000]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 72000]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 72000]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 72000]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 72000]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 72000]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 72000]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 72000]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 72000]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 72000]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 72000]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 72000]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 72000]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 72000]
        rangeStart = 72000
    elif timeStart == "9 PM":
        filtered_data = filtered_data[filtered_data[1] >= 75600]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 75600]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 75600]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 75600]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 75600]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 75600]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 75600]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 75600]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 75600]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 75600]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 75600]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 75600]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 75600]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 75600]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 75600]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 75600]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 75600]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 75600]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 75600]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 75600]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 75600]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 75600]
        rangeStart = 75600
    elif timeStart == "10 PM":
        filtered_data = filtered_data[filtered_data[1] >= 79200]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 79200]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 79200]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 79200]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 79200]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 79200]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 79200]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 79200]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 79200]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 79200]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 79200]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 79200]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 79200]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 79200]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 79200]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 79200]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 79200]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 79200]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 79200]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 79200]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 79200]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 79200]
        rangeStart = 79200
    elif timeStart == "11 PM":
        filtered_data = filtered_data[filtered_data[1] >= 82800]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 82800]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 82800]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 82800]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 82800]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 82800]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 82800]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 82800]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 82800]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 82800]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 82800]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 82800]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 82800]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 82800]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 82800]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 82800]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 82800]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 82800]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 82800]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 82800]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 82800]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 82800]
        rangeStart = 82800
    else:
        filtered_data = filtered_data[filtered_data[1] >= 86400]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] >= 86400]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] >= 86400]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] >= 86400]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] >= 86400]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] >= 86400]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] >= 86400]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] >= 86400]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] >= 86400]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] >= 86400]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] >= 86400]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] >= 86400]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] >= 86400]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] >= 86400]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] >= 86400]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] >= 86400]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] >= 86400]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] >= 86400]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] >= 86400]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] >= 86400]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] >= 86400]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] >= 86400]
        rangeStart = 86400
    
    #Time end filter
    if timeEnd == "6 AM":
        filtered_data = filtered_data[filtered_data[1] <= 21600]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 21600]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 21600]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 21600]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 21600]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 21600]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 21600]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 21600]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 21600]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 21600]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 21600]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 21600]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 21600]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 21600]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 21600]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 21600]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 21600]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 21600]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 21600]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 21600]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 21600]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 21600]
        rangeEnd = 21600
    elif timeEnd == "7 AM":
        filtered_data = filtered_data[filtered_data[1] <= 25200]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 25200]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 25200]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 25200]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 25200]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 25200]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 25200]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 25200]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 25200]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 25200]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 25200]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 25200]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 25200]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 25200]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 25200]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 25200]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 25200]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 25200]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 25200]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 25200]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 25200]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 25200]
        rangeEnd = 25200
    elif timeEnd == "8 AM":
        filtered_data = filtered_data[filtered_data[1] <= 28800]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 28800]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 28800]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 28800]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 28800]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 28800]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 28800]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 28800]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 28800]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 28800]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 28800]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 28800]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 28800]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 28800]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 28800]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 28800]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 28800]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 28800]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 28800]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 28800]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 28800]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 28800]
        rangeEnd = 28800
    elif timeEnd == "9 AM":
        filtered_data = filtered_data[filtered_data[1] <= 32400]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 32400]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 32400]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 32400]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 32400]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 32400]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 32400]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 32400]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 32400]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 32400]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 32400]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 32400]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 32400]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 32400]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 32400]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 32400]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 32400]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 32400]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 32400]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 32400]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 32400]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 32400]
        rangeEnd = 32400
    elif timeEnd == "10 AM":
        filtered_data = filtered_data[filtered_data[1] <= 36000]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 36000]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 36000]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 36000]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 36000]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 36000]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 36000]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 36000]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 36000]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 36000]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 36000]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 36000]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 36000]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 36000]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 36000]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 36000]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 36000]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 36000]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 36000]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 36000]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 36000]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 36000]
        rangeEnd = 36000
    elif timeEnd == "11 AM":
        filtered_data = filtered_data[filtered_data[1] <= 39600]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 39600]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 39600]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 39600]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 39600]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 39600]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 39600]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 39600]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 39600]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 39600]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 39600]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 39600]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 39600]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 39600]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 39600]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 39600]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 39600]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 39600]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 39600]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 39600]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 39600]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 39600]
        rangeEnd = 39600
    elif timeEnd == "12 PM":
        filtered_data = filtered_data[filtered_data[1] <= 43200]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 43200]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 43200]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 43200]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 43200]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 43200]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 43200]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 43200]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 43200]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 43200]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 43200]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 43200]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 43200]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 43200]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 43200]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 43200]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 43200]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 43200]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 43200]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 43200]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 43200]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 43200]
        rangeEnd = 43200
    elif timeEnd == "1 PM":
        filtered_data = filtered_data[filtered_data[1] <= 46800]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 46800]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 46800]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 46800]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 46800]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 46800]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 46800]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 46800]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 46800]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 46800]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 46800]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 46800]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 46800]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 46800]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 46800]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 46800]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 46800]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 46800]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 46800]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 46800]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 46800]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 46800]
        rangeEnd = 46800
    elif timeEnd == "2 PM":
        filtered_data = filtered_data[filtered_data[1] <= 50400]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 50400]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 50400]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 50400]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 50400]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 50400]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 50400]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 50400]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 50400]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 50400]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 50400]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 50400]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 50400]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 50400]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 50400]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 50400]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 50400]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 50400]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 50400]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 50400]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 50400]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 50400]
        rangeEnd = 50400
    elif timeEnd == "3 PM":
        filtered_data = filtered_data[filtered_data[1] <= 54000]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 54000]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 54000]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 54000]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 54000]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 54000]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 54000]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 54000]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 54000]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 54000]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 54000]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 54000]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 54000]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 54000]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 54000]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 54000]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 54000]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 54000]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 54000]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 54000]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 54000]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 54000]
        rangeEnd = 54000
    elif timeEnd == "4 PM":
        filtered_data = filtered_data[filtered_data[1] <= 57600]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 57600]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 57600]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 57600]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 57600]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 57600]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 57600]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 57600]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 57600]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 57600]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 57600]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 57600]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 57600]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 57600]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 57600]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 57600]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 57600]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 57600]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 57600]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 57600]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 57600]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 57600]
        rangeEnd = 57600
    elif timeEnd == "5 PM":
        filtered_data = filtered_data[filtered_data[1] <= 61200]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 61200]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 61200]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 61200]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 61200]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 61200]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 61200]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 61200]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 61200]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 61200]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 61200]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 61200]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 61200]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 61200]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 61200]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 61200]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 61200]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 61200]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 61200]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 61200]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 61200]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 61200]
        rangeEnd = 61200
    elif timeEnd == "6 PM":
        filtered_data = filtered_data[filtered_data[1] <= 64800]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 64800]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 64800]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 64800]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 64800]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 64800]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 64800]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 64800]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 64800]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 64800]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 64800]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 64800]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 64800]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 64800]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 64800]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 64800]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 64800]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 64800]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 64800]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 64800]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 64800]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 64800]
        rangeEnd = 64800
    elif timeEnd == "7 PM":
        filtered_data = filtered_data[filtered_data[1] <= 68400]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 68400]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 68400]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 68400]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 68400]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 68400]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 68400]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 68400]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 68400]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 68400]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 68400]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 68400]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 68400]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 68400]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 68400]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 68400]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 68400]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 68400]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 68400]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 68400]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 68400]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 68400]
        rangeEnd = 68400
    elif timeEnd == "8 PM":
        filtered_data = filtered_data[filtered_data[1] <= 72000]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 72000]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 72000]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 72000]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 72000]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 72000]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 72000]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 72000]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 72000]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 72000]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 72000]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 72000]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 72000]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 72000]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 72000]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 72000]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 72000]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 72000]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 72000]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 72000]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 72000]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 72000]
        rangeEnd = 72000
    elif timeEnd == "9 PM":
        filtered_data = filtered_data[filtered_data[1] <= 75600]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 75600]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 75600]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 75600]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 75600]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 75600]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 75600]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 75600]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 75600]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 75600]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 75600]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 75600]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 75600]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 75600]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 75600]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 75600]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 75600]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 75600]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 75600]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 75600]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 75600]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 75600]
        rangeEnd = 75600
    elif timeEnd == "10 PM":
        filtered_data = filtered_data[filtered_data[1] <= 79200]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 79200]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 79200]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 79200]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 79200]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 79200]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 79200]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 79200]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 79200]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 79200]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 79200]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 79200]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 79200]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 79200]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 79200]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 79200]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 79200]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 79200]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 79200]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 79200]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 79200]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 79200]
        rangeEnd = 79200
    elif timeEnd == "11 PM":
        filtered_data = filtered_data[filtered_data[1] <= 82800]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 82800]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 82800]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 82800]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 82800]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 82800]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 82800]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 82800]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 82800]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 82800]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 82800]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 82800]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 82800]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 82800]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 82800]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 82800]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 82800]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 82800]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 82800]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 82800]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 82800]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 82800]
        rangeEnd = 82800
    else:
        filtered_data = filtered_data[filtered_data[1] <= 86400]
        dfST10ACpy = dfST10ACpy[dfST10ACpy[1] <= 86400]
        dfST20ACpy = dfST20ACpy[dfST20ACpy[1] <= 86400]
        dfST30ACpy = dfST30ACpy[dfST30ACpy[1] <= 86400]
        dfST40ACpy = dfST40ACpy[dfST40ACpy[1] <= 86400]
        dfST50ACpy = dfST50ACpy[dfST50ACpy[1] <= 86400]
        dfST60ACpy = dfST60ACpy[dfST60ACpy[1] <= 86400]
        dfST10BCpy = dfST10BCpy[dfST10BCpy[1] <= 86400]
        dfST20BCpy = dfST20BCpy[dfST20BCpy[1] <= 86400]
        dfST30BCpy = dfST30BCpy[dfST30BCpy[1] <= 86400]
        dfST40BCpy = dfST40BCpy[dfST40BCpy[1] <= 86400]
        dfST50BCpy = dfST50BCpy[dfST50BCpy[1] <= 86400]
        dfST60BCpy = dfST60BCpy[dfST60BCpy[1] <= 86400]
        dfST71Cpy = dfST71Cpy[dfST71Cpy[1] <= 86400]
        dfST72Cpy = dfST72Cpy[dfST72Cpy[1] <= 86400]
        dfST80Cpy = dfST80Cpy[dfST80Cpy[1] <= 86400]
        dfST90Cpy = dfST90Cpy[dfST90Cpy[1] <= 86400]
        dfST91Cpy = dfST91Cpy[dfST91Cpy[1] <= 86400]
        dfST92Cpy = dfST92Cpy[dfST92Cpy[1] <= 86400]
        dfST100Cpy = dfST100Cpy[dfST100Cpy[1] <= 86400]
        dfST110Cpy = dfST110Cpy[dfST110Cpy[1] <= 86400]
        dfST120Cpy = dfST120Cpy[dfST120Cpy[1] <= 86400]
        rangeEnd = 86400
        
    #print(dfST10ACpy.columns)
    machinesLines = []
    machine_names = ["ST10A", "ST20A", "ST30A", "ST40A", "ST50A", "ST60A",
                 "ST10B", "ST20B", "ST30B", "ST40B", "ST50B", "ST60B",
                 "ST71", "ST72", "ST80", "ST90", "ST91", "ST92", "ST100", "ST110", "ST120"]
                 
    # Define a list of colors for the lines
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5',
          '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5',
          '#393b79',
         ]

    # List of corresponding dataframes
    dataframes = [dfST10ACpy, dfST20ACpy, dfST30ACpy, dfST40ACpy, dfST50ACpy, dfST60ACpy,
              dfST10BCpy, dfST20BCpy, dfST30BCpy, dfST40BCpy, dfST50BCpy, dfST60BCpy,
              dfST71Cpy, dfST72Cpy, dfST80Cpy, dfST90Cpy, dfST91Cpy, dfST92Cpy, dfST100Cpy, dfST110Cpy, dfST120Cpy]


    
    
    # Append lines for each machine
    for name, df, color in zip(machine_names, dataframes, colors):
    
        time_values = df[1].apply(seconds_to_datetime)
        
        hover_text = (
        'Station: ' + name + 
        '<br>Time: ' + df[4].astype(str) + 
        '<br>Duration: %{y}' + 
        '<br>Status Code: ' + df[3].astype(str)
        )
        machinesLines.append(go.Scatter(
            x=time_values,
            y=df[2],
            mode='lines',
            name=name,
            line=dict(color=color),
            hovertemplate=hover_text + '<extra></extra>'
        ))
    
    setRange = range(rangeStart, rangeEnd)
    
    hover_text_copy
    
    # Get a list of the indices from the filtered DataFrame
    index_list = filtered_data.index.tolist()

    # Create a list to hold the hover text strings
    hover_texts = []
    
    for index, row in filtered_data.iterrows():
        # Find the current position in the filtered DataFrame
        current_position = index_list.index(index)

        # Find the corresponding index in hover_text_copy
        hover_text_copy_index = hover_text_copy.index.get_loc(index)

        # Indices for Previous Status Codes in hover_text_copy
        previous_indices = [hover_text_copy.index[i] if i >= 0 else None for i in range(hover_text_copy_index-1, max(hover_text_copy_index-6, -1), -1)]
        previous_status_codes = [str(hover_text_copy.loc[idx, 3]) if idx is not None else 'N/A' for idx in previous_indices]

        # Indices for Post Status Codes in hover_text_copy
        post_indices = [hover_text_copy.index[i] if i < len(hover_text_copy) else None for i in range(hover_text_copy_index+1, min(hover_text_copy_index+4, len(hover_text_copy)))]
        post_status_codes = [str(hover_text_copy.loc[idx, 3]) if idx is not None else 'N/A' for idx in post_indices]
        
        #Index for iteration over previous status codes for descending order implementation
        start_index = len(previous_status_codes)

        # Constructing the hover text
        hover_text = (
            'Station: ' + machine +
            '<br>Time: ' + str(row[4]) +
            '<br>Duration: ' + str(row[2]) + '<br>' +
            ''.join(['<br>Previous Status Code {}: {}'.format(start_index - j, code) for j, code in enumerate(previous_status_codes)]) +
            '<br>' + '<br>Current Status Code: ' + str(row[3]) + '<br>' +
            ''.join(['<br>Post Status Code {}: {}'.format(j+1, code) for j, code in enumerate(post_status_codes)])
        )
        hover_texts.append(hover_text)
    
    #Layout for the single machine performance graph
    machine_performance_chart = {
        "data": [
            {
                "x": filtered_data[4],
                "y": filtered_data[2],
                "type": "lines",
                "hovertemplate": '%{text}<extra></extra>',
                "text": hover_texts
            },
        ],
        "layout": {
            "title": {
                "text": "Time Spent On Station Process",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"ticksuffix": " Seconds", "fixedrange": True},
            "colorway": ["#17B897"],
        },
    }
    
    #Layout for the all machines line graph
    all_machines = {
        "data": machinesLines,
        "layout": {
            "title": {
                "text": "All Stations With Given Filters",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {
                "fixedrange": True,
                "type": "time",
                "tickformat": "%H:%M:%S"
            },
            "yaxis": {
                "ticksuffix": " Seconds", 
                "fixedrange": True
            },
            "showlegend": True,
        },
    }
    
    #Place all the throughput values of machine one into a list
    codes_data = [codesSixSeven, codesSevenEight, codesEightNine, codesNineTen, codesTenEleven, 
                codesElevenTwelve, codesTwelveThirteen, codesThirteenFourteen, codesFourteenFifteen, codesFifteenSixteen, codesSixteenSeventeen, codesSeventeenEighteen, 
                codesEighteenNineteen, codesNineteenTwenty, codesTwentyTwentyone, codesTwentyoneTwentytwo, codesTwentytwoTwentythree, codesTwentythreeTwentyfour]
    #Place all the throughput values of machine two into a list
    compare_data = [compareSixSeven, compareSevenEight, compareEightNine, compareNineTen, compareTenEleven, compareElevenTwelve, compareTwelveThirteen, compareThirteenFourteen, compareFourteenFifteen,
                compareFifteenSixteen, compareSixteenSeventeen, compareSeventeenEighteen, compareEighteenNineteen, compareNineteenTwenty, compareTwentyTwentyone, compareTwentyoneTwentytwo, compareTwentytwoTwentythree,
                compareTwentythreeTwentyfour]

    #X-axis labels for one-hour intervals
    x_labels = ["6:00", "7:00", "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]

    #Layout for the machine throughput bar graph
    machine_throughput = {
        "data": [
            # Data for codes
            {
                'x': x_labels,
                'y': codes_data,
                'type': 'bar',
                'name': machine,
                'marker': {'color': '#E12D39'},
            },
            # Data for compare
            {
                'x': x_labels,
                'y': compare_data,
                'type': 'bar',
                'name': machine_throughput,
                'marker': {'color': '#3498DB'},
            },
        ],
        "layout": {
            "title": {"text": "Throughput Per Hour For These Two Machines", "x": 0.05, "xanchor": "left"},
            "xaxis": {"fixedrange": True, "tickmode": "array", "tickvals": x_labels},
            "yaxis": {"fixedrange": True},
        },
    }
    
    #Return only the graph that the active tab is selecting
    if tab == 'tab-1':
        return dcc.Graph(id='machine-performance-chart', figure=machine_performance_chart)
    elif tab == 'tab-2':
        return dcc.Graph(id='machine-throughput', figure=machine_throughput)
    elif tab == 'tab-3':
        return dcc.Graph(id='all-machines', figure=all_machines)
    



if __name__ == "__main__":
    app.run_server(debug=False)
