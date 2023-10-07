import os
from dotenv import load_dotenv

load_dotenv()

# Access environment variables
DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
DATABASE=os.getenv('DATABASE')
DB_USER=os.getenv('DB_USER')
DB_USER_PASSWORD=os.getenv('DB_USER_PASSWORD')
DB_HOST=os.getenv('DB_HOST')
DB_PORT=os.getenv('DB_PORT')