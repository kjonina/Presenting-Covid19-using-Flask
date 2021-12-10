import pandas as pd
import datetime
from os import listdir
from os.path import isfile, join
import glob
import re
from datetime import datetime
import numpy as np



def create_csv():
    # gettting the CSV from the website
    url = 'https://opendata-geohive.hub.arcgis.com/datasets/d8eb52d56273413b84b0187a4e9117be_0.csv?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D.'
    df = pd.read_csv(url)

    # =============================================================================
    # Column 'Date' must be date, not datetime
    # =============================================================================
    df['Date'] = pd.to_datetime(df['Date']).dt.date

    # =============================================================================
    # Dropping irrelevant columns
    # =============================================================================
    df = df.drop(columns = ['X','Y','CovidCasesConfirmed','StatisticsProfileDate', 'FID',
                            'CommunityTransmission', 'CloseContact','TravelAbroad'])

    # =============================================================================
    # Melting
    # =============================================================================

    df = pd.melt(frame=df,id_vars=["Date"], var_name="Column", value_name="Cases")

    # =============================================================================
    # Trying to get Age Range
    # =============================================================================
    df['Age Range'] = df['Column']

    df['Age Range'] = df['Age Range'].str.replace('to','-')
    df['Age Range']= df['Age Range'].str.replace('up','+')
    df['Age Range']= df['Age Range'].replace("TotalConfirmedCovidCases", np.nan)
    df['Age Range']= df['Age Range'].replace("ConfirmedCovidCases",np.nan)
    df['Age Range']= df['Age Range'].replace("TotalCovidDeaths", np.nan)
    df['Age Range']= df['Age Range'].replace("ConfirmedCovidDeaths",np.nan)
    df['Age Range']= df['Age Range'].replace("HospitalisedCovidCases", np.nan)
    df['Age Range']= df['Age Range'].replace("RequiringICUCovidCases", np.nan)
    df['Age Range']= df['Age Range'].replace("HealthcareWorkersCovidCases", np.nan)
    df['Age Range']= df['Age Range'].replace("ClustersNotified", np.nan)
    df['Age Range']= df['Age Range'].str.replace("Aged", '')
    df['Age Range']= df['Age Range'].str.replace("Hospitalised5", '1-4')
    df['Age Range']= df['Age Range'].str.replace("1-4-14",'5-14')
    df['Age Range']= df['Age Range'].str.replace("1-45-64",'55-64')
    df['Age Range']= df['Age Range'].str.replace("Hospitalised", '')
    df['Age Range']= df['Age Range'].replace("Median_Age", np.nan)
    df['Age Range']= df['Age Range'].replace("Male", np.nan)
    df['Age Range']= df['Age Range'].replace("Female", np.nan)
    df['Age Range']= df['Age Range'].replace("Female", np.nan)
    df['Age Range']= df['Age Range'].replace("Unknown",np.nan)

    # =============================================================================
    # Rearranging columns
    # =============================================================================
    df = df [[
        "Date",
        "Column",
        "Age Range",
        "Cases"]]

    # =============================================================================
    # Rearranging columns
    # =============================================================================
    # assigning integer
    # df["Cases"] = df["Cases"].astype(int)

    # reseting the dataframe index
    df = df.reset_index(drop = True)

    # =============================================================================
    # Getting all contents of 'Column' to have a space between them
    # =============================================================================
    column_list = []
    for i in  df["Column"]:
        match = re.findall('([A-Z][a-z]+)', i)
        if len(match) == 4:
            new_line = match[0] + ' ' + match[1] + ' ' + match[2] + ' ' + match[3]
        elif len(match) == 3:
            new_line = match[0] + ' ' + match[1] + ' ' + match[2]
        elif len(match) == 2:
            new_line = match[0] + ' ' + match[1]
        else:
            new_line = match[0]

        column_list.append(new_line)


    column_list = pd.Series(column_list)
    column_list = column_list.reset_index()

    df = pd.merge(df, column_list, left_index = True, right_index = True)


    # =============================================================================
    # Renaming columns and rearranging them
    # =============================================================================
    df = df.rename(columns={'Column': "old_column", 0 : "Column"})

    df = df[[
        "Date",
        "old_column",
        "Column",
        "Age Range",
        "Cases"
    ]]



    # =============================================================================
    # Assigning age_list
    # =============================================================================
    age_list = df['Age Range'].unique()

    # removing NaN from the dataset
    age_list = age_list[1:]


    new_df = df.copy()

    # =============================================================================
    #
    # =============================================================================
    column_list = df['Column'].unique()

    # Columns that have accumulated cases and no daily cases count
    accumulated = ['Male','Hospitalised Covid Cases', 'Hospitalised Aged',
                   'Healthcare Workers Covid Cases', 'Aged', 'Unknown', 'Female',
                   'Median Age', 'Requiring Covid Cases', 'Clusters Notified']



    # =============================================================================
    # creating datasets for "Hospitalised Aged" and "Aged"
    # =============================================================================

    hospitalised_df = df[df['Column'].str.contains("Hospitalised Aged")]
    aged_df = df[df['Column'].str.startswith("Aged")]


    # =============================================================================
    #
    # =============================================================================
    df_list = []


    for i in column_list:
        if "Hospitalised Aged" == i:
            for age in age_list:
                h_df = hospitalised_df[hospitalised_df['Age Range'].str.contains(age)]
                h_df = pd.DataFrame(h_df)
                h_df['Daily Cases'] = h_df['Cases'].diff(1)
                h_df['Diff'] = h_df['Daily Cases'].diff(1)
    #             h_df = h_df.dropna()
    #             h_df["Daily Cases"] = h_df["Daily Cases"].astype(int)
    #             h_df["Diff"] = h_df["Diff"].astype(int)
                df_list.append(h_df)

        elif "Aged" == i:
            for age in age_list:
                a_df = aged_df[aged_df['Age Range'].str.contains(age)]
                a_df = pd.DataFrame(a_df)
                a_df['Daily Cases'] = a_df['Cases'].diff(1)
                a_df['Diff'] = a_df['Daily Cases'].diff(1)
    #             a_df = a_df.dropna()
    #             a_df["Daily Cases"] = a_df["Daily Cases"].astype(int)
    #             a_df["Diff"] = a_df["Diff"].astype(int)
                df_list.append(a_df)

        elif  i in accumulated:
            n_df = df[df['Column'].str.contains(i)]
            n_df = pd.DataFrame(n_df)
            n_df['Daily Cases'] = n_df['Cases'].diff(1)
            n_df['Diff'] = n_df['Daily Cases'].diff(1)
    #         n_df = n_df.dropna()
    #         n_df["Daily Cases"] = n_df["Daily Cases"].astype(int)
    #         n_df["Diff"] = n_df["Diff"].astype(int)
            df_list.append(n_df)
        else:
            n_df = df[df['Column'].str.contains(i)]
            n_df = pd.DataFrame(n_df)
            n_df['Daily Cases'] = np.nan
            n_df['Diff'] = n_df['Cases'].diff(1)
    #         n_df = n_df.dropna()
    #         n_df["Daily Cases"] = n_df["Daily Cases"].astype(int)
    #         n_df["Diff"] = n_df["Diff"].astype(int)
            df_list.append(n_df)
    df =  pd.concat(df_list)

    # sorting data by date
    df = df.sort_values(ascending = True, by = ["Date"])

    # reseting the dataframe index
    df = df.reset_index(drop=True)


    # dropping old_column
    df = df.drop(columns = ['old_column'])
    return df
    # =============================================================================
    # Saving new dataframe to csv
    # =============================================================================

    # df.to_csv(r"tidy_data_df.csv", index =  False)
