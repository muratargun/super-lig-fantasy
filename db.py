import streamlit as st
from supabase import create_client, Client

# Initialize Supabase client using secrets or direct strings
@st.cache_resource
def init_supabase() -> Client:
    # Replace these strings with your actual Supabase URL and Anon Key
    url = st.secrets.get("SUPABASE_URL", "YOUR_SUPABASE_URL_HERE")
    key = st.secrets.get("SUPABASE_KEY", "YOUR_SUPABASE_KEY_HERE")
    return create_client(url, key)

supabase = init_supabase()

def get_all_players():
    response = supabase.table("players").select("*").execute()
    return response.data

def get_users():
    response = supabase.table("users").select("*").execute()
    return response.data
