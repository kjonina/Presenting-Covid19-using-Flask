
import pandas as pd



from tidy_data import create_csv


def create_new_dfs(df):

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

    # =============================================================================
    # Dataset for Confirmed Covid Cases with Age Range
    # =============================================================================
    aged_and_hospitalised_df = df[df['Column'].str.contains("Aged")]

    # column cases actually represents accumulated cases
    aged_and_hospitalised_df = aged_and_hospitalised_df.rename(columns={'Cases': 'Accumulated Cases'})

    # =============================================================================
    # Dataset for Confirmed Covid Cases (NO Age Range)
    # =============================================================================
    confirmed_cc_df = df[df['Column'].str.startswith("Confirmed Covid Cases")]

    # in this dataset, the age range is empty
    confirmed_cc_df = confirmed_cc_df.drop(columns = ['Age Range','Age Range', 'Daily Cases'])

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
    icu_cc_df = icu_cc_df.drop(columns = ['Age Range','Age Range'])

    # column cases actually represents accumulated cases
    icu_cc_df = icu_cc_df.rename(columns={'Cases': 'Accumulated Cases'})

    # =============================================================================
    # Dataset for Median Age
    # =============================================================================
    median_age_df = df[df['Column'].str.contains("Median Age")]

    # in this dataset, the age range is empty
    median_age_df = median_age_df.drop(columns = ['Age Range', 'Daily Cases','Diff'])

    # column cases actually represents accumulated cases
    median_age_df = median_age_df.rename(columns={'Cases': 'Median Age'})


    return aged_df, hospitalised_df, aged_and_hospitalised_df, confirmed_cc_df, hospital_cc_df, icu_cc_df,  median_age_df
