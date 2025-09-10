import os
import psycopg2
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

if not DATABASE_URL:
    print("DATABASE_URL not found in environment")
    exit(1)

result = urlparse(DATABASE_URL)

print(f"Connecting to database: {result.hostname}")

try:
    conn = psycopg2.connect(
        dbname=result.path[1:],
        user=result.username,
        password=result.password,
        host=result.hostname,
        port=result.port
    )

    cursor = conn.cursor()

    # Delete ALL socialaccount migrations
    print("Deleting ALL socialaccount migrations...")
    cursor.execute("DELETE FROM django_migrations WHERE app='socialaccount'")
    
    # Also check if we need to delete sites migrations
    cursor.execute("SELECT app, name FROM django_migrations WHERE app='sites'")
    sites_migrations = cursor.fetchall()
    print(f"Sites migrations found: {sites_migrations}")
    
    if not sites_migrations:
        print("No sites migrations found, this might cause issues...")
    
    # Commit the changes
    conn.commit()
    
    print("All socialaccount migrations deleted!")
    
    # Close connection
    cursor.close()
    conn.close()

except Exception as e:
    print(f"Error: {e}")
