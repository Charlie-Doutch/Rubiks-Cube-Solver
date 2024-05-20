from random import randint, choice

class RubiksCube:
    
    # Rubiks Cube Class

    def __init__(self, n = 3, colours = ['w', 'o', 'g', 'r', 'b', 'y'], state = None):
        """
        n = number for width and height of cube
        colours = list with first letter of every colour
        state = String representing state of cube

        Initialises Cube
        """

        if state is None:
            self.n = n
            self.colours = colours
            self.reset()
        else:
            self.n = int((len(state) / 6) ** (0.5))
            self.colours = []
            self.cube = [[[]]]
            for i, s in enumerate(state):
                if s not in self.colours:
                    self.colours.append(s)
                    self.cube[-1][-1].append(s)
                if len(self.cube[-1][-1]) == self.n and len(self.cube[-1]) < self.n:
                    self.cube[-1].append([])
                elif len(self.cube[-1][-1]) == self.n and len(self.cube[-1]) == self.n and i < len(state) -1:
                    self.cube.append([[]])

    def reset(self):
        """
        Reset Cube
        """
        self.cube = [[[c for x in range(self.n)] for y in range(self.n)] for c in self.colours]

    def solved(self):
        """
        Determine if cube is solved,
        return bool
        """
        for side in self.cube:
            hold = []
            check = True
            for row in side:
                if len(set(row)) == 1:
                    hold.append(row[0])
                else:
                    check = False
                    break
            if check == False:
                break
            if len(set(hold)) > 1:
                check = False
                break
        return check
    
    def createString(self):
        """
        Creates string representation of cube
        """
        return ''.join([i for r in self.cube for s in r for i in s])

    def show(self):
        """
        Shows the Rubik's Cube

        Temp function until this code is implemented with the program window
        """
        spacing = f'{" " * (len(str(self.cube[0][0])) + 2)}'
        l1 = '\n'.join(spacing + str(c) for c in self.cube[0])
        l2 = '\n'.join('  '.join(str(self.cube[i][j]) for i in range(1, 5)) for j in range(len(self.cube[0])))
        l3 = '\n'.join(spacing + str(c) for c in self.cube[5])
        print(f'{l1}\n\n{l2}\n\n{l3}')

    def horizontal_move(self, row, direction):
        """
        row - integer representing which row to move
        direction - boolean representing left or right turn
        """
        if row < len(self.cube[0]):
            if direction == 0: #Left Move
                self.cube[1][row], self.cube[2][row], self.cube[3][row], self.cube[4][row] = (self.cube[2][row],
                                                                                              self.cube[3][row],
                                                                                              self.cube[4][row],
                                                                                              self.cube[1][row])
            
            elif direction == 1: #Right Move
                self.cube[1][row], self.cube[2][row], self.cube[3][row], self.cube[4][row] = (self.cube[4][row],
                                                                                              self.cube[1][row],
                                                                                              self.cube[2][row],
                                                                                              self.cube[3][row])
            else: #Print error message
                print(f'ERROR - direction has to be 0 (left) or 1 (right)') 
                return