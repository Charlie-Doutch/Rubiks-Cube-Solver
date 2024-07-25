import json
import os.path

from cube import RubiksCube
from solver import IDA_star, build_heuristic_dict
from main_window import Blocks

class SolveCube:
    MAX_MOVES = 5
    NEW_HEURISTICS = False
    HEURISTIC_FILE = 'Rubiks-Cube-Solver/heuristic.json'

    def __init__(self):
        # Initialize the cube with the current state
        self.cube = RubiksCube(state=Blocks.get_colours_string())
        self.cube.show()
        print('-----------')

        # Load heuristics or build new ones
        self.h_db = self.load_or_build_heuristics()

        # Initialize the solver
        self.solver = IDA_star(self.h_db)

    def load_or_build_heuristics(self):
        # Check if heuristic file exists
        if os.path.exists(self.HEURISTIC_FILE):
            with open(self.HEURISTIC_FILE) as f:
                h_db = json.load(f)
        else:
            h_db = None

        # Build new heuristics if needed
        if h_db is None or self.NEW_HEURISTICS:
            actions = [(r, n, d) for r in ['h', 'v', 'fb'] for d in [0, 1] for n in range(self.cube.n)]
            h_db = build_heuristic_dict(
                self.cube.stringify(),
                actions,
                max_moves=self.MAX_MOVES,
                heuristic=h_db
            )

            # Save heuristics to file
            with open(self.HEURISTIC_FILE, 'w', encoding='utf-8') as f:
                json.dump(
                    h_db,
                    f,
                    ensure_ascii=False,
                    indent=4
                )
        return h_db

    def solve(self):
        # Solve the cube and apply moves
        moves = self.solver.run(self.cube.stringify())
        print(moves)

        for m in moves:
            if m[0] == 'h':
                self.cube.horizontal_twist(m[1], m[2])
            elif m[0] == 'v':
                self.cube.vertical_twist(m[1], m[2])
            elif m[0] == 'fb':
                self.cube.side_twist(m[1], m[2])
        self.cube.show()