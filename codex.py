separators = [';', ' ', ':']
operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
             '==', '&&', '||', '!', '!=', '&', '^', ',']
reservedWords = ['begin', 'end', 'integer', 'float', 'list', 'in', 
                 'out', 'while', 'if', 'for', 'bwhile', 'ewhile', 'bif', 
                 'elif', 'enif', 'inc', 'bfor', 'enfor']

reservedCharacters = separators + operators + reservedWords
codex = dict([(reservedCharacters[i], i + 2) for i in range(len(reservedCharacters))])
codex['identifier'] = 0
codex['constant'] = 1