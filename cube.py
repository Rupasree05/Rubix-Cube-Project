import random

# -----------------------------
# STEP 1: Cube Representation
# -----------------------------
# 6 faces: U=Up, D=Down, F=Front, B=Back, L=Left, R=Right
# Each face is a 3x3 grid with a color letter

def create_cube():
    return {
        'U': [['W']*3 for _ in range(3)],  # White
        'D': [['Y']*3 for _ in range(3)],  # Yellow
        'F': [['G']*3 for _ in range(3)],  # Green
        'B': [['B']*3 for _ in range(3)],  # Blue
        'L': [['O']*3 for _ in range(3)],  # Orange
        'R': [['R']*3 for _ in range(3)]   # Red
    }

# -----------------------------
# STEP 2: Helper Functions
# -----------------------------
def rotate_face(face):
    """Rotate a face 90° clockwise"""
    return [list(row) for row in zip(*face[::-1])]

def print_cube(cube):
    """Print cube faces in text form"""
    for face, grid in cube.items():
        print(face)
        for row in grid:
            print(" ".join(row))
        print()

# -----------------------------
# STEP 3: Moves (example: R move)
# -----------------------------
def move_R(cube):
    """Rotate Right face clockwise"""
    cube['R'] = rotate_face(cube['R'])

    # Save U, F, D, B right columns
    U_col = [cube['U'][i][2] for i in range(3)]
    F_col = [cube['F'][i][2] for i in range(3)]
    D_col = [cube['D'][i][2] for i in range(3)]
    B_col = [cube['B'][2-i][0] for i in range(3)]  # reversed

    # Perform rotation
    for i in range(3):
        cube['F'][i][2] = U_col[i]
        cube['D'][i][2] = F_col[i]
        cube['B'][2-i][0] = D_col[i]
        cube['U'][i][2] = B_col[i]

# -----------------------------
# STEP 4: Scramble Generator
# -----------------------------
def scramble_cube(cube, moves_count=20):
    moves = [move_R]  # For now only R, later add L, U, D, F, B
    for _ in range(moves_count):
        move = random.choice(moves)
        move(cube)

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    cube = create_cube()
    print("✅ Rubix Cube Representation:")
    print_cube(cube)

    print("➡ Applying R move...")
    move_R(cube)
    print_cube(cube)

    print("➡ Scrambling...")
    scramble_cube(cube, 5)
    print_cube(cube)
