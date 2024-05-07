TOKEN_WORDS = ['log', 'sin', 'cos']


class Tokenizer(list):
    def __init__(self, string:str):
        string = list(string)
        for _ in range(string.count(' ')):
            string.remove(' ')
        word = ''
        tokens = []
        for s in string:
            word += s
            if word.isdigit() or any(i.startswith(word) for i in TOKEN_WORDS):
                continue
            else:
                if len(word) > 1:
                    tokens.append(word[:-1])
                tokens.append(s)
                word = ''
        self.tokens = tokens + [word] if word else tokens
         = 2