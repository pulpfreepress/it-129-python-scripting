"""Demonstrates operations on dictionaries.
"""

def main():
    students = {}
    students['rick'] = 'Rick Miller'
    students['steve'] = 'Steve Jobs'
    classes = {}
    classes['it-129'] = ['Sammy', 'Dylan', 'Jose']
    classes['it-566'] = ['Kayla', 'Nigina', 'Chaleeya']


    student_1 = students['rick']

    print(students['rick'])
    print(student_1)
    print(students['steve'])
    print(classes['it-129'])
    print(students)
    print(classes)

    
    

if __name__ == '__main__':
    main()