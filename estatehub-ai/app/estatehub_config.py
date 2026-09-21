import os
from dotenv import load_dotenv
load_dotenv()
MOCK_MODE=os.getenv("MOCK_MODE","true").lower()=="true"
DATABASE_URL=os.getenv("DATABASE_URL","sqlite:///./estatehub.db")
SUPABASE_URL=os.getenv("SUPABASE_URL","")
SUPABASE_ANON_KEY=os.getenv("SUPABASE_ANON_KEY","")
APP_NAME=os.getenv("APP_NAME","EstateHub AI")
