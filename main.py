import streamlit as st

# Set page config
st.set_page_config(
    page_title="Delight 🍰",
    page_icon="🎂",
    layout="centered"
)

# Initialize session state variables
if "token" not in st.session_state:
    st.session_state.token = None

if "username" not in st.session_state:
    st.session_state.username = None

# Simple homepage
st.markdown("## 🎉 Welcome to Delight - SweetSpot Deliveries")
st.markdown("Explore cakes, customize orders, manage your cart, and track delivery!")

# Info
if st.session_state.token:
    st.success(f"Logged in as **{st.session_state.username}**")
else:
    st.info("Please login or register to start your sweet journey.")

# Navigation note
st.markdown("➡️ Use the **left sidebar menu** to navigate through pages.")
