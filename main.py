import datetime

from src.data_handler import read_data, fill_missing_data
from src.data_analysis import get_top_three_countries, get_daily_total_vaccination

FILE_PATH = "./data/country_vaccination_stats.csv"

def main():
    data = read_data(FILE_PATH)
    data = fill_missing_data(data)
    print(data.head())

    top_countries = get_top_three_countries(data)
    print(top_countries)

    total_vaccination = get_daily_total_vaccination(data, "1/6/2021")
    print(total_vaccination)

if __name__ == "__main__":
    main()