from codex import *
from programInternalForm import ProgramInternalForm
from lab3 import tokenGenerator, isIdentifier, isConstant
from lab2 import *

if __name__ == '__main__':
    fileName = "p2.txt"

    file = open(fileName, 'r')
    for line in file:
        print(line)

    with open(fileName, 'r') as file:
        for line in file:
            print([token for token in tokenGenerator(line, separators)])

    symbolTable = SymbolTable()
    pif = ProgramInternalForm()
    errors = False

    with open(fileName, 'r') as file:
        lineNo = 0
        for line in file:
            lineNo += 1
            for token in tokenGenerator(line[0:-1], separators):
                if token in separators + operators + reservedWords:
                    if token != ' ':
                        pif.add(codex[token], -1)
                elif isIdentifier(token):
                    id = symbolTable.add(token)
                    pif.add(codex['identifier'], symbolTable.get(token).index)
                elif isConstant(token):
                    id = symbolTable.add(token)
                    pif.add(codex['constant'], symbolTable.get(token).index)
                else:
                    #raise Exception('Unknown token ' + token + ' at line ' + str(lineNo))
                    print('Lexical Error:Unknown token ' + token + ' at line ' + str(lineNo))
                    errors = True

    if errors:
        print("The program contains errors!")
    else:
        print('Program Internal Form: \n', pif)
        print('Symbol Table: \n', symbolTable.getTreeAsList())

        print('\n\nCodex: ')
        for e in codex:
            print(e, " -> ", codex[e])