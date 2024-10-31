import snowflake.connector
from flask import current_app
import logging
import os;
# Configure logging
logging.basicConfig(level=logging.INFO)

def get_schemas(ctx):
    """Retrieve the list of schemas in the configured database."""
    try:
        with ctx.cursor() as cursor:
            cursor.execute(f"SHOW SCHEMAS IN DATABASE {os.getenv('SNOWFLAKE_DATABASE')};")
            schemas = cursor.fetchall()
            return [schema[1] for schema in schemas]  # Schema name is in the second column (index 1)
    except Exception as e:
        logging.error(f"Error retrieving schemas: {e}")
        return []

def get_tables_in_schema(ctx, schema_name):
    """Retrieve the list of tables in a specified schema."""
    try:
        with ctx.cursor() as cursor:
            cursor.execute(f"SHOW TABLES IN SCHEMA {os.getenv('SNOWFLAKE_DATABASE')}.{schema_name};")
            tables = cursor.fetchall()
            return [table[1] for table in tables]  # Table name is in the second column (index 1)
    except Exception as e:
        logging.error(f"Error retrieving tables for schema {schema_name}: {e}")
        return []

def get_columns_in_table(ctx, schema_name, table_name):
    """Retrieve the list of columns in a specified table."""
    try:
        with ctx.cursor() as cursor:
            cursor.execute(f"DESC TABLE {os.getenv('SNOWFLAKE_DATABASE')}.{schema_name}.{table_name};")
            columns = cursor.fetchall()
            return [
                {
                    "name": column[0],  # Column name
                    "type": column[1],  # Column type
                    "description": column[2] if len(column) > 2 else 'N/A'  # Column description if available
                }
                for column in columns
            ]
    except Exception as e:
        logging.error(f"Error retrieving columns for table {table_name}: {e}")
        return []

def get_table_summary(ctx, schema_name, table_name):
    """Retrieve summary statistics for the specified table."""
    try:
        with ctx.cursor() as cursor:
            cursor.execute(f"DESC TABLE {os.getenv('SNOWFLAKE_DATABASE')}.{schema_name}.{table_name};")
            columns_info = cursor.fetchall()

            numeric_columns = []
            non_numeric_columns = []

            for column in columns_info:
                column_name = column[0]  # Column name
                column_type = column[1]  # Column type
                if "NUMBER" in column_type or "FLOAT" in column_type or "INT" in column_type:
                    numeric_columns.append(column_name)
                else:
                    non_numeric_columns.append(column_name)

            # Prepare the SQL for summary statistics
            sql_parts = []
            for col in numeric_columns:
                sql_parts.append(
                    f"COUNT({col}) AS {col}_non_null_count, "
                    f"AVG({col}) AS {col}_mean, "
                    f"MIN({col}) AS {col}_min, "
                    f"MAX({col}) AS {col}_max"
                )
            for col in non_numeric_columns:
                sql_parts.append(
                    f"COUNT({col}) AS {col}_non_null_count, "
                    f"COUNT(DISTINCT {col}) AS {col}_unique_count"
                )

            summary_sql = f"SELECT {', '.join(sql_parts)} FROM {os.getenv('SNOWFLAKE_DATABASE')}.{schema_name}.{table_name};"
            cursor.execute(summary_sql)
            summary_stats = cursor.fetchone()

            # Prepare the summary statistics in a readable format
            summary = {}
            for i, column in enumerate(columns_info):
                column_name = column[0]
                if column_name in numeric_columns:
                    summary[column_name] = {
                        "non_null_count": summary_stats[i * 4],
                        "mean": summary_stats[i * 4 + 1],
                        "min": summary_stats[i * 4 + 2],
                        "max": summary_stats[i * 4 + 3]
                    }
                else:
                    summary[column_name] = {
                        "non_null_count": summary_stats[i * 2],
                        "unique_count": summary_stats[i * 2 + 1]
                    }
            
            return summary
    except Exception as e:
        logging.error(f"Error retrieving summary for table {table_name}: {e}")
        return {}
