import streamlit as st
import random
st.markdown(
    """
    <style>
    /* Background image */
    .stApp {
        background-image: url("https://m.media-amazon.com/images/I/61fB-s4DPVS.jpg, width=400, height=500");
        background-size: cover;
        background-attachment: fixed;
    }

    /* Title style */
    h1 {
        color: white;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
    }

    /* Table styling */
    table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
    }
    td {
        width: 40px;
        height: 40px;
        text-align: center;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🟦 Rubik's Cube Simulator 🟦")


# -----------------------------
# STEP 1: Cube Representation
# -----------------------------
def create_cube():
    """Create a solved Rubik's Cube"""
    return {
        'U': [['W']*3 for _ in range(3)],  # Up
        'D': [['Y']*3 for _ in range(3)],  # Down
        'F': [['G']*3 for _ in range(3)],  # Front
        'B': [['B']*3 for _ in range(3)],  # Back
        'L': [['O']*3 for _ in range(3)],  # Left
        'R': [['R']*3 for _ in range(3)]   # Right
    }

# -----------------------------
# STEP 2: Helper Functions
# -----------------------------
def rotate_face(face):
    """Rotate a face 90° clockwise"""
    return [list(row) for row in zip(*face[::-1])]

# -----------------------------
# STEP 3: Moves
# -----------------------------
def move_R(cube):
    cube['R'] = rotate_face(cube['R'])
    U_col = [cube['U'][i][2] for i in range(3)]
    F_col = [cube['F'][i][2] for i in range(3)]
    D_col = [cube['D'][i][2] for i in range(3)]
    B_col = [cube['B'][2-i][0] for i in range(3)]
    for i in range(3):
        cube['F'][i][2] = U_col[i]
        cube['D'][i][2] = F_col[i]
        cube['B'][2-i][0] = D_col[i]
        cube['U'][i][2] = B_col[i]

def move_L(cube):
    cube['L'] = rotate_face(cube['L'])
    U_col = [cube['U'][i][0] for i in range(3)]
    F_col = [cube['F'][i][0] for i in range(3)]
    D_col = [cube['D'][i][0] for i in range(3)]
    B_col = [cube['B'][2-i][2] for i in range(3)]
    for i in range(3):
        cube['F'][i][0] = D_col[i]
        cube['U'][i][0] = F_col[i]
        cube['B'][2-i][2] = U_col[i]
        cube['D'][i][0] = B_col[i]

def move_U(cube):
    cube['U'] = rotate_face(cube['U'])
    F_row = cube['F'][0].copy()
    R_row = cube['R'][0].copy()
    B_row = cube['B'][0].copy()
    L_row = cube['L'][0].copy()
    cube['R'][0] = F_row
    cube['B'][0] = R_row
    cube['L'][0] = B_row
    cube['F'][0] = L_row

def move_D(cube):
    cube['D'] = rotate_face(cube['D'])
    F_row = cube['F'][2].copy()
    R_row = cube['R'][2].copy()
    B_row = cube['B'][2].copy()
    L_row = cube['L'][2].copy()
    cube['R'][2] = B_row
    cube['B'][2] = L_row
    cube['L'][2] = F_row
    cube['F'][2] = R_row

def move_F(cube):
    cube['F'] = rotate_face(cube['F'])
    U_row = cube['U'][2].copy()
    L_col = [cube['L'][2-i][2] for i in range(3)]
    D_row = cube['D'][0].copy()
    R_col = [cube['R'][i][0] for i in range(3)]
    cube['U'][2] = L_col
    for i in range(3):
        cube['R'][i][0] = U_row[i]
    cube['D'][0] = R_col[::-1]
    for i in range(3):
        cube['L'][2-i][2] = D_row[i]

def move_B(cube):
    cube['B'] = rotate_face(cube['B'])
    U_row = cube['U'][0].copy()
    L_col = [cube['L'][i][0] for i in range(3)]
    D_row = cube['D'][2].copy()
    R_col = [cube['R'][2-i][2] for i in range(3)]
    cube['U'][0] = R_col
    for i in range(3):
        cube['R'][2-i][2] = D_row[i]
    cube['D'][2] = L_col[::-1]
    for i in range(3):
        cube['L'][i][0] = U_row[i]

# Dictionary for easy mapping
move_dict = {
    "R": move_R,
    "L": move_L,
    "U": move_U,
    "D": move_D,
    "F": move_F,
    "B": move_B
}

# -----------------------------
# STEP 4: Scramble Function
# -----------------------------
def scramble_cube(cube, moves_count=20):
    moves = list(move_dict.keys())
    scramble_moves = [random.choice(moves) for _ in range(moves_count)]
    for m in scramble_moves:
        move_dict[m](cube)
    return scramble_moves

# -----------------------------
# STEP 5: Streamlit App
# -----------------------------
st.set_page_config(page_title="Rubik's Cube Simulator", layout="centered")
st.title("🟦 Rubik's Cube Simulator and Scrambler 🟦")
st.write("Simulate moves, scramble the cube, and visualize each face.")

# Initialize cube in session state
if "cube" not in st.session_state:
    st.session_state.cube = create_cube()

# Buttons for user actions
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Reset Cube"):
        st.session_state.cube = create_cube()
with col2:
    if st.button("Scramble Cube"):
        moves_applied = scramble_cube(st.session_state.cube)
        st.success(f"Scrambled with moves: {' '.join(moves_applied)}")
with col3:
    st.write("")

# Move selector
move_selected = st.selectbox("Select a move to apply:", list(move_dict.keys()))
if st.button("Apply Move"):
    move_dict[move_selected](st.session_state.cube)
    st.success(f"Applied move: {move_selected}")

# Display all cube faces
st.subheader("Cube Faces:")
for face, grid in st.session_state.cube.items():
    st.markdown(f"**{face} Face**")
    st.table(grid)
