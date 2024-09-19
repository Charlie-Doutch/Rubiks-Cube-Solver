# Credit to Ben Bellerose for the Basis of this Solving Code
from collections import deque
from cube import RubiksCube
import json
from random import choice
from tqdm import tqdm  # For loading bar in heuristic building

class IDA_star(object):
    def __init__(self, heuristic, max_depth=5):
        """
        Initializes Solver

        heuristic = dictionary with past solves
        max_depth = max depth tree can go, 20 has been proven to be the most moves a Rubik's Cube can take
        """
        self.max_depth = max_depth
        self.threshold = max_depth
        self.min_threshold = None
        self.heuristic = heuristic
        self.moves = []

    def run(self, state):
        """
        Solves Rubik's Cube

        state = String of Rubik's cube state

        Outputs the move list to solve cube
        """
        while True:
            status = self.search(state, 1)
            if status:
                return self.moves
            self.moves = []
            self.threshold = self.min_threshold
        return []

    def search(self, state, search_score):
        """
        state = string with state of cube
        search_score = number meaning the cost to reach a node on the tree

        Searches game tree using IDA* algorithm

        Outputs boolean saying if cube is solved or not
        """
        cube = RubiksCube(state=state)
        if cube.solved():
            return True
        elif len(self.moves) >= self.threshold:
            return False
        min_val = float('inf')
        best_action = None
        for a in [(r, n, d) for r in ['h', 'v', 'fb'] for d in [0, 1] for n in range(cube.n)]:
            cube = RubiksCube(state=state)
            if a[0] == 'h':
                cube.horizontal_move(a[1], a[2])
            elif a[0] == 'v':
                cube.vertical_move(a[1], a[2])
            elif a[0] == 'fb':
                cube.front_back_move(a[1], a[2])
            if cube.solved():
                self.moves.append(a)
                return True
            cube_str = cube.stringify()
            heuristic_score = self.heuristic[cube_str] if cube_str in self.heuristic else self.max_depth
            final_score = search_score + heuristic_score
            if final_score < min_val:
                min_val = final_score
                best_action = [(cube_str, a)]
            elif final_score == min_val:
                if best_action is None:
                    best_action = [(cube_str, a)]
                else:
                    best_action.append((cube_str, a))

        if best_action is not None:
            if self.min_threshold is None or min_val < self.min_threshold:
                self.min_threshold = min_val
            next_action = choice(best_action)
            self.moves.append(next_action[1])
            status = self.search(next_action[0], search_score + min_val)
            if status:
                return status
        return False

def build_heuristic_dict(state, actions, max_moves=20, heuristic=None):
    """
    state = string with state of cube
    actions = list of tuples representing moves that can be taken
    max_moves = number representing max number of moves allowed
    heuristic = dictionary containing heuristic map

    Creates heuristic map for finding best path to solve cube
    """
    if heuristic is None:
        heuristic = {state: 0}
    que = [(state, 0)]
    node_count = sum([len(actions) ** (x + 1) for x in range(max_moves + 1)])
    with tqdm(total=node_count, desc='Heuristic Dictionary') as pbar:
        while True:
            if not que:
                break
            s, d = que.pop()
            if d > max_moves:
                continue
            for a in actions:
                cube = RubiksCube(state=s)
                if a[0] == 'h':
                    cube.horizontal_move(a[1], a[2])
                elif a[0] == 'v':
                    cube.vertical_move(a[1], a[2])
                elif a[0] == 'fb':
                    cube.front_back_move(a[1], a[2])
                a_str = cube.stringify()
                if a_str not in heuristic or heuristic[a_str] > d + 1:
                    heuristic[a_str] = d + 1
                que.append((a_str, d+1))
                pbar.update(1)
    return heuristic
