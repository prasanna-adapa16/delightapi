import streamlit as st
import requests

st.title("📝 Register")

api_url = "http://127.0.0.1:8000/api/register/"

with st.form("register_form"):
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    full_name = st.text_input("Full Name")
    mobile_number = st.text_input("Mobile Number")
    address = st.text_area("Address")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    location = st.selectbox("Location", ["Hyderabad", "Bangalore", "Mumbai"])

    submitted = st.form_submit_button("Register")

    if submitted:
        if password != confirm_password:
            st.error("Passwords do not match!")
        else:
            payload = {
                "username": username,
                "email": email,
                "password": password,
                "confirm_password": confirm_password,
                "full_name": full_name,
                "mobile_number": mobile_number,
                "address": address,
                "gender": gender,
                "location": location
            }

            try:
                res = requests.post(api_url, json=payload)
                if res.status_code == 201:
                    st.success("Registered successfully! Now you can log in.")
                else:
                    st.error(f"Registration failed: {res.json()}")
            except Exception as e:
                st.error(f"Error: {e}")

