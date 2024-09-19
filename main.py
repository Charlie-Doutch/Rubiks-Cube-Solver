# Credit to Ben Bellerose for the Basis of this Solving Code
import json
import os.path
from cube import RubiksCube
from solver import IDA_star, build_heuristic_dict
import threading

class SolveCube:
    MAX_MOVES = 5
    NEW_HEURISTICS = False
    HEURISTIC_FILE = 'Rubiks-Cube-Solver/heuristic.json'

    def __init__(self, cube_state):
        # Initialize the cube with the current state
        self.cube = RubiksCube(state=cube_state)
        self.cube.show()
        print('-----------')

        # Load heuristics or build new ones
        self.h_db = self.load_or_build_heuristics()

        # Initialize the solver
        if self.USE_BFS:
            self.solve_method = bfs_solve_rubiks_cube
        else:
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
        cube_string = self.cube.stringify()
        print("Cube state before solving:", cube_string)

        solver_thread = threading.Thread(target=self.solve)
        solver_thread.start()

        # Use IDA* solver
        moves = self.solver.run(cube_string)

        print("Moves returned by the solver:", moves)

        if not moves:
            print("No moves returned by the solver.")
        
        for m in moves:
            if m[0] == 'h':
                self.cube.horizontal_move(m[1], m[2])
            elif m[0] == 'v':
                self.cube.vertical_move(m[1], m[2])
            elif m[0] == 'fb':
                self.cube.front_back_move(m[1], m[2])
        self.cube.show()
