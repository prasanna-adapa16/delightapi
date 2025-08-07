import streamlit as st
import requests

st.title("🔐 Login")

api_url = "http://127.0.0.1:8000/api/login/"

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
        payload = {
            "username": username,
            "password": password
        }

        try:
            res = requests.post(api_url, json=payload)
            if res.status_code == 200:
                data = res.json()
                st.session_state["token"] = data["token"]
                st.session_state["user_id"] = data["user_id"]
                st.session_state["username"] = data["username"]
                st.success("Logged in successfully!")
                
                # 🔁 This is crucial to make the session changes available immediately
                st.experimental_rerun()
            else:
                st.error("Invalid credentials")
        except Exception as e:
            st.error(f"Error: {e}")
