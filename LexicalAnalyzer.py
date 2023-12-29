import re

from SymbolTable import Symbol_Table

class Token:
    def __init__(self, line, col, token_name):
        self.line = line
        self.col = col
        self.token_name = '<' + token_name + '>'

    def __repr__(self):
        return self.token_name

class Lexical_Analyzer:
    def __init__(self, tokens, source_code):
        rules_list = [f'(?P<{token_name}>{regex})' for token_name, regex in tokens.items()]
        self.pattern = re.compile('|'.join(rules_list))
        self.line = 0
        self.col = 0
        # self.pattern = re.compile('|'.join(map(lambda token_name, regex: f'(?P<{token_name}>{regex})', tokens.items())))
        self.code_lines = source_code.split('\n')
        self.symbol_table = Symbol_Table()

    def tokenize(self):
        token_stream = []
        self.line = 1
        while self.line <= len(self.code_lines):
            token_line = []
            code_line = self.code_lines[self.line - 1]
            self.col = 1
            while self.col <= len(code_line):
                while now := code_line[self.col-1] == ' ':
                    self.col += 1

                if match := self.pattern.match(code_line, self.col-1):
                    token_name, token_value = match.lastgroup, match.group(match.lastgroup)
                    if token_name in ['IDENTIFIER', 'CONST_STRING', 'CONST_NUMBER']:
                        token_name = 'ID_TK, ' + self.symbol_table.add_item(token_value, token_name)
                    
                    token = Token(line=self.line, col=self.col, token_name=token_name)
                    self.col = match.end()+1
                    token_line.append(token)
                else:
                    pass
                    #TODO: raise issue
            token_stream.append(token_line)
            self.line += 1

        return token_stream