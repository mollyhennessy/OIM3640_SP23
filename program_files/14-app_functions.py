import os
"""
Note these functions assume there is a directory called 
'watchlists' in the parent directory of your current working directory
Run read_directory by itself first to make sure the directory exists.
You will also need at least one file with the extension .watchlist 
in order to print(read_list()) as intended  
"""

def read_directory():
    if not os.path.exists("../watchlists/"):
        print("No saved watchlists")
        os.mkdir("../watchlists")
    else:
        files = sorted(os.listdir("../watchlists"))
        if not files:
            print("No available watchlists")
        else:
            print("Available watchlists:")
            print("-" * 21)
            for number, name in enumerate(files, 1):
                if name.endswith('watchlist'):
                    name = name.replace('.watchlist', '')
                    print(f"{number} - {name}")
            return files

def read_list():
    watchlists = read_directory()
    if watchlists:
        choice = int(input("Enter a watchlist number: "))
        chosen_file = watchlists[choice - 1]
        return open(f"../watchlists/{chosen_file}", "r").read().split()
    else:
        return "Select add a list fron the menu..."

#read_directory()
print(read_list())