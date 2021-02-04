#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import os

import plotly.io as pio

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)
def read_data(file_name='Cellular-Phone_TRANSFORMED.csv'):
    #'''this function reads the data'''

    # create the path to the data
    input_path = "C:/Users/yassi/Desktop/data"
    input_file = os.path.join(input_path, file_name)
    # read in the data.frame
    df = pd.read_csv(input_file, sep=",")
    return df

def create_figure1(dff):
    #'''this function creates a figure for the dashboard'''

    # create the figure with any df
    fig1 = px.scatter_geo(dff, locations="ISO",
                     hover_name="Country", 
                     size="bb",
                     projection="natural earth", size_max=75, 
                     color="Continent",
                     width=1600, height=600)
    fig1.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0})
    return fig1

def create_figure2(dff):
    #'''this function creates a figure for the dashboard'''

    # create the figure with any df
    fig2 = px.bar(dff, x='Country', y='bb', log_y=True,
                         width=700, height=400)
    return fig2

def create_figure3(dff):
    
    fig3 = px.line_geo(dff, locations="ISO", 
                      #color="Continent", 
                      projection="orthographic", 
                     width=600, height=600)
    fig3.update_geos(projection_rotation=dict(lon=-42, lat=69, roll=0),)
    
    fig3.update_layout(margin={"r":0,"t":0,"l":100,"b":10})
    return fig3


# def create_figure4(df):
#     df4 = df.copy()
#     df4 = df4.iloc[25:,: ]
#     y = df4.groupby('Year')['bb'].apply(lambda x: sum(x))
#     x = [1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]    
#     df4 = y.to_frame()
#     #df4 = px.data.df4()
#     fig4 = px.scatter(df4, x="Year", y="bb")
    
#     return fig4

def create_figure4(df):
    df4 = df.copy()
    df4 = df4.iloc[25:,:]
    df4.drop(df4.tail(2).index,inplace=True) 
    fig4 = px.scatter(df4, x="Year", y="bb", color="Continent", log_y=True,
                  width=1600, height=400)
    return fig4


# def slider_range_min(file_name):
#     slider_df = read_data(file_name=file_name)
    
#     return int(slider_df.loc[:,['Year']].min())


# def slider_range_max(file_name):
#     slider_df = read_data(file_name=file_name)
    
#     return int(slider_df.loc[:,['Year']].max())



# some default data for the first create_figure(df) call
df = read_data()


# Layout
app.layout = html.Div(children=[

    html.H1("The spread of the patents in the world over the years", style={'text-align': 'center'}),
    
    dcc.Dropdown(
        id='dropdown',
        options=[
           
            {'label': 'Cellular Phone', 'value': 'Cellular-Phone_TRANSFORMED.csv'},
            {'label': 'Microcomputer', 'value': 'Microcomputer_TRANSFORMED.csv'},
            {'label': 'Molecular chimeras', 'value': 'Molecular-chimeras_TRANSFORMED.csv'},
            {'label': 'Digital Voice Mail System', 'value': 'Digital-Voice-Mail-System_TRANSFORMED.csv'},
            #{'label': 'Co-transformation - invented in 1983', 'value': 'Co-transformation_TRANSFORMED.csv'},
            {'label': 'Laser ', 'value': 'Laser_TRANSFORMED.csv'},
            {'label': 'Airbag', 'value': 'Airbag_TRANSFORMED.csv'},
            {'label': 'Antibody Molecules', 'value': 'Antibody-Molecules_TRANSFORMED.csv'},
            {'label': 'Google Pagerank Algorithm', 'value': 'Google-Pagerank-Algorithm_TRANSFORMED.csv'}
           
        ],
        value='Cellular-Phone_TRANSFORMED.csv'
    ),
   html.Div(id='info_container', children=[], style={'color': 'black', 'fontSize': 16, 'fontWeight': 600}),
    html.Div([
        html.Div(
        dcc.Graph(id='my_bee_map', figure=create_figure1(df)), style={'display': 'inline-block'}), 
        html.Div(
        dcc.Graph(id='line_map', figure=create_figure3(df)), style={'display': 'inline-block'}),
    ], style={'width': '100%', 'display': 'inline-block'}),
    
     
    
    html.Div([
        html.Div(
        dcc.Graph(id='bar_chart', figure=create_figure2(df)), style={'display': 'inline-block'}), 
        html.Div(
        dcc.Graph(id='scatter_plot', figure=create_figure4(df)), style={'display': 'inline-block'}),
    ], style={'width': '100%', 'display': 'inline-block'}),
        
    dcc.Slider(
        id="slct_year",
        min=1975,
        max=2020,
        value=1975,
         marks={
        #1930: {'label': '1930'},
        #1931: {'label': 'Hair Dryer', 'style': {'color': '#f50'}},
        #1940: {'label': '1940'},
        1950: {'label': '1950'},
        #1955: {'label': 'Atomic Reactor', 'style': {'color': '#f50'}},
        1960: {'label': '1960'},
        1970: {'label': '1970'},
        #1975: {'label': 'Cellular Phone', 'style': {'color': '#f50'}},
        1980: {'label': '1980'},
        1990: {'label': '1990'},
        2000: {'label': '2000'},
        #2001: {'label': 'Antibody Molecules, Google Pagerank Algorithm', 'style': {'color': '#f50'}},
        2010: {'label': '2010'},
        2020: {'label': '2020'}
    },
        
    ),
    
   
    html.Div(id='output_container', children=[]),
    html.Br(),
    
    

])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure'),
    Output(component_id='line_map', component_property='figure'),
     Output(component_id='scatter_plot', component_property='figure'),
     Output(component_id='bar_chart', component_property='figure'),
    Output(component_id='info_container', component_property='children')],
     
    
    [Input(component_id='slct_year', component_property='value'),
     Input(component_id='dropdown', component_property='value')]
 )

def update_graph(option_slctd, file_name):
    #'''reads data and creates figure for dcc.Graph()'''
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)
    
    
    # file_name is the value from the Dropdown list
    df = read_data(file_name=file_name)
    dff = df.copy()
    dff = dff[dff["Year"] == option_slctd]    
    fig1 = create_figure1(dff) 
    fig3 = create_figure3(dff)
    fig2 = create_figure2(dff)
    fig4 = create_figure4(df)
    info_container = df.loc[0,"Info"]
    
    return container, fig1, fig3, fig2, fig4, info_container

# def slider_range_max(file_name):
#     slider_df = read_data(file_name=file_name)
    
#     return int(slider_df.loc[:,['Year']].max())

# def slider_range_min(file_name):
#     slider_df = read_data(file_name=file_name)
    
#     return int(slider_df.loc[:,['Year']].min())

# def update_graph(option_slctd):
#     print(option_slctd)
#     print(type(option_slctd))

#     container = "The year chosen by user was: {}".format(option_slctd)

#     dff = df_pace.copy()
#     dff = dff[dff["Year"] == option_slctd]
    

#     # Plotly Express
#     fig1 = px.scatter_geo(dff, locations="ISO",
#                      hover_name="Country", size="bb",
#                      projection="natural earth", color="Continent",
#                          width=1600, height=800)
#     fig2 = px.bar(dff, x='Country', y='bb',
#                          width=1600, height=200)
#     fig3 = px.line_geo(dff, locations="ISO",
#                   color="Continent", 
#                   projection="orthographic")

#     return container, fig1, fig2, fig3


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False, port=3335)

