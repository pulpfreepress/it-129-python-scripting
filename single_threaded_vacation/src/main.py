"""Single-Threaded Vacation

   Demonstrates how a single-threaded application behaves.
"""

_thirsty = True
_hungry = True


def fetch_drink():
    steps_to_the_bar = range(5000)
    for i in steps_to_the_bar:
        if (i % 99) == 0:
            print()
            print(" Fetching Drinks  ", end="")
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
        else:
            print(".", end="")
    global _hungry
    _hungry = False
    print()




def main():
    global _hungry
    global _thirsty
    
    while _hungry or _thirsty:
        print("***** Relaxing *****\a")
        fetch_drink()
        print("***** Relaxing *****\a")
        fetch_food()
        print("***** Relaxing *****\a")

if __name__ == "__main__":
    main()