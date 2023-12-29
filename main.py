# Coded by Peyman Roohi-Moghadam

from TOKENS import TOKENS
from LexicalAnalyzer import Lexical_Analyzer
from tabulate import tabulate 

#! test code, should be removed in future
SOURCE_CODE = \
"""
x = 6
print x
if (x==6 ) {
    print("hi")
}
else {
    print 'bye'
}
"""
analyzer = Lexical_Analyzer(TOKENS, SOURCE_CODE)
token_stream = analyzer.tokenize()

print(*token_stream, sep="\n")
t = []
for tl in token_stream:
    for tk in tl:
        t.append([tk.line, tk.col, tk.token_name])
print(tabulate(t, headers=['line', 'col', 'token'], tablefmt='grid'))
print(analyzer.symbol_table)
