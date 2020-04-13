import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def c(n, k):
    res = np.math.factorial(k) * np.math.factorial(n-k)
    res = np.math.factorial(n) / res
    return res


def b(k, n, t):
    c_n_k = c(n, k)
    res = []

    for i in t:
        i /= len(t)
        val = c_n_k * (i**k) * ((1-i) ** (n-k))
        res.append(val)

    return res


"""
B(t) - Bezier curve explicit definition
About: https://en.wikipedia.org/wiki/B%C3%A9zier_curve
"""


def B(p, t, n):
    interpol = []
    arr = []

    for k in range(n):
        res = b(k, n, t)
        res = [p[k]*x for x in res[::]]
        arr.append(res)

    times = range(len(arr[0]))
    index = range(len(arr))
    val = 0

    for t in times:
        for i in index:
            val += arr[i][t]
        interpol.append(val)
        val = 0

    return interpol


def draw(date, new_cases, new_death, title):
    fig = plt.figure()
    ax_1 = fig.add_subplot(211)
    ax_2 = fig.add_subplot(212)

    new_cases = B(list(new_cases), range(len(list(date))), len(new_cases))
    new_death = B(list(new_death), range(len(list(date))), len(new_death))

    ax_1.set_title(title)
    ax_1.plot(date, new_cases, c='g')
    ax_1.grid(True)
    ax_1.set_xlabel("New cases per day")
    ax_1.set_ylabel("Days")
    get_quarantine = str(input("Quarantine: "))

    ax_1.tick_params(axis='x', labelsize=4)
    ax_2.tick_params(axis='x', labelsize=4)

    ax_2.plot(date, new_death, c='r')
    ax_2.grid(True)
    ax_2.set_xlabel("New deaths per day")
    ax_2.set_ylabel("Days")

    if get_quarantine != "0":
        ax_1.axvline(get_quarantine, c='b')
        ax_2.axvline(get_quarantine, c='b')

    plt.show()


string = 'https://covid.ourworldindata.org/data/ecdc/full_data.csv'
df = pd.read_csv(string)
country = str(input("Input county name: "))
loc = str("location == \"" + country + "\"")
sort_data = df.query(loc)
columns = ['date', 'new_cases', 'new_deaths']
sort_data = sort_data[columns]
draw(sort_data['date'], sort_data['new_cases'], sort_data['new_deaths'], country)
