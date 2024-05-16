from random import randint, choice

class RubiksCube:
    
    # Rubiks Cube Class

    def __init__(self, n = 3, colours = ['w', 'o', 'g', 'r', 'b', 'y'], state = None):
ghghjgjh
        """
        n = number for width and height of cube
        colours = list with first letter of every colour
        state = String representing state of cube
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
