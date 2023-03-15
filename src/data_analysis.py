import pandas as pd


def get_top_three_countries(df: pd.DataFrame):
    "Gets pd.DataFrame and return the top-3 countries with highest median daily vaccination numbers"
    data = df.copy()

    countries_sorted = data.groupby('country')['daily_vaccinations'].median().sort_values(ascending=False)

    return countries_sorted[0: 3].index.values


def get_daily_total_vaccination(data: pd.DataFrame, date):
    "Gets pd.DataFrame and date in String format and returns the total vaccinations done in given date"
    return data.groupby('date')['daily_vaccinations'].sum()[date]