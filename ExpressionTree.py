from classes import *
from utilits import *

class ExpressionTree:
    def generate_from_tokens(tokens:list): 
        current_tree = None
        if type(tokens) is Tokenizer:
            tokens = tokens.tokens
        bracket_level = 0
        priorities:list[function] = [
            lambda x: x.isdigit(),
            lambda x: x in '*',
            lambda x: x in '+'
        ]
        i = 0
        word = []
        while i < len(tokens):
            if tokens[i] == '(':
                ... # put all shit in ( ) in word
                current_tree = ExpressionTree.generate_from_tokens(word) # this shit must be left
            priority = [i for i in range(len(priorities)) if priorities[i](tokens[i])][0]
            ... # put everything higher priority in word