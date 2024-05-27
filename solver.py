from random import choice
from tqdm import tqdm

from cube import RubiksCube

class IDA_star(object):
    def __init__(self, heuristic, max_depth = 20):
        """
        Initializes Solver
        
        heuristic = dictionary with past solves
        max_depth = max depth tree can go, 20 has been proven to be the most moves a rubik's cube can take
        """
        self.max_depth = max_depth
        self.threshold = max_depth
        self.min_threshold = None
        self.heuristic = heuristic
        self.moves = []

    def run(self, state):
        """
        Solves Rubik's Cube

        State = String of Rubik's cube state

        Outputs the move list to solve cube 
        """
        while True: 
            status = self.search(state, 1)
            if status:
                return self.moves
            self.moves = []
            self.threshold = self.min_threshold
        return []
