import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tic
import math

dane = pd.read_csv('dane_csv.csv', sep = ';', decimal = ',', index_col=0)
dane['Sprzedaz całkowita'] = dane['prodA'] + dane['prodB']
sprzedaz = dane.drop(['prodA', 'prodB'], axis = 1)


sprzedaz['mies_cat'] = pd.Categorical(sprzedaz.Miesiac,
                      categories=["styczen", "luty", "marzec"],
                      ordered=True)



sprzedaz.sort_values(['mies_cat', 'dzien'], inplace = True, ignore_index = True)

#sprzedaz = sprzedaz.filter(sprzedaz.Miesiac.isin(["styczen", "marzec"]))

print(dane[dane['Miesiac'] != "luty"])

max_v = math.ceil(sprzedaz["Sprzedaz całkowita"].max())
min_v = math.floor(sprzedaz["Sprzedaz całkowita"].min())
avg_v = min_v + (max_v - min_v) / 2

skala = [min_v, min_v+2, avg_v, max_v-2, max_v]

#
fig = plt.figure(figsize=(17, 8))

ax = fig.add_axes([0.2, 0.2, 0.6, 0.7], aspect=2)

ax.set_title("Sprzedaż całkowita w styczniu i marcu", fontsize=14, verticalalignment='bottom')
ax.set_ylabel("Miesiąc.", fontsize=7)

ax.set_yticks(skala)
ax.set_xticks([0, 30, 31, 58, 59, 89], [1, 31, 1, 28, 1, 31])

#ax.grid(axis="y",linestyle="--", alpha=0.5)

ax.axhline(skala[1], linestyle="--", alpha=0.5, color="gray")
ax.axhline(skala[2], linestyle="--", alpha=0.5, color="gray")
ax.axhline(skala[3], linestyle="--", alpha=0.5, color="gray")

ax.get_yaxis().set_major_formatter(
    tic.FuncFormatter(lambda x, p: format(int(x), ',')+"k"))

lines = ax.plot(sprzedaz["Sprzedaz całkowita"])



plt.show()



