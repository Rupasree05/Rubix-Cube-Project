import streamlit as st
from solver import convert_to_kociemba, solve_cube

st.title("🟥 Rubik's Cube Solver in Streamlit")

st.write("Enter the colors of your cube face by face.")

colors = ["W", "Y", "R", "O", "G", "B"]

def face_input(name):
    st.subheader(f"{name} Face")
    return [
        st.selectbox(f"{name}{i+1}", colors)
        for i in range(9)
    ]

# User inputs
U = face_input("Up (U)")
R = face_input("Right (R)")
F = face_input("Front (F)")
D = face_input("Down (D)")
L = face_input("Left (L)")
B = face_input("Back (B)")

if st.button("Solve Cube"):

    # 🔍 Check color count
    all_colors = U + R + F + D + L + B
    if any(all_colors.count(c) != 9 for c in colors):
        st.error("❌ Invalid cube: each color (W,Y,R,O,G,B) must appear exactly 9 times.")
        st.stop()

    # Build cube state
    state = convert_to_kociemba(U, R, F, D, L, B)
    st.write("### Cube State Notation:")
    st.code(state)

    # Solve
    st.write("### Solution:")
    solution = solve_cube(state)
    st.success(solution)

