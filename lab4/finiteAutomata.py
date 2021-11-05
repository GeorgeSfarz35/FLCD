class FiniteAutomata:
    @staticmethod
    def parseLine(line):
        return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]

    
    @staticmethod
    def parseConsole(line):
        return [value.strip() for value in line.strip()[1:-1].strip().split(',')]

    @staticmethod
    def fromFile(fileName):
        with open(fileName) as file:
            Q = FiniteAutomata.parseLine(file.readline())
            E = FiniteAutomata.parseLine(file.readline())
            q0 = file.readline().split('=')[1].strip()
            F = FiniteAutomata.parseLine(file.readline())

            S = FiniteAutomata.parseTransitions(FiniteAutomata.parseLine(''.join([line for line in file])))

            return FiniteAutomata(Q, E, S, q0, F)

    @staticmethod
    def fromConsole():
        Q = FiniteAutomata.parseConsole(input('Q = '))
        E = FiniteAutomata.parseConsole(input('E = '))
        q0 = input('q0 = ')
        F = FiniteAutomata.parseConsole(input('F = '))

        S = FiniteAutomata.parseTransitions(FiniteAutomata.parseConsole(input('S = ')))

        return FiniteAutomata(Q, E, S, q0, F)

