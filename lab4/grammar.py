class Grammar:
    @staticmethod
    def parseLine(line):
        return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]

    @staticmethod
    def parseConsole(line):
        return [value.strip() for value in line.strip()[1:-1].strip().split(',')]

    @staticmethod
    def fromFile(fileName):
        with open(fileName) as file:
            N = Grammar.parseLine(file.readline())
            E = Grammar.parseLine(file.readline())
            S = file.readline().split('=')[1].strip()
            P = Grammar.parseRules(Grammar.parseLine(''.join([line for line in file])))

            return Grammar(N, E, P, S)

    @staticmethod
    def fromConsole():
        N = Grammar.parseConsole(input('N = '))
        E = Grammar.parseConsole(input('E = '))
        S = input('S = ')
        P = Grammar.parseRules(Grammar.parseConsole(input('P = ')))

        return Grammar(N, E, P, S)
