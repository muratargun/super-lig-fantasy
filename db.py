import streamlit as st
from supabase import create_client, Client

# REPLACE THESE TWO STRINGS WITH YOUR ACTUAL SUPABASE CREDENTIALS
SUPABASE_URL = "https://apclcfuuyicudfhllxlv.supabase.co/rest/v1/"# Must start with https://"
SUPABASE_KEY = "sb_publishable_LAeVM0z3u7JDtnQWGLz76g_0GUfkjhx"               # Your publishable key from Supabase

@st.cache_resource
def get_supabase() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)

supabase = get_supabase()

def fetch_players():
    response = supabase.table("players").select("*").execute()
    return response.data

def fetch_users():
    response = supabase.table("league_users").select("*").execute()
    return response.data

def add_user(friend_name: str, team_name: str):
    response = supabase.table("league_users").insert({
        "friend_name": friend_name,
        "team_name": team_name
    }).execute()
    return response.data
