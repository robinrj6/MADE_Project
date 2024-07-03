import sqlite3
import matplotlib.pyplot as plt
import numpy as np


def plot_graph(x, y, y1, y2, year, gas):
    ax1 = plt.subplot(221)
    ax1.margins(0.10)
    ax1.set_xlabel("Year")  # add X-axis label
    ax1.set_ylabel("Emission")  # add Y-axis label
    ax1.plot(year, y1, linestyle='-', marker='o')
    ax1.set_title('Emission vs Year')

    ax2 = plt.subplot(222)
    ax2.margins(0.10)
    ax2.set_xlabel("Year")  # add X-axis label
    ax2.set_ylabel("# Diseases")  # add Y-axis label
    ax2.plot(year, y2, linestyle='-', marker='o')
    ax2.set_title('# Diseases vs Year')

    ax3 = plt.subplot(212)
    ax3.margins(0.10)
    ax3.set_xlabel("Emission")  # add X-axis label
    ax3.set_ylabel("# Diseases")  # add Y-axis label
    ax3.plot(x, y, linestyle='-', marker='o')
    ax3.set_title(f"{gas} Relation")

    plt.show()


db = sqlite3.connect('../data/Store.sqlite')

gases = list(map(lambda x: x[0], db.execute(
    'SELECT entity from primap group by entity').fetchall()))

data = db.execute(
    "select year,count(*) from Diseases group by year").fetchall()

year_vs_disease_count = dict(data)

for gas in gases:
    year_vs_emission = {}
    y1 = []
    y2 = []
    for x in range(1996, 2020):
        data = db.execute(
            f"select avg(`{x}`) from (select * from primap where entity='{gas}')").fetchone()
        print(data)
        year_vs_emission[x] = data[0]
        y1.append(year_vs_emission[x])
    x = []
    y = []
    for year in year_vs_disease_count:
        x.append(year_vs_emission[year])
        y.append(year_vs_disease_count[year])
        y2.append(year_vs_disease_count[year])

    x = np.array(x)
    y = np.array(y)

    plot_graph(x, y, y1, y2, range(1996, 2020), gas)
