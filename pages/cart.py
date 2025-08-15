import streamlit as st
import random

# Sample cake images
CAKE_IMAGES = [
    "https://tse3.mm.bing.net/th/id/OIP.GTsmyuEquu6pDVBJjYewlgHaLH?pid=Api&P=0&h=180",
    "https://auctioneersoftware.s3.amazonaws.com/bar/2020/12/medium/j1QJnGyQ9HYBLcrtW44LMant.jpeg",
    "https://www.homestylebakery.com/wp-content/uploads/2020/05/Red-Velvet-Cake-with-Cream-Cheese-Icing.jpg",
    "https://tse2.mm.bing.net/th/id/OIP.CO_j9JWiZB4WaXbs9xxjNAHaKr?pid=Api&P=0&h=180",
    "https://img.freepik.com/premium-photo/tiramisu-delight_1013369-3511.jpg",
    "https://i0.wp.com/www.thelittleblogofvegan.com/wp-content/uploads/2021/09/vegan-carrot-cake.jpg?fit=1543%2C1920&ssl=1",
   
]

# Sample cart data
def get_sample_cart():
    cakes = [
        {
            "id": 1,
            "name": "Chocolate Truffle",
            "price": 500,
            "flavour": "Chocolate",
            "store": "Sweet Treats Bakery",
            "description": "Rich chocolate cake with ganache topping",
            "store_address": "123 Cake Street, Delhi",
        },
        {
            "id": 2,
            "name": "Vanilla Cream Delight",
            "price": 450,
            "flavour": "Vanilla",
            "store": "Creamy Delights",
            "description": "Classic vanilla cake with fresh cream",
            "store_address": "456 Dessert Lane, Mumbai",
        },
        {
            "id": 3,
            "name": "Red Velvet Magic",
            "price": 600,
            "flavour": "Red Velvet",
            "store": "Velvet Dreams",
            "description": "Red velvet cake with cream cheese frosting",
            "store_address": "789 Bakery Road, Bangalore",
        },
        {
            "id": 4,
            "name": "Strawberry Shortcake",
            "price": 550,
            "flavour": "Strawberry",
            "store": "Berry Fresh",
            "description": "Light sponge cake with fresh strawberries",
            "store_address": "321 Fruit Garden, Chennai",
        },
        {
            "id": 5,
            "name": "Tiramisu Delight",
            "price": 700,
            "flavour": "Coffee",
            "store": "Italian Delights",
            "description": "Italian classic with coffee-soaked ladyfingers",
            "store_address": "654 Coffee Street, Hyderabad",
        },
        {
            "id": 6,
            "name": "Carrot Cake Supreme",
            "price": 480,
            "flavour": "Carrot",
            "store": "Healthy Bites",
            "description": "Moist carrot cake with walnuts and cream cheese",
            "store_address": "987 Wellness Lane, Pune",
        },
    ]
    # Assign random images
    for cake in cakes:
        cake["image"] = random.choice(CAKE_IMAGES)
    return cakes

# Session state initialization
if "cart" not in st.session_state:
    st.session_state.cart = get_sample_cart()
if "selected_cake_id" not in st.session_state:
    st.session_state.selected_cake_id = None
if "show_details" not in st.session_state:
    st.session_state.show_details = False
if "show_select_modal" not in st.session_state:
    st.session_state.show_select_modal = False
if "selected_items" not in st.session_state:
    st.session_state.selected_items = []
if "show_purchase_modal" not in st.session_state:
    st.session_state.show_purchase_modal = False
if "search_term" not in st.session_state:
    st.session_state.search_term = ""

# Page configuration for full width
st.set_page_config(
    page_title="Sweet Delights - Cake Cart",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for aesthetics
st.markdown("""
    <style>
    body { 
        background: #ffe6e6; 
    }
    .main-header {
        background: linear-gradient(90deg, #ffb6b9, #fcd5ce, #b5ead7, #c7ceea);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: #333;
        font-size: 3rem;
        font-weight: bold;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    .search-container {
        background: white;
        border-radius: 25px;
        padding: 0.5rem 1rem;
        border: 2px solid #ffb6b9;
        margin-bottom: 1rem;
    }
    .cake-card {
        background: linear-gradient(135deg, #ffffff 50%, #f8f8f8 50%);
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 6px 20px rgba(255,182,185,0.25);
        transition: transform 0.3s ease;
        border: 3px solid #ffb6b9;
        min-height: 400px;
    }
    .cake-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 30px rgba(255,182,185,0.35);
    }
    .cake-img {
        width: 100%;
        height: 220px;
        object-fit: cover;
        border-radius: 15px;
        margin-bottom: 1.5rem;
        border: 3px solid #fcd5ce;
    }
    .price-tag {
        background: linear-gradient(45deg, #ffb6b9, #fcd5ce);
        color: #333;
        padding: 0.6rem 1.5rem;
        border-radius: 25px;
        font-weight: bold;
        font-size: 1.2rem;
        display: inline-block;
        margin-bottom: 0.8rem;
    }
    .flavour-tag {
        background: linear-gradient(45deg, #b5ead7, #c7ceea);
        color: #333;
        padding: 0.5rem 1.2rem;
        border-radius: 20px;
        font-weight: bold;
        font-size: 1.1rem;
        display: inline-block;
        margin-bottom: 0.8rem;
    }
    .modal {
        background: #fff0f6;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(255,182,185,0.3);
        margin: 2rem auto;
        max-width: 500px;
        text-align: center;
        border: 2px solid #ffb6b9;
    }
    .stButton>button {
        border-radius: 20px !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        padding: 0.6rem 1.5rem !important;
        background: linear-gradient(90deg, #ffb6b9, #fcd5ce) !important;
        color: #333 !important;
        border: none !important;
        margin: 0.3rem 0.4rem 0.3rem 0 !important;
        box-shadow: 0 3px 10px rgba(255,182,185,0.25) !important;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #b5ead7, #c7ceea) !important;
        color: #222 !important;
        transform: scale(1.05);
    }
    .total-section {
        background: linear-gradient(90deg, #ffb6b9, #fcd5ce);
        color: #333;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        margin-top: 2rem;
        box-shadow: 0 4px 15px rgba(255,182,185,0.2);
    }
    .purchase-all-btn {
        background: linear-gradient(90deg, #ff6b6b, #ff8e8e) !important;
        color: white !important;
        font-size: 1.4rem !important;
        font-weight: bold !important;
        padding: 1rem 2rem !important;
        border-radius: 25px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(255,107,107,0.3) !important;
        transition: all 0.3s ease !important;
    }
    .purchase-all-btn:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 6px 20px rgba(255,107,107,0.4) !important;
    }
    .cake-title {
        font-size: 1.4rem;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #333;
    }
    .cake-description {
        font-size: 1rem;
        color: #666;
        margin-bottom: 1.5rem;
        line-height: 1.4;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🛒 Cart</div>', unsafe_allow_html=True)

# Top navigation bar
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    search_term = st.text_input("🔍 Search", key="search_input", placeholder="Search cakes...")
    if search_term != st.session_state.search_term:
        st.session_state.search_term = search_term
        st.rerun()

with col2:
    st.markdown('<div style="text-align: center; font-size: 1.2rem; font-weight: bold; color: #333;">🎂 Sweet Delights</div>', unsafe_allow_html=True)

with col3:
    if st.button("📋 Select Items", key="select_items_btn"):
        st.session_state.show_select_modal = True
        st.rerun()

# Filter cakes based on search
filtered_cakes = st.session_state.cart
if st.session_state.search_term:
    filtered_cakes = [
        cake for cake in st.session_state.cart 
        if st.session_state.search_term.lower() in cake['name'].lower() 
        or st.session_state.search_term.lower() in cake['flavour'].lower()
    ]

# Select Items Page
if st.session_state.show_select_modal:
    st.markdown('<div class="main-header">📋 Select Items to Purchase</div>', unsafe_allow_html=True)
    
    # Back button
    if st.button("← Back to Cart", key="back_to_cart"):
        st.session_state.show_select_modal = False
        st.rerun()
    
    # Initialize selected items if not exists
    if "temp_selected_items" not in st.session_state:
        st.session_state.temp_selected_items = []
    
    # Display cakes in rows of 3 with checkboxes
    for i in range(0, len(filtered_cakes), 3):
        row_cakes = filtered_cakes[i:i+3]
        cols = st.columns(3)
        
        for j, cake in enumerate(row_cakes):
            with cols[j]:
                st.markdown(f"""
                    <div class="cake-card">
                        <img src="{cake['image']}" class="cake-img"/>
                        <div class="cake-title">{cake['name']}</div>
                        <div class="price-tag">₹{cake['price']}</div>
                        <div class="flavour-tag">{cake['flavour']}</div>
                        <div class="cake-description">{cake['description'][:100]}...</div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Checkbox for selection
                if st.checkbox(f"Select {cake['name']}", key=f"select_{cake['id']}", value=cake['id'] in st.session_state.temp_selected_items):
                    if cake['id'] not in st.session_state.temp_selected_items:
                        st.session_state.temp_selected_items.append(cake['id'])
                else:
                    if cake['id'] in st.session_state.temp_selected_items:
                        st.session_state.temp_selected_items.remove(cake['id'])
    
    # OK button at bottom
    if st.button("OK", key="ok_select", use_container_width=True):
        if st.session_state.temp_selected_items:
            st.session_state.selected_items = st.session_state.temp_selected_items.copy()
            st.session_state.show_select_modal = False
            st.session_state.show_purchase_modal = True
            st.rerun()
        else:
            st.warning("Please select at least one item!")

# Purchase Modal
elif st.session_state.show_purchase_modal:
    selected_cakes = [cake for cake in filtered_cakes if cake['id'] in st.session_state.selected_items]
    total_price = sum(cake['price'] for cake in selected_cakes)
    
    st.markdown('<div class="main-header">🛒 Purchase Confirmation</div>', unsafe_allow_html=True)
    
    # Back button
    if st.button("← Back to Selection", key="back_to_selection"):
        st.session_state.show_purchase_modal = False
        st.session_state.show_select_modal = True
        st.rerun()
    
    # Display selected cakes
    st.markdown(f'<div class="total-section">Total Price: ₹{total_price}</div>', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center; margin: 2rem 0;">Selected Items:</h3>', unsafe_allow_html=True)
    
    # Display selected cakes in a grid
    for i in range(0, len(selected_cakes), 3):
        row_cakes = selected_cakes[i:i+3]
        cols = st.columns(3)
        
        for j, cake in enumerate(row_cakes):
            with cols[j]:
                st.markdown(f"""
                    <div class="cake-card">
                        <img src="{cake['image']}" class="cake-img"/>
                        <div class="cake-title">{cake['name']}</div>
                        <div class="price-tag">₹{cake['price']}</div>
                        <div class="flavour-tag">{cake['flavour']}</div>
                        <div class="cake-description">{cake['description'][:100]}...</div>
                    </div>
                """, unsafe_allow_html=True)
    
    # Action buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Continue to Purchase", key="continue_purchase", use_container_width=True):
            # Remove selected items from cart
            st.session_state.cart = [cake for cake in st.session_state.cart if cake['id'] not in st.session_state.selected_items]
            st.session_state.show_purchase_modal = False
            st.session_state.selected_items = []
            st.session_state.temp_selected_items = []
            st.success("🎉 Purchase successful!")
            st.rerun()
    with col2:
        if st.button("Cancel", key="cancel_purchase", use_container_width=True):
            st.session_state.show_purchase_modal = False
            st.session_state.selected_items = []
            st.session_state.temp_selected_items = []
            st.rerun()

# Cake Details Popup - Removed as we'll show details inline

# Main cart display
if filtered_cakes:
    # Display cakes in rows of 3
    for i in range(0, len(filtered_cakes), 3):
        row_cakes = filtered_cakes[i:i+3]
        cols = st.columns(3)
        
        for j, cake in enumerate(row_cakes):
            with cols[j]:
                # Check if this cake is selected for details
                show_details_for_this_cake = (st.session_state.show_details and 
                                           st.session_state.selected_cake_id == cake['id'])
                
                if show_details_for_this_cake:
                    # Expanded card with full details
                    st.markdown(f"""
                        <div class="cake-card" style="min-height: 600px;">
                            <img src="{cake['image']}" class="cake-img"/>
                            <div class="cake-title">{cake['name']}</div>
                            <div class="price-tag">₹{cake['price']}</div>
                            <div class="flavour-tag">{cake['flavour']}</div>
                            <div class="cake-description" style="color: #000000; font-size: 1rem; line-height: 1.6; margin: 1rem 0;">
                                <strong>Description:</strong><br>
                                {cake['description']}
                            </div>
                            <hr style="margin: 1.5rem 0; border: 1px solid #ffb6b9;">
                            <div style="margin-top: 1rem; color: #000000;">
                                <p style="margin: 0.5rem 0; font-size: 1rem;"><strong>Store:</strong> {cake['store']}</p>
                                <p style="margin: 0.5rem 0; font-size: 1rem;"><strong>Address:</strong> {cake['store_address']}</p>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Close details button
                    if st.button("Close Details", key=f"close_{cake['id']}", use_container_width=True):
                        st.session_state.show_details = False
                        st.session_state.selected_cake_id = None
                        st.rerun()
                else:
                    # Normal card
                    st.markdown(f"""
                        <div class="cake-card">
                            <img src="{cake['image']}" class="cake-img"/>
                            <div class="cake-title">{cake['name']}</div>
                            <div class="price-tag">₹{cake['price']}</div>
                            <div class="flavour-tag">{cake['flavour']}</div>
                            <div class="cake-description">{cake['description'][:100]}...</div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("View Details", key=f"view_{cake['id']}"):
                            st.session_state.selected_cake_id = cake['id']
                            st.session_state.show_details = True
                            st.rerun()
                    with col2:
                        if st.button("Purchase", key=f"purchase_{cake['id']}"):
                            st.session_state.selected_items = [cake['id']]
                            st.session_state.show_purchase_modal = True
                            st.rerun()

    # Total cost and purchase all at bottom
    total_cost = sum(cake['price'] for cake in filtered_cakes)
    st.markdown(f"""
        <div class="total-section">
            💰 Total Cost: ₹{total_cost}
        </div>
    """, unsafe_allow_html=True)
    
    # Purchase All button
    st.markdown("""
        <style>
        .purchase-all-btn {
            background: linear-gradient(90deg, #ff6b6b, #ff8e8e) !important;
            color: white !important;
            font-size: 1.4rem !important;
            font-weight: bold !important;
            padding: 1rem 2rem !important;
            border-radius: 25px !important;
            border: none !important;
            box-shadow: 0 4px 15px rgba(255,107,107,0.3) !important;
            transition: all 0.3s ease !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    if st.button("🛒 Purchase All Items", key="purchase_all_btn", use_container_width=True):
        if filtered_cakes:
            st.session_state.selected_items = [cake['id'] for cake in filtered_cakes]
            st.session_state.show_purchase_modal = True
            st.rerun()
        else:
            st.warning("No items to purchase!")

else:
    st.info("No cakes found matching your search criteria. 🎂")