
def say_hello():
    s1 = "Hello World!"
    print(s1.upper())
    print("My name is Rick!".lower())

def say_goodbye():
    print("Good bye!")

def say_my_name():
    print("Module name is: " + __name__)


def main():
    input_string = input("Please enter a string: ")
    print(input_string.upper())
    say_hello()
    say_my_name()
    say_goodbye()

if __name__ == "__main__":
    main()