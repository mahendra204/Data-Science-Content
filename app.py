import streamlit as st 

#simple authentication system

users = {"Mahendra": "mahendra123", "Mahi": "mahi123", "maha" : "maha123"}



def login():
    # Centering the title using custom HTML and CSS
    st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;  /* Light grey background */
    }
    .centered-title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-top: 30px;
        color: #a3293b;  /* Blue title color */
    }
    .stTextInput > label {
        font-weight: bold;
        color: #33ff3c;  /* Darker blue color for labels */
    }
    .stButton > button {
        background-color: #2949a3;  /* Blue background for buttons */
        color: #e333ff;  /* White text for buttons */
        border-radius: 15px;  /* Rounded corners for buttons */
        font-size: 16px;
        padding: 10px 30px;
    }
    .stButton > button:hover {
        background-color: #ff6e33;  /* Darker blue on hover */
        color: #33f0ff;  /* White text on hover */
    }
    </style>
    <div class="centered-title">Login Page</div>
    """,
    unsafe_allow_html=True
)
    
    username = st.text_input("Username")
    password = st.text_input("password", type = 'password')
    
    if st.button("login"):
        if username in users and users[username] == password:
            st.success(f"welcom {username}")
            st.session_state.logged_in = True
        else:
            st.error("invalid username or password")
def logout():
    if st.button("logout"):
        st.session_state.logged_in = False
        st.success("logged out successfully")
        
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if st.session_state.logged_in:
    logout()
else:
    login()
        