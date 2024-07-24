import json
import os.path

from cube import RubiksCube
from solver import IDA_star, build_heuristic_dict
from main_window import Block, Blocks

running = False

MAX_MOVES = 5
NEW_HEURISTICS = False
HEURISTIC_FILE = 'Rubiks-Cube-Solver/heuristic.json'

if running:
    cube = RubiksCube(state=Blocks.get_colours_string())
    cube.show()
    print('-----------')

    if os.path.exists(HEURISTIC_FILE):
        with open(HEURISTIC_FILE) as f:
            h_db = json.load(f)
    else:
        h_db = None

    if h_db is None or NEW_HEURISTICS is True:
        actions = [(r, n, d) for r in ['h', 'v', 'fb'] for d in [0, 1] for n in range(cube.n)]
        h_db = build_heuristic_dict(
            cube.stringify(),
            actions,
            max_moves = MAX_MOVES,
            heuristic = h_db
        )

        with open(HEURISTIC_FILE, 'w', encoding='utf-8') as f:
            json.dump(
                h_db,
                f,
                ensure_ascii=False,
                indent=4
            )

    solver = IDA_star(h_db)
    moves = solver.run(cube.stringify())
    print(moves)

    for m in moves:
        if m[0] == 'h':
            cube.horizontal_twist(m[1], m[2])
        elif m[0] == 'v':
            cube.vertical_twist(m[1], m[2])
        elif m[0] == 'fb':
            cube.side_twist(m[1], m[2])
    cube.show()
