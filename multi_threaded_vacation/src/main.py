"""Multi-Threaded Vacation

   Demonstrates how a multi-threaded application behaves.
"""

import threading
import time

_thirsty = True
_hungry = True

def fetch_drink():
    steps_to_the_bar = range(5000)
    for i in steps_to_the_bar:
        if (i % 99) == 0:
            print()
            print(" Fetching Drinks  ", end="")
            time.sleep(.2)
        else:
            print(".",end="")
    global _thirsty
    _thirsty = False
    print()




def fetch_food():
    steps_to_the_grill = range(5000)
    for i in steps_to_the_grill:
        if (i % 99) == 0: 
            print()
            print(" Fetching Food ", end="")
            time.sleep(.2)
        else:
            print(".", end="")
    global _hungry
    _hungry = False
    print()




def main():
    global _hungry
    global _thirsty
    
    while _hungry or _thirsty:
        print("***** Relaxing *****")
        print('\a')
        drink_fetcher = threading.Thread(target=fetch_drink)
        drink_fetcher.start()
        print("***** Relaxing *****")
        print('\a')
        food_fetcher = threading.Thread(target=fetch_food)
        food_fetcher.start()
        print("***** Relaxing *****")
        print('\a')

if __name__ == "__main__":
    main()