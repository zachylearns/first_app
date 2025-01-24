import random
import streamlit as st

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

# Title and Instructions
st.title("Number Guessing Game")
st.write("Want to play a game? I'm guessing of a number between 1 and 20. Try to guess it")

# Track attempts using Streamlit's session state
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# Input from the user
guess = st.number_input("Enter your guess (1-20):", min_value=1, max_value=20, step=1, key="guess")

# Check the guess
if st.button("Submit Guess"):
    st.session_state.attempts += 1  # Increment attempts
    if guess < secret_number:
        st.write("MORE")
    elif guess > secret_number:
        st.write("Whoa, too much")
    else:
        st.write(f"Nice job, nerd! It only took you {st.session_state.attempts} attempts...")
        st.write("Reload the page to play again.")
