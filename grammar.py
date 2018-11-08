from utils import *
import numpy as np
import re
from globals import *
import os
import dialogflow_v2

class Grammar:
    def __init__(self, custom_words):
        self.grammar_dict = {}
        self.read_grammar(os.getcwd() + "/static/nlp/grammar.txt", custom_words)
    
    # Function for reading grammar file
    def read_grammar(self, grammar_file, custom_words):
        # Loop over all lines in file
        with open(grammar_file, "r") as f:
            grammar_string = f.read()
            grammar_string = grammar_string.format(*custom_words)
            for line in grammar_string.split('\n'):
                if len(line) == 0:
                    continue
                line = line.split()
                prob = float(line[0])
                line = line[1:]
                # Create dictionary for rewrite rules
                if line[0] not in self.grammar_dict.keys():
                    self.grammar_dict[line[0]] = []
                self.grammar_dict[line[0]].append((prob, line[1:]))

    # Generate a random sentence
    def gen_sent(self, start):
        sentence = ""
        probs = [self.grammar_dict[start][i][0] for i in range(len(self.grammar_dict[start]))]
        rand = np.random.choice(list(range(0, len(self.grammar_dict[start]))), p=probs)
        # Loop over symbol in grammar rule
        for symbol in self.grammar_dict[start][rand][1]:
            # If the symbol is not in the dictionary, append it to the sentence
            if symbol not in self.grammar_dict.keys():
                sentence += symbol + " "
            # Otherwise, recurse
            else:
                sentence += self.gen_sent(symbol)
        return sentence

    def generate_response(self, user_input):
        for pattern in RESPONSE_MAP:
            match = re.match(pattern, user_input.rstrip(".!"))
            if match:
                response = RESPONSE_MAP[pattern]
                sent = clean_sentence(self.gen_sent(response))
                return sent
        return ""
            