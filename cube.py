class RubiksCube:
    def __init__(self, n=3, colours=['w', 'o', 'g', 'r', 'b', 'y'], state=None):
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
            self.n = int((len(state) / 6) ** (.5))
            self.colours = []
            self.cube = [[[]]]
            for i, s in enumerate(state):
                if s not in self.colours: self.colours.append(s)
                self.cube[-1][-1].append(s)
                if len(self.cube[-1][-1]) == self.n and len(self.cube[-1]) < self.n:
                    self.cube[-1].append([])
                elif len(self.cube[-1][-1]) == self.n and len(self.cube[-1]) == self.n and i < len(state) - 1:
                    self.cube.append([[]])

    def reset(self):
        """
        Reset Cube
        """
        self.cube = [[[c for _ in range(self.n)] for _ in range(self.n)] for c in self.colours]

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
            if not check:
                break
            if len(set(hold)) > 1:
                check = False
                break
        return check

    def stringify(self):
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
        row - number representing which row you would like to move
        direction - boolean representing if you want to move right or left [left - 0, right - 1]
        Description: move desired row of rubiks cube
        """

        if direction == 0:  # move left
            self.cube[1][row], self.cube[2][row], self.cube[3][row], self.cube[4][row] = (self.cube[2][row],
                                                                                          self.cube[3][row],
                                                                                          self.cube[4][row],
                                                                                          self.cube[1][row])
        elif direction == 1:  # move right
            self.cube[1][row], self.cube[2][row], self.cube[3][row], self.cube[4][row] = (self.cube[4][row],
                                                                                          self.cube[1][row],
                                                                                          self.cube[2][row],
                                                                                          self.cube[3][row])

        # Rotating connected face
        if direction == 0:  # move left
            if row == 0:
                self.cube[0] = [list(x) for x in zip(*reversed(self.cube[0]))]  # Transpose top
            elif row == self.n - 1:
                self.cube[5] = [list(x) for x in zip(*reversed(self.cube[5]))]  # Transpose bottom
        elif direction == 1:  # move right
            if row == 0:
                self.cube[0] = [list(x) for x in zip(*self.cube[0])][::-1]  # Transpose top
            elif row == self.n - 1:
                self.cube[5] = [list(x) for x in zip(*self.cube[5])][::-1]  # Transpose bottom

    def vertical_move(self, column, direction):
        """
        column = Number indicating column to turn
        direction = Bool indicating move up or down
        """
        if column < 0 or column >= self.n:
            print(f'ERROR - column outside range. Select from 0-{self.n-1}')
            return

        for i in range(self.n):
            if direction == 0:  # Down Move
                self.cube[0][i][column], self.cube[2][i][column], self.cube[4][-i-1][-column-1], self.cube[5][i][column] = (self.cube[4][-i-1][-column-1],
                                                                                                                            self.cube[0][i][column],
                                                                                                                            self.cube[5][i][column],
                                                                                                                            self.cube[2][i][column])

            elif direction == 1:  # Up Move
                self.cube[0][i][column], self.cube[2][i][column], self.cube[4][-i-1][-column-1], self.cube[5][i][column] = (self.cube[2][i][column],
                                                                                                                            self.cube[5][i][column],
                                                                                                                            self.cube[0][i][column],
                                                                                                                            self.cube[4][-i-1][-column-1])

            else:  # Error message for debugging
                print(f'ERROR - direction must be 0 (Down) or 1 (Up)')
                return

        # Move connected pieces
        if direction == 0:  # Move Down
            if column == 0:
                self.cube[1] = [list(x) for x in zip(*self.cube[1])][::1]  # Move Left
            elif column == self.n - 1:
                self.cube[3] = [list(x) for x in zip(*self.cube[3])][::1]  # Move Right

        elif direction == 1:  # Move Up
            if column == 0:
                self.cube[1] = [list(x) for x in zip(*reversed(self.cube[1]))]  # Move Left
            elif column == self.n - 1:
                self.cube[3] = [list(x) for x in zip(*reversed(self.cube[3]))]  # Move Right

    def front_back_move(self, column, direction):
        """
        column = Number representing what column to move
        direction = Clockwise or Anticlockwise move
        """
        if column < 0 or column >= self.n:
            print(f'ERROR - column outside of range. Select from 0-{self.n-1}')
            return

        for i in range(self.n):
            if direction == 0:  # Clockwise move
                self.cube[0][column][i], self.cube[1][-i-1][column], self.cube[3][i][-column-1], self.cube[5][-column-1][-1-i] = (self.cube[3][i][-column-1],
                                                                                                                                  self.cube[0][column][i],
                                                                                                                                  self.cube[5][-column-1][-1-i],
                                                                                                                                  self.cube[1][-i-1][column])

            elif direction == 1:  # Anticlockwise move
                self.cube[0][column][i], self.cube[1][-i-1][column], self.cube[3][i][-column-1], self.cube[5][-column-1][-1-i] = (self.cube[1][-i-1][column],
                                                                                                                                  self.cube[5][-column-1][-1-i],
                                                                                                                                  self.cube[0][column][i],
                                                                                                                                  self.cube[3][i][-column-1])

            else:  # Error message for debugging
                print(f'ERROR - direction must be 0 (Clockwise) or 1 (Anticlockwise)')
                return

        # Move connected pieces
        if direction == 0:  # Clockwise move
            if column == 0:
                self.cube[4] = [list(x) for x in zip(*reversed(self.cube[4]))]  # Move Back
            elif column == self.n - 1:
                self.cube[2] = [list(x) for x in zip(*reversed(self.cube[2]))]  # Move Front

        elif direction == 1:  # Anticlockwise move
            if column == 0:
                self.cube[4] = [list(x) for x in zip(*self.cube[4])][::-1]  # Move Back
            elif column == self.n - 1:
                self.cube[2] = [list(x) for x in zip(*self.cube[2])][::-1]  # Move Front
