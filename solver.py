# solver.py
from kociemba import solve

# Convert 6 faces into kociemba notation
# Expect 9 characters per face
def convert_to_kociemba(U, R, F, D, L, B):
    return (
        "".join(U) +
        "".join(R) +
        "".join(F) +
        "".join(D) +
        "".join(L) +
        "".join(B)
    )

def solve_cube(state):
    try:
        return solve(state)
    except Exception as e:
        return f"Error solving cube: {e}"
