import pandas_datareader as pdr
import sys
from time import sleep, time

def display_menu():
    print("""
StockTracker Menu
1. Track watchlist    
2. Add watchlist
3. Edit watchlist
4. Delete watchlist
5. Exit     
    """)

def track(watchlist):
    start_time = time()
    prompt = ''
    while True:
        for symbol in watchlist:
            try:
                print(f'{symbol:8}{pdr.get_quote_yahoo(symbol)["price"].values[0]}')
            except:
                print(f"{symbol} not found")
        sleep(1)
        if time() - start_time >= 10:
            start_time = time()
            prompt = input("To continue press enter, any key to quit ")
            if prompt.isalpha():
                break





def add_list():
    pass


def edit_list():
    print("Edit your list")


def delete_list():
    pass






options = {"1":track, "2":add_list, "3":edit_list, "4":delete_list}
def main():
    while True:
        display_menu()
        choice = input("Enter your selection: " )
        if choice == "1":
            watchlist = "AMZN AAPL GOOG FB".split()
            options[choice](watchlist)
        elif choice in  "234":
            options[choice]()
        elif choice == '5':
            print("Goodbye!")
            time.sleep(1)
            sys.exit()
        else:
            print("Enter a valid selection")


if __name__ == "__main__":
    main()

