# Coded by Peyman Roohi-Moghadam

from TOKENS import TOKENS

#! test code, should be removed in future
SOURCE_CODE = \
"""
x = 6
print x
if ( x == 6 ) {
    print "hi"
}
else {
    print 'bye'
}
"""

token_stream = []

for line in SOURCE_CODE.split('\n'):
    token_line = []

    lexemes = line.split(" ")
    for lexeme in lexemes:
        if lexeme != '': # ignoring whitespaces
            token_line.append(TOKENS.get(lexeme, lexeme)) # TODO: defining a func for generating id tokens and symbol table
    
    token_stream.append(token_line)

print(token_stream)