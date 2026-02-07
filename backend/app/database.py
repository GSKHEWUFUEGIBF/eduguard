import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
anon_key: str = os.environ.get("SUPABASE_ANON_KEY")
supabase: Client = create_client(url, anon_key)

# Example query:
# data = supabase.table('your_table').select('*').execute()
# print(data)
