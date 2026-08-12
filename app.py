import streamlit as st

st.set_page_config(page_title="Friends Fantasy League", page_icon="⚽", layout="centered")

# Custom styling for the mobile app feel
st.markdown("""
<style>
.player-card { background-color: #1f2937; color: white; padding: 10px; border-radius: 8px; text-align: center; margin-bottom: 8px; font-size: 14px;}
.stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("⚽ Friends League")

# Mock Database of Players
PLAYERS = [
    {"name": "Victor Osimhen", "club": "Galatassaray", "position": "FWD"},
    {"name": "Mauro Icardi", "club": "Galatassaray", "position": "FWD"},
    {"name": "Ciro Immobile", "club": "Besıktas", "position": "FWD"},
    {"name": "Rafa Silva", "club": "Besıktas", "position": "MID"},
    {"name": "Gedson Fernandes", "club": "Besıktas", "position": "MID"},
    {"name": "Fred", "club": "Fenerbahce", "position": "MID"},
    {"name": "Talisca", "club": "Fenerbahce", "position": "MID"},
    {"name": "Lucas Torreira", "club": "Galatassaray", "position": "MID"},
    {"name": "Eren Elmalı", "club": "Trabzonspor", "position": "DEF"},
    {"name": "Davinson Sanchez", "club": "Galatassaray", "position": "DEF"},
    {"name": "Mert Günok", "club": "Besıktas", "position": "GK"},
    {"name": "Uğurcan Çakır", "club": "Trabzonspor", "position": "GK"}
]

# Initialize temporary memory (Session State) to hold your selected squad
if 'my_squad' not in st.session_state:
    st.session_state['my_squad'] = []

tab1, tab2, tab3 = st.tabs(["🛒 Market", "📋 Pitch", "⚔️ Matchup"])

with tab1:
    st.subheader("Sign Players")
    st.write("Tap 'Add' to sign a player to your squad.")
    
    for player in PLAYERS:
        col1, col2, col3 = st.columns([3, 2, 2])
        col1.write(f"**{player['name']}**")
        col2.write(f"*{player['club']}*")
        
        # Check if player is already in the squad
        in_squad = any(p['name'] == player['name'] for p in st.session_state['my_squad'])
        
        if in_squad:
            if col3.button("Drop", key=f"drop_{player['name']}"):
                st.session_state['my_squad'] = [p for p in st.session_state['my_squad'] if p['name'] != player['name']]
                st.rerun()
        else:
            if col3.button("Add", key=f"add_{player['name']}", type="primary"):
                if len(st.session_state['my_squad']) < 11:
                    st.session_state['my_squad'].append(player)
                    st.rerun()
                else:
                    st.error("Squad full! Drop a player first.")
                    
    st.info(f"Squad Size: {len(st.session_state['my_squad'])} / 11")

with tab2:
    st.subheader("Your Starting 11")
    if len(st.session_state['my_squad']) == 0:
        st.warning("Your pitch is empty. Go to the Market tab to sign players.")
    else:
        # Sort players by position to draw the pitch correctly
        forwards = [p for p in st.session_state['my_squad'] if p['position'] == 'FWD']
        mids = [p for p in st.session_state['my_squad'] if p['position'] == 'MID']
        defs = [p for p in st.session_state['my_squad'] if p['position'] == 'DEF']
        gks = [p for p in st.session_state['my_squad'] if p['position'] == 'GK']

        st.caption("FORWARDS")
        cols = st.columns(len(forwards) if forwards else 1)
        for i, p in enumerate(forwards):
            cols[i].markdown(f'<div class="player-card"><b>{p["name"]}</b><br>{p["club"]}</div>', unsafe_allow_html=True)

        st.caption("MIDFIELDERS")
        cols = st.columns(len(mids) if mids else 1)
        for i, p in enumerate(mids):
            cols[i].markdown(f'<div class="player-card"><b>{p["name"]}</b><br>{p["club"]}</div>', unsafe_allow_html=True)
            
        st.caption("DEFENDERS")
        cols = st.columns(len(defs) if defs else 1)
        for i, p in enumerate(defs):
            cols[i].markdown(f'<div class="player-card"><b>{p["name"]}</b><br>{p["club"]}</div>', unsafe_allow_html=True)
            
        st.caption("GOALKEEPER")
        cols = st.columns(len(gks) if gks else 1)
        for i, p in enumerate(gks):
            cols[i].markdown(f'<div class="player-card"><b>{p["name"]}</b><br>{p["club"]}</div>', unsafe_allow_html=True)

with tab3:
    st.subheader("Gameweek 1: You vs. Ahmet")
    
    # Calculate fake dynamic points based on squad size just to test interactivity
    my_points = len(st.session_state['my_squad']) * 6
    
    c1, c2, c3 = st.columns([2, 1, 2])
    c1.metric("Your Points", my_points)
    c2.write("### VS")
    c3.metric("Ahmet", "42")
    
    st.divider()
    st.subheader("League Table")
    st.table({
        "Rank": [1, 2, 3],
        "Manager": ["You", "Ahmet", "Mehmet"], 
        "Points": [my_points, 42, 15]
    })
