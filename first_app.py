import streamlit as st

# Title and introduction
st.title("Welcome to My First Streamlit App!")
st.write("This app lets you interact with Python in a fun and simple way.")

# Ask the user for their name
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! Nice to meet you.")

# Ask the user for their favorite number
number = st.number_input("What's your favorite number?", step=1)
if number:
    st.write(f"Your favorite number is {number}. Cool!")

# End with a thank-you message
st.write("Thanks for trying my app!")
