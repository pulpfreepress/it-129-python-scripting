"""Demonstrate Python file Input/Output (I/O)
"""

memory = [1111]*100

def dump_memory():
    counter = 0
    for instruction in memory:
        counter += 1
        if (counter % 10) == 0:
            print()
            counter = 0
        else:
            print(str(instruction) + ' ', end='')


def load_memory_from_file(filename):
    try:
        # Open named file
        with open(filename, mode="r") as f:
            # read each line
            # and store in memory
            count = 0
            for instruction_string in f.readlines():
                memory[count] = int(instruction_string)
                count += 1
    except Exception as e:
        print(f'Problem loading program into memory. {e}')
        
            
        


def main():
    load_memory_from_file("data/program_1.txt")
    dump_memory()
    


if __name__ == '__main__':
    main()