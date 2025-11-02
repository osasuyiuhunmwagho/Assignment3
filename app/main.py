import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

 # Load my credentials from .env
load_dotenv()  


def get_connection():
    return psycopg2.connect(
        host=os.getenv("PGHOST"),
        port=os.getenv("PGPORT"),
        database=os.getenv("PGDATABASE"),
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD")
    )

if __name__ == "__main__" :
        try:
            conn = get_connection()
            print("LETS GOOOO✅ Successfully connected to the database!")


            # Closing the connection
            conn.close()
            print("Connection closed.")


        except psycopg2.Error as e:
            print(f"❌ Error connecting to database: {e}")