import streamlit as st

# Create a text input bar
user_input = st.text_input("Enter your message:")

# Check if the user has entered anything
if user_input:
    # Display the user input
    st.write("You entered:", user_input)
