import os
import psycopg2
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()

# Get DATABASE_URL from your environment
DATABASE_URL = os.getenv('DATABASE_URL')

if not DATABASE_URL:
    print("DATABASE_URL not found in environment")
    exit(1)

result = urlparse(DATABASE_URL)

print(f"Connecting to database: {result.hostname}")

try:
    # Connection parameters
    conn = psycopg2.connect(
        dbname=result.path[1:],
        user=result.username,
        password=result.password,
        host=result.hostname,
        port=result.port
    )

    cursor = conn.cursor()

    # Check current problematic migrations
    print("Checking current migrations...")
    cursor.execute("SELECT app, name FROM django_migrations WHERE app IN ('sites', 'socialaccount') ORDER BY applied")
    migrations = cursor.fetchall()
    
    for migration in migrations:
        print(f"Found: {migration[0]}.{migration[1]}")

    # Delete the problematic migration
    print("Deleting problematic socialaccount migration...")
    cursor.execute("DELETE FROM django_migrations WHERE app='socialaccount' AND name='0001_initial'")
    
    # Commit the changes
    conn.commit()
    
    print("Migration conflict fixed!")
    
    # Close connection
    cursor.close()
    conn.close()

except Exception as e:
    print(f"Error: {e}")
