# Coded by Peyman Roohi-Moghadam

from TOKENS import TOKENS
from LexicalAnalyzer import Lexical_Analyzer
from tabulate import tabulate 

SOURCE_CODE = open('docs/input2.pey', 'r')
try:
    analyzer = Lexical_Analyzer(TOKENS, SOURCE_CODE.read())
    token_stream = analyzer.tokenize()
except ValueError as e:
    print(e)
finally:
    SOURCE_CODE.close()
    
print('\nToken stream:')
print(*token_stream, sep='\n')

print('\nSymbol table:')
print(analyzer.symbol_table)

print('\nTokens:')
t = []
for tl in token_stream:
    for tk in tl:
        t.append([tk.line, tk.col, tk.token_name])
print(tabulate(t, headers=['LINE', 'COL', 'TOKEN'], tablefmt='grid'))