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
        self.line = 0
        self.col = 0
        self.patterns = re.compile('|'.join(map(lambda pattern: f'(?P<{pattern[0]}>{pattern[1]})', tokens.items())))
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
                #escaping whitespace
                while code_line[self.col-1] == ' ':
                    self.col += 1
                
                #find lexemes
                lexeme = self.patterns.match(code_line, self.col-1)
                if lexeme:
                    token_name = lexeme.lastgroup
                    token_value = lexeme.group(lexeme.lastgroup)
                    #check if lexeme is symbol
                    if token_name in ['IDENTIFIER', 'CONST_STRING', 'CONST_NUMBER']:
                        #add to symbol table and change token name
                        token_name = 'ID_TK, ' + self.symbol_table.add_item(token_value, token_name)
                    #tokenize
                    token = Token(line=self.line, col=self.col, token_name=token_name)
                    self.col = lexeme.end()+1
                    token_line.append(token)
                else:
                    pass
                    #TODO: raise issue
            self.line += 1
            token_stream.append(token_line)

        return token_stream