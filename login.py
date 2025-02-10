import pickle
import numpy as np
import streamlit as st
import json
import bcrypt
import os
import subprocess
import gdown

URLS = [
    "pages/movies1.pkl",
    "pages/df1.pkl",
    "pages/df_fr_content.pkl"
    's.pkl'
    'pages/users.pkl'
    "app_final.py"
    "users.json"
]

for url in URLS:
    filename = url.split("/")[-1]  # Extract filename from URL
    try:
        subprocess.run(["wget", "-O", filename, url], check=True)
        print(f"Downloaded: {filename}")
    except subprocess.CalledProcessError:
        print(f"Failed to download {url}")


# Google Drive file ID (Extract from URL)
file_id = "1POu4NYaDFTrizqjfRIsIfUQ9klA6CmUk"
output_file = "s.pkl"

# Download file
gdown.download(f"https://drive.google.com/uc?id={file_id}", output_file, quiet=False)

print("Download completed!")



if "verified" not in st.session_state:
    st.session_state.verified = False

user_file= "users.json"


def load_file():
    if not os.path.exists(user_file):
        return  {}
    with open (user_file,"r") as file:
        return json.load(file)

def save_user_file(userdict):
    with open (user_file,"w") as file:
        return json.dump(userdict,file,indent=4)

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(password,hashed_password):
        return  bcrypt.checkpw(password.encode(),hashed_password.encode())

users=load_file()

st.title("Your Next Binge 🍿")

userid=st.text_input("enter user id")
password=st.text_input("enter your password",type="password")

if st.button("Login"):
    if userid in users and check_password(password,users[userid]):
        st.success("You are logged in,Welcome back")

        st.session_state.verified=True
        st.session_state.user_index = list(users.keys()).index(userid)
    if userid in users and not  check_password(password, users[userid]):
        st.warning("Invalid password!")

    if userid not in users:
        st.warning("User not found")

if st.button("Register"):
    if userid in users:
        st.warning("User already exists")
    else:
        users[userid]=hash_password(password)
        save_user_file(users)
        st.success(f"User {userid} registered successfully! You can now log in.")
        with open("s.pkl", "rb") as f:
            usermatrix =pickle.load(f)

        new_user_vector = np.zeros((1, usermatrix.shape[1]))
        usermatrix = np.vstack([usermatrix, new_user_vector])

        with open("s.pkl", "wb") as f:
            pickle.dump(usermatrix, f)


if st.session_state.verified:
    st.switch_page("pages/app_final.py")
