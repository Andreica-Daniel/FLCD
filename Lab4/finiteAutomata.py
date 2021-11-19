class FiniteAutomata:

    def __init__(self, states, alphabet, initial_state, final_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions

    def is_dfa(self):
        for k in self.transitions.keys():
            if len(self.transitions[k]) > 1:
                return False
        return True

    def is_accepted(self, sequence):
        if self.is_dfa():
            current = self.initial_state
            for symbol in sequence:
                print(current, symbol)
                if (current, symbol) in self.transitions.keys():
                    current = self.transitions[(current, symbol)][0]
                else:
                    return False
            return current in self.final_states
        return False

    def __str__(self):
        return "states = { " + ', '.join(self.states) + " }\n alphabet = { " + ', '.join(self.alphabet) + " }\n initial_state = { " + self.initial_state + " }\n final_states = { " + ', '.join(self.final_states) + " }\n transitions = { " + str(self.transitions) + " } "



def get_line(line):
    return line.strip().split(' ')[2:]

def read_from_file(fileName):
    with open(fileName) as file:
        states = get_line(file.readline())
        alphabet = get_line(file.readline())
        initial_state = get_line(file.readline())[0]
        final_states = get_line(file.readline())
        file.readline()
        transitions = {}
        for line in file:
            src = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[0]
            route = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(', ')[1]
            dst = line.strip().split('->')[1].strip()

            if (src, route) in transitions.keys():
                if dst not in transitions[(src, route)]:
                    transitions[(src, route)].append(dst)
            else:
                transitions[(src, route)] = [dst]
        return FiniteAutomata(states, alphabet, initial_state, final_states, transitions)
