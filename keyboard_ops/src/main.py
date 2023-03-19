"""Demonstrate Python console operations
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
            

def enter_program_from_keyboard():
    count = 0
    while True:
        try:
            instruction = input(" Instruction or 'no' to quit: ")
            if instruction.lower() == 'no':
                return
            else:
                memory[count] = int(instruction)
                count += 1

        except Exception as e:
            print(f'Problem entering instructions from console...{e}')
    
        
            
        


def main():
    enter_program_from_keyboard()
    dump_memory()
    


if __name__ == '__main__':
    main()