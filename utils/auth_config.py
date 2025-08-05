import streamlit_authenticator as stauth

# Username: [name, username, password]
users = [
    {"name": "Dr. Smith", "username": "doctor", "password": "pass123", "role": "Doctor"},
    {"name": "Audit Officer", "username": "auditor", "password": "audit456", "role": "Auditor"},
    {"name": "Admin", "username": "admin", "password": "admin789", "role": "Admin"}
]

names = [user["name"] for user in users]
usernames = [user["username"] for user in users]
passwords = [user["password"] for user in users]
roles = dict(zip(usernames, [user["role"] for user in users]))

hashed_pw = stauth.Hasher(passwords).generate()
