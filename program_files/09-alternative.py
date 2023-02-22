from collections import Counter
import yfinance

text = open("../files/desolation_row.txt", 'r').read()

text = text.lower().split()
counted = Counter(text)
print(counted)
print(len(counted))

