# wrtie a function that takes stock symbols

def stock_symbols():
    stocks = []
    while True:
        stock = input("Enter stock symbol: ").upper()
        if stock != '' and stock not in stocks:
            stocks.append(stock)
        else:
            break
    return sorted(stocks)

# watchlist = stock_symbols()
# print(watchlist)

# function to eliminate punctuation

def clean(text):
    punctuation = ',.!?;"'
    for mark in punctuation:
        text = text.replace(mark, '')
    text = text.split()
    return text


# lyrics = open("../files/desolation_row.txt", "r").read()
# processed = clean(lyrics)
# print(" ".join(processed))

def replace_vowels(string):
    vowels = {'a': 4, 'e': 3, 'i': 1, 'o': 0, 'u': 8}
    for vowel,num in vowels.items():
        string = string.replace(vowel, str(num))
    return string

def moiras_vowels(string):
    vowels = {'a': 4, 'e': 3, 'i': 1, 'o': 0, 'u': 8}
    revised = ''
    for letter in string:
        if letter in 'aeiou':
            letter = str(vowels[letter])
        revised += letter
    return revised

# print(moiras_vowels("Yay! Spring is coming"))

def is_anagram():
    string = input("Enter first string: ").lower()
    string2 = input("Enter second string: ").lower()
    string = sorted(string.replace(" ", ""))
    string2 = sorted(string2.replace(" ", ""))
    if string == string2:
        return True
    else:
        return False

print(is_anagram())







