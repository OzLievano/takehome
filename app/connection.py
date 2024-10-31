import snowflake.connector 
from app.config import Config
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def connect_to_snowflake():
    try:
        ctx = snowflake.connector.connect(
            user=Config.SNOWFLAKE_USER,
            password=Config.SNOWFLAKE_PASSWORD,
            account=Config.SNOWFLAKE_ACCOUNT,
            database=Config.SNOWFLAKE_DATABASE,
            warehouse=Config.SNOWFLAKE_WAREHOUSE,
        )
        logging.info("Successfully connected to Snowflake.")
        return ctx
    except Exception as e:
        logging.error(f"Error connecting to Snowflake: {e}")
        return None
