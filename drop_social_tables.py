import psycopg2
import os
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()

# Get your DATABASE_URL from environment
db_url = os.getenv('DATABASE_URL')
parsed = urlparse(db_url)

try:
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        dbname=parsed.path[1:], 
        user=parsed.username, 
        password=parsed.password, 
        host=parsed.hostname, 
        port=parsed.port
    )
    cursor = conn.cursor()

    print("🗑️ Dropping problematic socialaccount tables...")
    
    # Drop the problematic tables
    cursor.execute('DROP TABLE IF EXISTS socialaccount_socialapp CASCADE;')
    cursor.execute('DROP TABLE IF EXISTS socialaccount_socialapp_sites CASCADE;')
    cursor.execute('DROP TABLE IF EXISTS socialaccount_socialaccount CASCADE;')
    cursor.execute('DROP TABLE IF EXISTS socialaccount_socialtoken CASCADE;')
    
    # Also clear migration records for socialaccount
    cursor.execute("DELETE FROM django_migrations WHERE app='socialaccount';")
    
    conn.commit()
    print("✅ Successfully dropped socialaccount tables and cleared migration history")
    
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

print("\n🔄 Now run: python manage.py migrate")
