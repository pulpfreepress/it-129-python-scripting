"""Demonstrates operations on strings
 and lists
"""

def main():
    s1 = 'Hello' 
    s2 = 'World!'
    l1 = ['H', 'e', 'l', 'l', 'o']
    l2 = ['W', 'o', 'r', 'l', 'd', '!']

    print(s1)
    print(l1)

    s3 = s1 + ' ' + s2
    print(s3)

    l3 = l1 + [' '] + l2
    print(l3)
    l3.append('!')
    print(l3)
    l3.sort()
    print(l3)
   

if __name__ == "__main__":
    main()