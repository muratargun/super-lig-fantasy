import streamlit as st
from supabase import create_client, Client

SUPABASE_URL = "https://apclcfuuyicudfhllxlv.supabase.co"
SUPABASE_KEY = "sb_publishable_LAeVM0z3u7JDtnQWGLz76g_0GUfkjhx"

# We removed @st.cache_resource here so Streamlit is forced to use the new URL
def get_supabase() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)

supabase = get_supabase()

def fetch_players():
    try:
        response = supabase.table("players").select("*").execute()
        return response.data
    except Exception as e:
        st.error(f"Error loading players: {e}")
        return []

def fetch_users():
    try:
        response = supabase.table("league_users").select("*").execute()
        return response.data
    except Exception as e:
        st.error(f"Error loading managers: {e}")
        return []

def add_user(friend_name: str, team_name: str):
    try:
        response = supabase.table("league_users").insert({
            "friend_name": friend_name,
            "team_name": team_name
        }).execute()
        return response.data
    except Exception as e:
        st.error(f"Error adding manager: {e}")
        return None
