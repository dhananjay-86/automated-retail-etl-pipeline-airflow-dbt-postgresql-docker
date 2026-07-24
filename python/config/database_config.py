from dotenv import load_dotenv  #Imports the function that reads the .env file.
import os        #Python's built-in module for working with environment variables.

# Load environment variables from .env
load_dotenv()    # reads .env

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}