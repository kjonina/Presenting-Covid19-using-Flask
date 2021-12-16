import pandas as pd
import datetime
from datetime import datetime
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go



# ============================================================================ Plotly Graph 1
# =============================================================================


def graph1(confirmed_cc_df, hospital_cc_df,icu_cc_df):

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
# Plotly Graph 2
# =============================================================================


def graph2(aged_df):

    aged_df = aged_df.drop(columns = ['Column', 'Accumulated Cases'])

    aged_table = pd.pivot_table(aged_df, index=['Date'], values = 'Daily Cases',
                        columns=['Age Range'])


    # # plotly
    fig = go.Figure()

    # set up ONE trace
    fig.add_trace(go.Scatter(x=aged_table.index,
                             y=aged_table[aged_table.columns[0]],
                             visible=True, line = dict(color = "#636EFA"),
                            mode ='lines',
                            hovertemplate="<b>Confirmed COVID-19 Cases</b><br><br>" +
                                                "Date: %{x|%d %b %Y} <br>" +
                                                "Daily Covid-19 Cases: %{y:,.}<br>"+
                                                "<extra></extra>"))

    updatemenu = []
    buttons = []

    # button with one option for each dataframe
    for col in aged_table.columns:
        buttons.append(dict(method='restyle',
                            label=col,
                            visible=True,
                            args=[{'y':[aged_table[col]],
                                   'x':[aged_table.index],
                                   'type':'scatter'}, [0]],
                            )
                      )

    # some adjustments to the updatemenus
    updatemenu = []
    your_menu = dict()
    updatemenu.append(your_menu)

    updatemenu[0]['buttons'] = buttons
    updatemenu[0]['direction'] = 'down'
    updatemenu[0]['showactive'] = True



    # add dropdown menus to the figure
    fig.update_layout(showlegend=False, updatemenus=updatemenu,
            title = 'Daily COVID-19 Cases in Ireland', title_font_size=24,
            yaxis_title = 'Daily COVID-19 Cases',yaxis_title_font_size=16,)


    graph2 = fig.to_html(full_html=False, default_height=600, default_width=1000)

    return graph2


# =============================================================================
# Plotly Graph 2 EXTRA
# =============================================================================


def graph2_extra(hospitalised_df):


    hospitalised_df = hospitalised_df.drop(columns = ['Column', 'Accumulated Cases'])

    hospitalised_table = pd.pivot_table(hospitalised_df, index=['Date'],  values = 'Daily Cases',
                        columns=['Age Range'])


    # # plotly
    fig = go.Figure()

    # set up ONE trace
    fig.add_trace(go.Scatter(x=hospitalised_table.index,
                             y=hospitalised_table[hospitalised_table.columns[0]],
                             visible=True, line = dict(color = "#EF553B"),
                            mode ='lines',
                            hovertemplate="<b>Hospitalised COVID-19 Cases</b><br><br>" +
                                                "Date: %{x|%d %b %Y} <br>" +
                                                "Daily Covid-19 Cases: %{y:,.}<br>"+
                                                "<extra></extra>"))

    updatemenu = []
    buttons = []

    # button with one option for each dataframe
    for col in hospitalised_table.columns:
        buttons.append(dict(method='restyle',
                            label=col,
                            visible=True,
                            args=[{'y':[hospitalised_table[col]],
                                   'x':[hospitalised_table.index],
                                   'type':'scatter'}, [0]],
                            )
                      )

    # some adjustments to the updatemenus
    updatemenu = []
    your_menu = dict()
    updatemenu.append(your_menu)

    updatemenu[0]['buttons'] = buttons
    updatemenu[0]['direction'] = 'down'
    updatemenu[0]['showactive'] = True



    # add dropdown menus to the figure
    fig.update_layout(showlegend=False, updatemenus=updatemenu,
            title = 'Hospitalised COVID-19 Cases in Ireland', title_font_size=24,
            yaxis_title = 'Hospitalised COVID-19 Cases',yaxis_title_font_size=16)


    graph2_extra = fig.to_html(full_html=False, default_height=600, default_width=1000)

    return graph2_extra


# =============================================================================
# Plotly Graph 3
# =============================================================================

def graph3(aged_df):

    max_aged_df = aged_df['Daily Cases'].max() +100

    fig = px.bar(aged_df,
             x="Age Range",
             y="Daily Cases",
             color_discrete_sequence=["#636EFA"],
             animation_frame="Date",
             animation_group="Age Range",
             range_y=[0,max_aged_df],
            labels = {"x": "Date", "y": "Daily Cases"},
            title = "COVID-19 Cases by Age Range",
    #              barmode='group',
            category_orders={"Age Range": ['1-4','5-14','15-24', '25-34', '35-44',
                                           '45-54', '55-64','65-74', '75-84','85+']})

    graph3 = fig.to_html(full_html=False, default_height=600, default_width=1000)

    return graph3



# =============================================================================
# Plotly Graph 3 EXTRA
# =============================================================================

def graph3_extra(hospitalised_df):
    max_hospitalised_df = hospitalised_df['Daily Cases'].max() + 10
    fig = px.bar(hospitalised_df,
                 x="Age Range",
                 y="Daily Cases",
                 color_discrete_sequence=["#EF553B"],
                 animation_frame="Date",
                 animation_group="Age Range",
                 range_y=[0,max_hospitalised_df],
                labels = {"x": "Date", "y": "Hospitalised Cases"},
                title = "Hospitalised COVID-19 Cases by Age Range",
                category_orders={"Age Range": ['1-4','5-14','15-24', '25-34', '35-44',
                                               '45-54', '55-64','65-74', '75-84','85+']})

    graph3_extra = fig.to_html(full_html=False, default_height=600, default_width=1000)

    return graph3_extra


# =============================================================================
# Plotly Graph 4
# =============================================================================

def graph4(confirmed_cc_df, median_age_df):
    # ZOOMING IN
    # https://community.plotly.com/t/y-axis-autoscaling-with-x-range-sliders/10245/4
    fig = make_subplots(specs=[[{"secondary_y": True}]])


    fig.add_trace(go.Bar(x = confirmed_cc_df['Date'],
                    y = confirmed_cc_df['Daily Cases'],
                    hovertemplate="<b>Confirmed Covid Cases</b><br><br>" +
                                        "Date: %{x|%d %b %Y} <br>" +
                                        "Daily Covid Cases: %{y:,.}<br>"+
                                        "<extra></extra>"), secondary_y = False)

    fig.add_trace(go.Scatter(x = median_age_df['Date'],
                                 y = median_age_df['Median Age'],
                                hovertemplate="<b>Median Age</b><br><br>" +
                                        "Date: %{x|%d %b %Y} <br>" +
                                        "Median Age: %{y:,.}<br>"+
                                        "<extra></extra>",
                                 line = dict(color="#FF9900")), secondary_y = True)


    fig.update_xaxes(
        rangeslider_visible = True,
        rangeselector = dict(
            buttons = list([
                            dict(count = 7, step = "day", stepmode = "backward", label = "1W"),
                            dict(count = 1, step = "month", stepmode = "backward", label = "1M"),
                            dict(count = 3, step = "month", stepmode = "backward", label = "3M"),
                            dict(count = 6, step = "month", stepmode = "backward", label = "6M"),
                            dict(count = 1, step = "year", stepmode = "backward", label = "1Y"),
                            dict(count = 1, step = "year", stepmode = "todate", label = "YTD"),
                            dict(count = 1, step = "all", stepmode = "backward", label = "MAX")])))
    fig.update_layout(xaxis_rangeslider_visible = False)

    # Set y-axes titles
    fig.update_yaxes(title_text="Covid-19 Cases", secondary_y=False, title_font_size = 20)
    fig.update_yaxes(title_text="Median Age", secondary_y=True, title_font_size = 20)

    fig.update_layout(showlegend=False)
    # Add title
    fig.update_layout(
            title = 'Confirmed Covid Cases and Median Age', title_font_size=30)

    fig['layout']['yaxis2']['showgrid'] = False

    graph4 = fig.to_html(full_html=False, default_height=1000, default_width=1500)

    return graph4


# =============================================================================
# Plotly Graph 5
# =============================================================================

def graph5(aged_df, hospitalised_df):
    total_aged_table = aged_df.groupby(['Age Range'])['Daily Cases'].sum().reset_index()
    total_hospitalised_table = hospitalised_df.groupby(['Age Range'])['Daily Cases'].sum().reset_index()


    fig = make_subplots(rows = 1, cols = 2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig.add_trace(go.Pie(labels=total_aged_table['Age Range'],
                                 values=total_aged_table['Daily Cases'],
                                  hovertemplate="<b>Age Range: %{label}</b><br><br>" +
                                        "Total % of COVID-19: %{percent} <br>"+
                                        "Total # of COVID-19: %{value} <br>"),1, 1)
    fig.add_trace(go.Pie(labels = total_hospitalised_table['Age Range'],
                                 values = total_hospitalised_table['Daily Cases'],
                                 hovertemplate="<b>Age Range: %{label}</b><br><br>" +
                                        "Total % of Hospitalised COVID-19 Cases: %{percent} <br>" +
                                        "Total # of Hospitalised COVID-19 Cases: %{value} <br>"), 1, 2)

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.4)

    fig.update_layout(
        title_text="Total COVID-19 Cases by Age Range",
        title_font_size = 30,
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='Total <br> Confirmed <br> COVID-19 <br> Cases', x=0.175, y=0.525, font_size=22, showarrow=False),
                     dict(text='Total <br> Hospitalised <br> COVID-19 <br> Cases', x=0.835, y=0.525, font_size=22, showarrow=False)],
        legend_title_text='Age Range')
    graph5 = fig.to_html(full_html=False, default_height=1000, default_width=1500)

    return graph5
