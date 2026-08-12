import streamlit as st

st.set_page_config(page_title="Süper Lig Fantasy", page_icon="⚽", layout="centered")

# Custom styling for mobile cards
st.markdown("""

""", unsafe_allow_html=True)

st.title("⚽ Our Private League")

tab1, tab2, tab3 = st.tabs(["📋 My Team", "⚔️ Matchup", "🏆 Table"])

with tab1:
    st.subheader("Your Starting 11")
    
    st.caption("FORWARDS")
    col1, col2 = st.columns(2)
    with col1: st.markdown('OsimhenGalatassaray (C)', unsafe_allow_html=True)
    with col2: st.markdown('ImmobileBesıktas', unsafe_allow_html=True)
    
    st.caption("MIDFIELDERS")
    col3, col4, col5 = st.columns(3)
    with col3: st.markdown('Rafa SilvaBesıktas', unsafe_allow_html=True)
    with col4: st.markdown('TorreiraGalatassaray', unsafe_allow_html=True)
    with col5: st.markdown('FredFenerbahce', unsafe_allow_html=True)
    
    if st.button("Save Lineup 🚀"):
        st.success("Lineup saved! (This is just a visual test for now)")

with tab2:
    st.subheader("Gameweek 1: You vs. Ahmet")
    c1, c2, c3 = st.columns([2, 1, 2])
    c1.metric("Your Points", "54")
    c2.write("### VS")
    c3.metric("Ahmet", "48")

with tab3:
    st.subheader("League Table")
    st.table({"Manager": ["You", "Ahmet", "Mehmet"], "Points": [15, 12, 9]})
