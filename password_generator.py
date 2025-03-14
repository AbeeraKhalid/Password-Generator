#PASSWORD-GENERATOR BY USING STREAMLIT,PYTHON, AND UV
import streamlit as st   # type: ignore
import random  # Import random for generating random choices
import string  # Import string to use predefined character sets


# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Includes uppercase and lowercase letters

    if use_digits:
        characters += string.digits  # Adds numbers (0-9) if selected
  
    if use_special:
        characters += (
            string.punctuation
        )  # Adds special characters 

#Generate a password by selecting random characters according to the specified length.    
    return "".join(random.choice(characters) for _ in range(length))


# Streamlit UI setup
st.title("🔐Simple-Password-Generator")  

# User input: password length (slider to select length between 7 and 38 characters)

length = st.slider("Select password length:", min_value=7, max_value=35, value=15)

# Checkbox options for including numbers and special characters in the password
use_digits = st.checkbox("Include numbers")  # Checkbox for numbers (0-9)
use_special = st.checkbox(
    "Include special characters"
)  # Checkbox for special characters (@!#$^&?*)

# Button to generate password


if st.button("Generate Password"):
    password = generate_password(


        length, use_digits, use_special
    )  # Call the password generation function
    st.write(f"Generated Password: `{password}`")  
    st.write("----------------------------------")
    st.write("Thank you for using the password generator🤗💐!")
    st.write("Created By [Abeera Khalid](https://www.linkedin.com/in/abeera-m-khalid-/)❤️")

