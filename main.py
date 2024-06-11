import json
import os.path

from cube import RubiksCube
from solver import IDA_star, build_heuristic_dict

MAX_MOVES = 5
NEW_HEURISTICS = False
HEURISTIC_FILE = 'heuristic.json'

cube = RubiksCube(state ="ryrowoobobyywowrrygrwggwgbybwbbrybgowgybbrwgwrooyyrgog")
# cube.show()
print('-----------')

if os.path.exists(HEURISTIC_FILE):
    with open(HEURISTIC_FILE) as f:
        h_db = json.load(f)
else:
    h_db = None

if h_db is None or NEW_HEURISTICS is True:
    actions = [(r, n, d) for r in ['h', 'v', 'fb'] for d in [0, 1] for n in range(cube.n)]
    h_db = build_heuristic_dict(cube.createString, actions, max_moves=MAX_MOVES, heuristic=h_db)

    with open(HEURISTIC_FILE, 'w', encoding='utf-8') as f:
        json.dump(h_db, f, ensure_ascii=False, indent=4)

solver = IDA_star(h_db)
moves = solver.run(cube.createString())
print(moves) #Temp Function to store solution in terminal until window works properly

for m in moves:
    if m[0] == 'h':
        cube.horizontal_move(m[1], m[2])
    elif m[0] == 'v':
        cube.vertical_move(m[1], m[2])
    elif m[0] == 'fb':
        cube.front_back_move(m[1], m[2])

cube.show()
