import os
from dotenv import load_dotenv

# Detect execution environment
if os.getenv("AIRFLOW_HOME"):
    load_dotenv("/opt/project/.env.docker")
else:
    load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}