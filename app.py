import streamlit as st
from db import fetch_players, fetch_users, add_user

st.set_page_config(page_title="Friends Fantasy League", page_icon="⚽", layout="centered")

st.title("⚽ Private Fantasy League")

tab1, tab2 = st.tabs(["👥 Managers", "🏃 Player Pool"])

with tab1:
    st.subheader("Register Manager")
    with st.form("user_form"):
        friend_name = st.text_input("Your Name")
        team_name = st.text_input("Team Name")
        submitted = st.form_submit_button("Join League")
        
        if submitted and friend_name and team_name:
            add_user(friend_name, team_name)
            st.success(f"Welcome {friend_name}! Team '{team_name}' registered.")
            st.rerun()

    st.divider()
    st.subheader("Current Managers")
    users = fetch_users()
    if users:
        for u in users:
            st.write(f"• **{u['friend_name']}** — *{u['team_name']}* ({u['total_points']} pts)")
    else:
        st.info("No managers registered yet.")

with tab2:
    st.subheader("Süper Lig Player Pool")
    players = fetch_players()
    if players:
        for p in players:
            st.write(f"**{p['name']}** | {p['club']} | `{p['position']}`")
    else:
        st.warning("No players found in database. Did you run the SQL script?")
