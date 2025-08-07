import streamlit as st
import requests

st.session_state["token"] = "bb195b7190798c5437c0170739b5c8cbcdb05eb2"

st.title("🛒 Your Cart")

# Ensure user is logged in
if "token" not in st.session_state:
    st.warning("Please login first to access your cart.")
    st.stop()

API_BASE = "http://127.0.0.1:8000/api"
headers = {"Authorization": f"Token {st.session_state['token']}"}

# Fetch cart items
def fetch_cart():
    try:
        res = requests.get(f"{API_BASE}/cart/", headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            st.error("❌ Failed to fetch cart. (Status: {})".format(res.status_code))
            return []
    except Exception as e:
        st.error(f"⚠️ Error fetching cart: {e}")
        return []

# Remove item from cart
def remove_item(cart_id):
    try:
        res = requests.delete(f"{API_BASE}/cart/remove/{cart_id}/", headers=headers)
        if res.status_code == 204:
            st.success("✅ Item removed from cart.")
        else:
            st.error("❌ Failed to remove item.")
    except Exception as e:
        st.error(f"⚠️ Error removing item: {e}")

# Update customization
def update_item(customization_id, new_data):
    try:
        res = requests.put(f"{API_BASE}/cart/update/{customization_id}/", json=new_data, headers=headers)
        if res.status_code == 200:
            st.success("✅ Cart item updated.")
        else:
            st.error("❌ Failed to update item. Server response: " + res.text)
    except Exception as e:
        st.error(f"⚠️ Error updating item: {e}")


# Load cart
cart_items = fetch_cart()

if not cart_items:
    st.info("🧺 Your cart is empty.")
else:
    total_amount = 0

    for item in cart_items:
        cake = item["cake"]
        customization = item["customization"]

        with st.expander(f"{cake['name']} - ₹{cake['price']} x {customization['quantity']}"):
            total_amount += float(cake["price"]) * customization["quantity"]

            if cake.get("image_url"):
                st.image(cake["image_url"], width=150)
            else:
                st.text("📷 No image available.")

            st.write("🎂 **Message**:", customization["message_on_cake"])
            st.write("🥚 **Egg Option**:", customization["egg_option"])
            st.write("⚖️ **Weight**:", customization["weight_label"], 
                     f"({customization['custom_weight']} kg)" if customization["weight_label"] == "custom" else "")
            st.write("⏰ **Delivery Time**:", customization["preferred_delivery_time"])

            # Update Form
            with st.form(f"update_form_{item['id']}"):
                quantity = st.number_input("Quantity", min_value=1, value=customization["quantity"], key=f"q_{item['id']}")
                message = st.text_input("Message on Cake", customization["message_on_cake"], key=f"m_{item['id']}")
                egg_option = st.selectbox("Egg Option", ["egg", "eggless"], 
                                          index=0 if customization["egg_option"] == "egg" else 1, key=f"e_{item['id']}")
                
                submitted = st.form_submit_button("Update")
                if submitted:
                    update_item(customization["id"], {
                        "quantity": quantity,
                        "message_on_cake": message,
                        "egg_option": egg_option
                    })
                    st.rerun()

            # Remove Button
            if st.button("🗑 Remove", key=f"remove_{item['id']}"):
                remove_item(item["id"])
                st.rerun()

    st.success(f"💰 Total Amount: ₹{total_amount:.2f}")

