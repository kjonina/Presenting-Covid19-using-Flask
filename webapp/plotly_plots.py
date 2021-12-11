import pandas as pd
import datetime
from datetime import datetime
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# # reading in the tidy data csv
# df = pd.read_csv('tidy_data_df.csv', parse_dates = ['Date'])

from tidy_data import create_csv

#
# # =============================================================================
# # Changing data type for different columns
# # =============================================================================
# df['Column'] = df['Column'].astype('category')
# df['Age Range'] = df['Age Range'].astype('category')
#
# df['Age Range'] = df['Age Range'].cat.reorder_categories(
#     ['1-4','5-14','15-24', '25-34', '35-44', '45-54', '55-64','65-74', '75-84','85+'], ordered=True)
#
# # =============================================================================
# # Changing data type for different columns
# # =============================================================================
#
# df['Date'] = df['Date'].astype(str)
# df['Date'] = pd.to_datetime(df['Date'], errors='ignore', format='%Y-%B-%d')
#
# # =============================================================================
# # Replacing Nan with 0
# # =============================================================================
# # replacing all Nan with 0
# df['Daily Cases'] = df['Daily Cases'].fillna(0)
# df['Diff'] = df['Diff'].fillna(0)
#
# #changing the 0.0 to 0
# df['Daily Cases'] = df['Daily Cases'].astype(int)
# df['Diff'] = df['Diff'].astype(int)
#
# # =============================================================================
# # Dataset for Confirmed Covid Cases with Age Range
# # =============================================================================
# aged_df = df[df['Column'].str.startswith("Aged")]
# aged_df = aged_df.rename(columns={'Cases': 'Accumulated Cases'})
#
# # =============================================================================
# # Dataset for Hospitalised Confirmed Covid Cases with Age Range
# # =============================================================================
# hospitalised_df = df[df['Column'].str.contains("Hospitalised Aged")]
#
# # column cases actually represents accumulated cases
# hospitalised_df = hospitalised_df.rename(columns={'Cases': 'Accumulated Cases'})

# # =============================================================================
# # Dataset for Confirmed Covid Cases with Age Range
# # =============================================================================
# aged_and_hospitalised_df = df[df['Column'].str.contains("Aged")]
#
# # column cases actually represents accumulated cases
# aged_and_hospitalised_df = aged_and_hospitalised_df.rename(columns={'Cases': 'Accumulated Cases'})

# # =============================================================================
# # Dataset for Confirmed Covid Cases (NO Age Range)
# # =============================================================================
# confirmed_cc_df = df[df['Column'].str.startswith("Confirmed Covid Cases")]
#
# # in this dataset, the age range is empty
# confirmed_cc_df = confirmed_cc_df.drop(columns = ['Age Range','Age Range', 'Daily Cases'])
#
# # column cases actually represents accumulated cases
# confirmed_cc_df = confirmed_cc_df.rename(columns={'Cases': 'Daily Cases'})
#
#
# # =============================================================================
# # Dataset for Hospitalised Covid Cases (NO Age Range)
# # =============================================================================
# hospital_cc_df = df[df['Column'].str.contains("Hospitalised Covid Cases")]
#
# # in this dataset, the age range is empty
# hospital_cc_df = hospital_cc_df.drop(columns = ['Age Range'])
#
# # column cases actually represents accumulated cases
# hospital_cc_df = hospital_cc_df.rename(columns={'Cases': 'Accumulated Cases'})
#
#
# # =============================================================================
# # Dataset for Covid Cases Requiring ICU
# # =============================================================================
# icu_cc_df = df[df['Column'].str.contains("Requiring")]
#
# # in this dataset, the age range is empty
# icu_cc_df = icu_cc_df.drop(columns = ['Age Range','Age Range'])
#
# # column cases actually represents accumulated cases
# icu_cc_df = icu_cc_df.rename(columns={'Cases': 'Accumulated Cases'})

# # =============================================================================
# # Dataset for Median Age
# # =============================================================================
# median_age_df = df[df['Column'].str.contains("Median Age")]
#
# # in this dataset, the age range is empty
# median_age_df = median_age_df.drop(columns = ['Age Range', 'Daily Cases','Diff'])
#
# # column cases actually represents accumulated cases
# median_age_df = median_age_df.rename(columns={'Cases': 'Median Age'})
#

# =============================================================================
# Plotly Graph 1
# =============================================================================


def graph1(df):
    # =============================================================================
    # Changing data type for different columns
    # =============================================================================
    df['Column'] = df['Column'].astype('category')
    df['Age Range'] = df['Age Range'].astype('category')

    df['Age Range'] = df['Age Range'].cat.reorder_categories(
        ['1-4','5-14','15-24', '25-34', '35-44', '45-54', '55-64','65-74', '75-84','85+'], ordered=True)

    # =============================================================================
    # Changing data type for different columns
    # =============================================================================

    df['Date'] = df['Date'].astype(str)
    df['Date'] = pd.to_datetime(df['Date'], errors='ignore', format='%Y-%B-%d')

    # =============================================================================
    # Replacing Nan with 0
    # =============================================================================
    # replacing all Nan with 0
    df['Daily Cases'] = df['Daily Cases'].fillna(0)
    df['Diff'] = df['Diff'].fillna(0)

    #changing the 0.0 to 0
    df['Daily Cases'] = df['Daily Cases'].astype(int)
    df['Diff'] = df['Diff'].astype(int)


    # =============================================================================
    # Dataset for Confirmed Covid Cases (NO Age Range)
    # =============================================================================
    confirmed_cc_df = df[df['Column'].str.startswith("Confirmed Covid Cases")]

    # in this dataset, the age range is empty
    confirmed_cc_df = confirmed_cc_df.drop(columns = ['Age Range', 'Daily Cases'])

    # column cases actually represents accumulated cases
    confirmed_cc_df = confirmed_cc_df.rename(columns={'Cases': 'Daily Cases'})



    # =============================================================================
    # Dataset for Hospitalised Covid Cases (NO Age Range)
    # =============================================================================

    hospital_cc_df = df[df['Column'].str.contains("Hospitalised Covid Cases")]

    # in this dataset, the age range is empty
    hospital_cc_df = hospital_cc_df.drop(columns = ['Age Range'])

    # column cases actually represents accumulated cases
    hospital_cc_df = hospital_cc_df.rename(columns={'Cases': 'Accumulated Cases'})

    # =============================================================================
    # Dataset for Covid Cases Requiring ICU
    # =============================================================================
    icu_cc_df = df[df['Column'].str.contains("Requiring")]

    # in this dataset, the age range is empty
    icu_cc_df = icu_cc_df.drop(columns = ['Age Range'])

    # column cases actually represents accumulated cases
    icu_cc_df = icu_cc_df.rename(columns={'Cases': 'Accumulated Cases'})


    # =============================================================================
    # plotly
    # =============================================================================

    fig = go.Figure()

    age = go.Scatter(x = confirmed_cc_df['Date'],
                                 y = confirmed_cc_df['Daily Cases'],
                                 name = 'Daily Cases',
                                 mode = 'lines',
                                 customdata = confirmed_cc_df['Column'],
                                 hovertemplate = "<b>%{customdata}</b><br><br>" +
                                                "Date: %{x|%d %b %Y} <br>" +
                                                "Covid-19 Cases: %{y:,.}<br>"+
                                                 "<extra></extra>",
                                 line = dict(color = "#636EFA"))

    hospitalisation = go.Scatter(x = hospital_cc_df['Date'],
                                 y = hospital_cc_df['Daily Cases'],
                                 name = 'Daily Hospitalisation with Covid',
                                 mode = 'lines',
                                 customdata = hospital_cc_df['Column'],
                                 hovertemplate = "<b>%{customdata}</b><br><br>" +
                                                "Date: %{x|%d %b %Y} <br>" +
                                                "Daily Hospitalisation with Covid: %{y:,.}<br>"+
                                                 "<extra></extra>",
                                 line = dict(color = "#EF553B"))

    icu = go.Scatter(x = icu_cc_df['Date'],
                                 y = icu_cc_df['Daily Cases'],
                                 name = 'Daily ICU Numbers',
                                 mode = 'lines',
                                 customdata = icu_cc_df['Column'],
                                 hovertemplate = "<b>%{customdata}</b><br><br>" +
                                                "Date: %{x|%d %b %Y} <br>" +
                                                "Daily Hospitalisation with Covid: %{y:,.}<br>"+
                                                 "<extra></extra>",
                                 line = dict(color = "#316395"))

    data = [age, hospitalisation, icu]

    layout = dict(
        title = 'Daily COVID-19 Cases in Ireland', title_font_size=30,
        yaxis_title = 'Daily COVID-19 Cases',yaxis_title_font_size=20,
        autosize = False, width = 1400, height = 1000,
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                                dict(count = 7, step = "day", stepmode = "backward", label = "1W"),
                                dict(count = 1, step = "month", stepmode = "backward", label = "1M"),
                                dict(count = 3, step = "month", stepmode = "backward", label = "3M"),
                                dict(count = 6, step = "month", stepmode = "backward", label = "6M"),
                                dict(count = 1, step = "year", stepmode = "backward", label = "1Y"),
                                dict(count = 1, step = "year", stepmode = "todate", label = "YTD"),
                                dict(count = 1, step = "all", stepmode = "backward", label = "MAX")])
            ),
            rangeslider=dict(
                visible = True
            ),
            type='date'
        )
    )

    fig = go.FigureWidget(data=data, layout=layout)
    # fig.update_layout(showlegend=False)
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.5,
        xanchor="right",
        x=1
    ))



    graph1 = fig.to_html(full_html=False, default_height=1000, default_width=1500)

    return graph1


# =============================================================================
# Plotly Graph 1
# =============================================================================


def graph2(df):
    # =============================================================================
    # Dataset for Confirmed Covid Cases with Age Range
    # =============================================================================
    aged_df = df[df['Column'].str.startswith("Aged")]
    aged_df = aged_df.rename(columns={'Cases': 'Accumulated Cases'})

    # =============================================================================
    # Dataset for Hospitalised Confirmed Covid Cases with Age Range
    # =============================================================================
    hospitalised_df = df[df['Column'].str.contains("Hospitalised Aged")]

    # column cases actually represents accumulated cases
    hospitalised_df = hospitalised_df.rename(columns={'Cases': 'Accumulated Cases'})


    age_list = ['0-4','5-14','15-24', '25-34', '35-44', '45-54', '55-64','65-74', '75-84','85+']

    fig = make_subplots(rows = 2, cols = 1, shared_xaxes = True, subplot_titles = [
            'Daily COVID-19 Cases by Age Range',
            'Daily Hospitalisation with COVID-19 Cases by Age Range'])

    # Loop through the suburbs
    for age in age_list:
      	# Subset the DataFrame

        new_aged_df = aged_df[aged_df['Age Range'] == age]
        # Add a trace for each suburb subset
        fig.add_trace(go.Scatter(
                    x = new_aged_df['Date'],
                    y = new_aged_df['Daily Cases'],
                    name = age,
                    mode ='lines', line = dict(color = "#636EFA"),
                    customdata = new_aged_df['Age Range'],
                    hovertemplate="<b>Age Range: %{customdata}</b><br><br>" +
                                        "Date: %{x|%d %b %Y} <br>" +
                                        "Daily Covid-19 Cases: %{y:,.}<br>"+
                                        "<extra></extra>"), row = 1, col = 1)

    # Loop through the suburbs
    for age in age_list:

      	# Subset the DataFrame
        new_h_df = hospitalised_df[hospitalised_df['Age Range'] == age]
        # Add a trace for each suburb subset
        fig.add_trace(go.Scatter(
                    x = new_h_df['Date'],
                    y = new_h_df['Daily Cases'],
                    name = age,
                    mode = 'lines', line = dict(color = "#EF553B"),
                    customdata = new_h_df['Age Range'],
                    hovertemplate = "<b>Age Range: %{customdata}</b><br><br>" +
                                        "Date: %{x|%d %b %Y} <br>" +
                                        "Hospitalised Covid-19 Cases: %{y:,.}<br>"+
                                        "<extra></extra>"), row = 2, col = 1)


    # Create the buttons
    dropdown_buttons = [
    {'label': "1-4", 'method': 'restyle', 'args': [{"visible": [True, False, False, False,
                                                                False, False, False, False, False, False]},
                                                  {"title": "1-4"}]},
    {'label': "5-14", 'method': 'restyle', 'args': [{"visible": [False,True, False, False,
                                                                False, False, False, False, False, False]},
                                                   {"title": "5-15"}]},
    {'label': "15-24", 'method': 'restyle', 'args': [{"visible": [False,False, True, False,
                                                                 False, False, False, False, False, False]},
                                                    {"title": "15-14"}]},
    {'label': "25-34", 'method': 'restyle', 'args': [{"visible": [False,False, False, True,
                                                                 False, False, False, False, False, False]},
                                                    {"title": "25-34"}]},
    {'label': "35-44", 'method': 'restyle', 'args': [{"visible": [False,False, False, False,
                                                                 True, False, False, False, False, False]},
                                                    {"title": "35-44"}]},
    {'label': "45-54", 'method': 'restyle', 'args': [{"visible": [False, False, False, False,
                                                                 False, True, False, False, False, False]},
                                                    {"title": "45-54"}]},
    {'label': "55-64", 'method': 'restyle', 'args': [{"visible": [False, False, False, False,
                                                                 False, False, True, False, False, False]},
                                                    {"title": "55-64"}]},
    {'label': "65-74", 'method': 'restyle', 'args': [{"visible": [False, False, False, False,
                                                                 False, False, False, True, False, False]},
                                                    {"title": "65-74"}]},
    {'label': "75-84", 'method': 'restyle', 'args': [{"visible": [False, False, False, False,
                                                                 False, False, False, False, True, False]},
                                                    {"title": "75-84"}]},
    {'label': "85+", 'method': 'restyle', 'args': [{"visible": [False, False,False, False,
                                                               False, False, False, False, False, True]},
                                                  {"title": "85+"}]},
    ]

    fig.update_layout(
        showlegend = False,
        xaxis_rangeslider_visible = False,
        title = 'COVID-19 Cases for each Age Range', title_font_size=30,
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                                dict(count = 7, step = "day", stepmode = "backward", label = "1W"),
                                dict(count = 1, step = "month", stepmode = "backward", label = "1M"),
                                dict(count = 3, step = "month", stepmode = "backward", label = "3M"),
                                dict(count = 6, step = "month", stepmode = "backward", label = "6M"),
                                dict(count = 1, step = "year", stepmode = "backward", label = "1Y"),
                                dict(count = 1, step = "year", stepmode = "todate", label = "YTD"),
                                dict(count = 1, step = "all", stepmode = "backward", label = "MAX")]))),


        autosize = False, width = 1400, height = 1000)

    fig['layout']['yaxis1']['title']='Daily COVID-19 Cases'
    fig['layout']['yaxis2']['title']='Daily Hospitalised COVID-19 Cases'



    # Update the figure to add dropdown menu
    fig.update_layout({'updatemenus': [{'active': 0, 'buttons': dropdown_buttons}]})


    graph2 = fig.to_html(full_html=False, default_height=1000, default_width=1500)

    return graph2
