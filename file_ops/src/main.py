"""Demonstrate Python file Input/Output (I/O)
"""

memory = [0]*100

def dump_memory():
    counter = 0
    for instruction in memory:
        counter += 1
        if (counter % 11) == 0:
            print()
            counter = 0
        else:
            print(f'{instruction:4} ', end='')
            

def load_program_from_file():
    program_file = input("Program Name: ")
    try:
        # Open named file
        with open(program_file, mode="r") as f:
            # read each line
            # and store in memory
            count = 0
            for instruction_string in f.readlines():
                memory[count] = int(instruction_string)
                count += 1
    except Exception as e:
        print(f'Problem loading program into memory. {e}')
        
            
        


def main():
    load_program_from_file()
    dump_memory()
    


if __name__ == '__main__':
    main()