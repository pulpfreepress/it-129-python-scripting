""" Serves as main entry point for the 
    computer simulator.
"""
from computer_simulator import ComputerSimulator

def main():
    simulator = ComputerSimulator()
    #simulator.launch_application()
    simulator.dump_memory()
    simulator.load_demo_program()
    simulator.dump_memory()


if __name__ == "__main__":
    main()