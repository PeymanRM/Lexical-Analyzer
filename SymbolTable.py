from tabulate import tabulate

class Symbol_Table:

    def __init__(self):
        self.table = []
    
    def __str__(self):
        table_list = [symbol.values() for symbol in self.table]
        return tabulate(table_list, headers=['ID', 'SYMBOL NAME', 'ATTRIBUTE'], tablefmt='grid')
    
    def __repr__(self):
        return self.table
    
    def add_item(self, symbol_name, attribute):
        #check if identifier already exists
        if attribute == 'IDENTIFIER':
            for symbol in self.table:
                if symbol['symbol_name'] == symbol_name:
                    return symbol['id']
        symbol = {
            'id': str(len(self.table)+1),
            'symbol_name': symbol_name,
            'attribute': attribute
            }
        self.table.append(symbol)
        return symbol['id']