class DFA:
    def __init__(self):
        # State transition table
        self.transition_table = {
            0: {'0': 0, '1': 1},
            1: {'0': 2, '1': 1},
            2: {'0': 0, '1': 3},
            3: {'0': 3, '1': 3}  # Loop in accepting state
        }
        # Start state
        self.start_state = 0
        # Set of accepting states
        self.accept_states = {3}
        # Current state
        self.current_state = self.start_state

    def reset(self):
        # Reset to the start state
        self.current_state = self.start_state

    def process_input(self, input_string):
        # Process the input string symbol by symbol
        for symbol in input_string:
            if symbol in self.transition_table[self.current_state]:
                self.current_state = self.transition_table[self.current_state][symbol]
            else:
                # Invalid symbol, reject the string
                return False
        # Return True if the current state is an accepting state, False otherwise
        return self.current_state in self.accept_states

# Contoh penggunaan
if __name__ == "__main__":
    dfa = DFA()
    
    # Contoh input string biner
    test_strings = ["", "0", "1", "101", "1001", "1010", "110101", "10111"]
    
    for string in test_strings:
        dfa.reset()  # Reset DFA to start state
        result = dfa.process_input(string)
        print(f"String: {string}, Diterima: {result}")