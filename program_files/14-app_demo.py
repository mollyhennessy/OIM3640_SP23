import pandas_datareader as pdr
import sys
import time

def display_menu():
    print("""
StockTracker Menu
1. Track watchlist    
2. Add watchlist
3. Edit watchlist
4. Delete watchlist
5. Exit     
    """)

def track():
    pass
    # symbol = "GOOG"
    # print(f'{symbol:8}{pdr.get_quote_yahoo("GOOG")["price"].values[0]}')


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
        if choice in "1234":
            options[choice]()
        elif choice == '5':
            print("Goodbye!")
            time.sleep(1)
            sys.exit()
        else:
            print("Enter a valid selection")


if __name__ == "__main__":
    main()

