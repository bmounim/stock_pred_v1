import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# Initialize Firebase
cred = credentials.Certificate("secrets/secrets2.json")
firebase_admin.initialize_app(cred)

def app():
    st.title('Stock Analysis User Portal')

    # Enhanced styles with a modern color palette and fonts
    st.markdown(
        """
        <style>
        .stTextInput>div>div>input, .stPassword>div>div>input {
            border-radius: 20px;
        }
        .stButton>button {
            border-radius: 20px;
            border: 1px solid #4CAF50;
            color: white;
            background-color: #4CAF50;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        </style>
        """, unsafe_allow_html=True
    )


    
    # User icon at the top center
    st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <i class="fas fa-user-circle" style="font-size: 4em; color: #f1c40f;"></i>
        </div>
    """, unsafe_allow_html=True)

    # Initialize session state variables
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    if "signedout" not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False

    # Functions to handle login and logout
    def f(): 
        try:
            user = auth.get_user_by_email(email)
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.signedout = True
            st.session_state.signout = True    
        except: 
            st.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''

    # User authentication fields with icons
    email = st.text_input('Email Address', placeholder="Email Address")
    password = st.text_input('Password', type='password', placeholder="**********")

    # Account login and creation
    if not st.session_state["signedout"]:
        choice = st.radio('Choose an option:', ['Login', 'Sign up'])

        if choice == 'Sign up':
            username = st.text_input("Enter your unique username")
            
            if st.button('Create my account'):
                user = auth.create_user(email=email, password=password, uid=username)
                st.success('Account created successfully!')
                st.markdown('Please login using your email and password')
                st.balloons()
        else:
            st.button('Login', on_click=f)
    
    # Account dashboard
    if st.session_state.signout:
        st.markdown(f'<div style="color: white;">Name: {st.session_state.username}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="color: white;">Email ID: {st.session_state.useremail}</div>', unsafe_allow_html=True)
        st.button('Sign out', on_click=t)