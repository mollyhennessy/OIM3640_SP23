import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

symbol = "GOOG"
start = "2022-03-20"
end = "2023-03-20"

data = yf.download(symbol, start, end)
columns = {'O': 'Open', 'H': 'High'}
for key in columns:
    print(f"{key} - {columns[key]}")
choice = input("Choose column: ").upper()

print(data[columns[choice]].describe())

plt.plot(data['Close'])
plt.show()