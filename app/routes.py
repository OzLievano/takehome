from flask import Blueprint, jsonify
from app.connection import connect_to_snowflake
from app.queries import get_schemas, get_tables_in_schema, get_columns_in_table, get_table_summary

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the FLASK Acryl Take-Home: Snowflake Metadata API",
        "methods": [
            {"method": "GET", "endpoint": "/schemas", "description": "Retrieve all schemas"},
            {"method": "GET", "endpoint": "/schemas/{schema_name}/tables", "description": "Retrieve all tables in a schema"},
            {"method": "GET", "endpoint": "/schemas/{schema_name}/tables/{table_name}", "description": "Retrieve columns for a specific table"},
            {"method": "GET", "endpoint": "/schemas/{schema_name}/tables/{table_name}/summary", "description": "Retrieve table statistic summary"},
        ]
    })

@bp.route('/schemas', methods=['GET'])
def schemas():
    ctx = connect_to_snowflake()
    if ctx:
        schemas_list = get_schemas(ctx)
        ctx.close()
        return jsonify(schemas_list), 200
    return jsonify({"error": "Failed to connect to Snowflake."}), 500

@bp.route('/schemas/<schema_name>/tables', methods=['GET'])
def tables_in_schema(schema_name):
    ctx = connect_to_snowflake()
    if ctx:
        tables = get_tables_in_schema(ctx, schema_name)
        ctx.close()
        return jsonify(tables), 200
    return jsonify({"error": "Failed to connect to Snowflake."}), 500

@bp.route('/schemas/<schema_name>/tables/<table_name>', methods=['GET'])
def columns_in_table(schema_name, table_name):
    ctx = connect_to_snowflake()
    if ctx:
        columns = get_columns_in_table(ctx, schema_name, table_name)
        ctx.close()
        return jsonify(columns), 200
    return jsonify({"error": "Failed to connect to Snowflake."}), 500

@bp.route('/schemas/<schema_name>/tables/<table_name>/summary', methods=['GET'])
def table_summary(schema_name, table_name):
    ctx = connect_to_snowflake()
    if ctx:
        summary = get_table_summary(ctx, schema_name, table_name)
        ctx.close()
        return jsonify(summary), 200
    return jsonify({"error": "Failed to connect to Snowflake."}), 500
