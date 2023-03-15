import pandas as pd

def read_data(file_path):
    "Reads csv data from given file path and returns pandas.DataFrame"
    data = pd.read_csv(file_path)

    return data

def fill_missing_data(df: pd.DataFrame):
    "Gets pandas.DataFrame and fills the missing data in daily_vaccinations column per country with the minimum daily vaccination number of relevant countries"

    data = df.copy()

    countries_min = data.groupby("country").min()["daily_vaccinations"].fillna(0)

    missing_rows = data['daily_vaccinations'].isna()

    for i, val in enumerate(missing_rows):
        if(val):
            data.loc[i, 'daily_vaccinations'] = countries_min[data.loc[i, 'country']]

    return data





