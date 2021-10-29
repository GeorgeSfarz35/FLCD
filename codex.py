separators = [';', ' ', ':', '\n']
operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
             '==', '&&', '||', '!', '!=', '&', '^', ',']
reservedWords = ['begin', 'end', 'integer', 'float', 'list', 'in', 
                 'out', 'while', 'if', 'bwhile', 'ewhile', 'bif', 
                 'elif', 'eif', 'inc']

reservedCharacters = separators + operators + reservedWords
codex = dict([(reservedCharacters[i], i + 2) for i in range(len(reservedCharacters))])
codex['identifier'] = 0
codex['constant'] = 1