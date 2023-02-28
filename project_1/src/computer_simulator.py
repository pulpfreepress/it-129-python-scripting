"""
Implements the computer simulator.
"""

class ComputerSimulator():

    def __init__(self):
        """Initializes computer simulator.
        """
        self.keep_going = True
        # Menu Item Constants
        self.LOAD_PROGRAM_FROM_FILE = '1'
        self.ENTER_PROGRAM_FROM_KEYBOARD = '2'
        self.LOAD_DEMO_PROGRAM = '3'
        self.RUN_PROGRAM = '4'
        self.QUIT = '5'

        # memory
        self.memory = [0] * 100

        # accumulator
        self.accumulator = 0

        # program counter
        self.program_counter = 0

        # opcodes

        self.READ = 10
        self.WRITE = 11
        self.LOAD = 20
        self.STORE = 21
        self.ADD = 30
        self.SUB = 31
        self.MUL = 32
        self.DIV = 33
        self.BRANCH = 40
        self.BRANCHNEG = 41
        self.BRANCHZERO = 42
        self.HALT = 43
       

    def display_menu(self):
        print('\n\n')
        print('\t\t Computer Simulator Menu')
        print('\n')
        print('\t1. Load program from file.')
        print('\t2. Enter program from keyboard')
        print('\t3. Load demo program')
        print('\t4. Run program')
        print('\t5. Quit')
        print()

    def process_menu_choice(self):
        """
        Processes and executes menu commands.
        """
        # Get menu selection from user
        user_input = input('Enter menu choice: ')
        print(f'You entered: {user_input}')

        # If input is valid menu choice
        # execute menu item
        # else display error message
        # and repeat menu 

        match user_input[0]:
            case self.LOAD_PROGRAM_FROM_FILE: self.load_program_from_file()
            case self.ENTER_PROGRAM_FROM_KEYBOARD: self.enter_program_from_keyboard()
            case self.LOAD_DEMO_PROGRAM: self.load_demo_program()
            case self.RUN_PROGRAM: self.run_program()
            case self.QUIT: self.keep_going = False
            case _: print(f'Invalid menu choice...{user_input[0]}')


    def load_program_from_file(self):
        print('load_program_from_file() method called...')

    def enter_program_from_keyboard(self):
         print('enter_program_from_keyboard() method called...')

    def load_demo_program(self):
         print('Loading demo program')
         self.memory[0] = 1007
         self.memory[1] = 1008
         self.memory[2] = 2007
         self.memory[3] = 3208
         self.memory[4] = 2109
         self.memory[5] = 1109
         self.memory[6] = 4010
         self.memory[10] = 4300



    def run_program(self):
         print('running program...')

         run = True
         while run:
            # decode instruction
            instruction = self.memory[self.program_counter]
            opcode = instruction / 100
            operand = instruction % 100
            self.program_counter += 1

            # Execute instruction
            match opcode:
                case self.READ: self.read()
                case self.WRITE: self.write()
                case self.LOAD: self.load()
                case self.STORE: self.store()
                case self.ADD: self.add()
                case self.SUB: self.sub()
                case self.MUL: self.mul()
                case self.DIV: self.div()
                case self.BRANCH: self.branch()
                case self.BRANCHNEG: self.branch_neg()
                case self.BRANCHZERO: self.branch_zero()


    def read(self, operand):
        user_input = input('Enter numeric value: ')
        self.memory[operand] = float(user_input)

    def write(self):




    def dump_memory(self):
        print(self.memory)

    def launch_application(self):
        while self.keep_going:
            self.display_menu()
            self.process_menu_choice()