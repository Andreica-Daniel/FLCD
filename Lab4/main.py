from finiteAutomata import read_from_file


class Console:

    def read_fa(self):
        self.fa = read_from_file('fa.in')

    def print_all(self):
        print(self.fa)

    def print_states(self):
        print(self.fa.states)

    def print_alphabet(self):
        print(self.fa.alphabet)

    def print_transitions(self):
        print(self.fa.transitions)

    def print_initial_state(self):
        print(self.fa.initial_state)

    def print_final_states(self):
        print(self.fa.final_states)

    def dfa(self):
        print(self.fa.is_dfa())

    def is_accepted(self):
        sequence = input('Read sequence>>')
        print(self.fa.is_accepted(sequence))


    def run(self):
        self.read_fa()
        commands = {'1': self.print_all,
                    '2': self.print_states,
                    '3': self.print_alphabet,
                    '4': self.print_transitions,
                    '5': self.print_initial_state,
                    '6': self.print_final_states,
                    '7': self.dfa,
                    '8': self.is_accepted}
        while True:
            print("\nMenu:")
            print("1.Print FA")
            print("2.Print states")
            print("3.Print alphabet")
            print("4.Print transitions")
            print("5.Print initial state")
            print("6.Print final states")
            print("7.Check DFA")
            print("8.Check if sequence is accepted")
            print("0.Exit")
            cmd = input(">>>")
            if cmd in commands.keys():
                commands[cmd]()
            elif cmd == "0":
                break
            else:
                print("Invalid command!!!")

console = Console()
console.run()