import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt


def draw(date, new_cases, new_death, title):
    plt.grid()
    plt.title(title)
    plt.scatter(x=date, y=new_cases, marker='o', c='b', edgecolor='b')
    plt.scatter(x=date, y=new_death, marker='o', c='b', edgecolor='b')
    plt.plot(date, new_cases, c = 'g')
    plt.plot(date, new_death, c='r')
    plt.legend(("cases_per_day", "deaths_per_day"))
    get_carantine = str(input("Carantine: "))

    if(get_carantine != "0"):
        plt.axvline(get_carantine, c='b')

    plt.tick_params(axis='x', labelsize=5)
    plt.show()


df = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/full_data.csv')
columns = df.columns.tolist()
today_data = dt.today()
today_data = dt.date(today_data)
today_data = str(today_data)
country = str(input("Input county name: "))
loc = str("location == \"" + country + "\"")
sort_data = df.query(loc)
columns = ['date', 'new_cases', 'new_deaths']
sort_data = sort_data[columns]
draw(sort_data['date'], sort_data['new_cases'], sort_data['new_deaths'], country)

"""
dat = df['location']

for i, country in enumerate(dat):
    print(country)
"""
