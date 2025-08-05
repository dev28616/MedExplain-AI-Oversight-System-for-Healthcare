# generate_hash.py
import streamlit_authenticator as stauth

# Plaintext passwords
passwords = ['admin123', 'reviewer123']

# Hash the passwords
hashed_passwords = stauth.Hasher(passwords).generate()

# Print the result
print(hashed_passwords)
