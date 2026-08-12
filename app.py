import streamlit as st
from db import fetch_users, fetch_players, add_user

st.set_page_config(page_title="Friends Fantasy League", page_icon="⚽", layout="centered")

# 1. Initialize session state to track if someone is logged in
if "logged_in_user" not in st.session_state:
    st.session_state["logged_in_user"] = None

def login(user_data):
    st.session_state["logged_in_user"] = user_data
    st.rerun()

def logout():
    st.session_state["logged_in_user"] = None
    st.rerun()

# ==========================================
# PAGE 1: THE LOGIN SCREEN
# ==========================================
if st.session_state["logged_in_user"] is None:
    st.title("⚽ Friends League Login")
    
    users = fetch_users()
    
    # Dropdown to select your existing profile
    if users:
        st.subheader("Welcome Back")
        user_dict = {u['friend_name']: u for u in users}
        selected_name = st.selectbox("Who are you?", ["-- Select Manager --"] + list(user_dict.keys()))
        
        if st.button("Enter App", type="primary"):
            if selected_name != "-- Select Manager --":
                login(user_dict[selected_name])
            else:
                st.error("Please select your name to enter.")
                
    st.divider()
    
    # Registration for friends who haven't joined yet
    st.subheader("New Manager? Register Here")
    with st.form("register_form"):
        new_name = st.text_input("Your Name")
        new_team = st.text_input("Team Name")
        submitted = st.form_submit_button("Join League")
        
        if submitted and new_name and new_team:
            add_user(new_name, new_team)
            st.success("Registered! You can now select your name from the dropdown above.")
            st.rerun()

# ==========================================
# PAGE 2: THE MAIN APP (After Login)
# ==========================================
else:
    user = st.session_state["logged_in_user"]
    
    # Top Header Panel
    col1, col2 = st.columns([3, 1])
    col1.markdown(f"### ⚽ {user['team_name']}")
    col1.caption(f"Manager: {user['friend_name']}")
    if col2.button("Logout"):
        logout()
        
    # The 3 Core Tabs
    tab1, tab2, tab3 = st.tabs(["📋 Your Squad", "🏆 League", "🏃 Players"])
    
    with tab1:
        st.subheader("Your Starting 11")
        st.info("The pitch view and your drafted players will appear here.")
        
    with tab2:
        st.subheader("League Standings")
        all_users = fetch_users()
        if all_users:
            # Sort managers by total points descending
            sorted_users = sorted(all_users, key=lambda x: x.get('total_points', 0), reverse=True)
            for i, u in enumerate(sorted_users):
                st.write(f"**{i+1}. {u['team_name']}** (*{u['friend_name']}*) — {u.get('total_points', 0)} pts")
                
    with tab3:
        st.subheader("Player Market")
        players = fetch_players()
        if players:
            for p in players:
                st.write(f"**{p['name']}** | {p['club']} | `{p['position']}`")
