# AcrylData Snowflake Metadata API Take Home

This is a Flask application connecting to Snowflake and retrieving metadata
- Listing Schemas
- Listing Tables for a Schema
- List Column details for a Table

## Table Of Contents 
- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
  - [Environment Variables](#environment-variables)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [GET /](#get-)
  - [GET /schemas](#get-schemas)
  - [GET /schemas/{schema_name}/tables](#get-schemasschema_nametables)
  - [GET /schemas/{schema_name}/tables/{table_name}](#get-schemasschema_nametable_name)
  - [GET /schemas/{schema_name}/tables/{table_name}/summary](#get-schemasschema_nametable_namesummary)

## Project Overview
This Flask development server enables you to interact with a Snowflake Database using 
REST APIs. It connects to a Snowflake database and exposes endpoints for retrieving 
schemas, tables, and columns metadata.

- **/app/__init__.py**: This module creates a modular Flask application with registered routes.
- **/app/config.py**: This module defines a class `Config` that retrieves our environment files. In this case, it is our Snowflake credentials to use the APIs.
- **/app/connection.py**: This module uses the `snowflake.connector` library to establish a connection to Snowflake using our credentials.
- **/app/queries.py**: This module uses the cursor object, which allows us to execute SQL statements and fetch results.
- **/app/routes.py**: This module is where we have defined our routes for the Flask application and created our endpoints.

## Getting Started

- **Python**: Ensure you have Python 3.6 or higher installed.
- **Snowflake Account**: Ensure you have the correct Snowflake account with necessary permissions to set up your environment.

## Environment Variables
- `SNOWFLAKE_USER`: Snowflake username
- `SNOWFLAKE_PASSWORD`: Snowflake password
- `SNOWFLAKE_ACCOUNT`: Snowflake account identifier
- `SNOWFLAKE_DATABASE`: Default database name
- `SNOWFLAKE_WAREHOUSE`: Default warehouse

You can set these environment variables by creating a `.env` file at the root of your project. Ensure that you add the `.env` file to your `.gitignore` file.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/OzLievano/takehome.git
   cd acrylData


## Running the Application

1. In your terminal in the root directory execute ```flask run```
2. App will run on http://127.0.0.1:5000/

## API Endpoints

GET /

Description: A welcome message with available APIs.

GET /schemas 

Description: List all Schemas in the Snowflake database.

Example Response: 
```[
  "ADOPTION",
  "ADOPTION_EVENTS",
  "ANALYTICS",
  "DATA_PLATFORM",
  "DBT_HSHETH",
  "ECOMMERCE",
  "EXTERNAL_FILES",
  "FINANCE",
  "INFORMATION_SCHEMA",
  "MARKETING",
  "PRODUCT_MANAGEMENT",
  "PUBLIC"
]```

GET /schemas/{schema_name}/tables
Description: List all tables within a Schema in the Snowflake database.
Example Response: 
```[
  "ACTUATING",
  "ADOPTIONS",
  "ADOPTION_BASED_OUTREACH",
  "ADOPTION_MATCH",
  "ARTIFICIAL_INTELLIGENCE",
  "ASYMMETRIC",
  "ASYNCHRONOUS",
  "B2B_CONTENT",
  "B2B_INITIATIVES",
  "B2C_ECOMMERCE",
  "B2C_MINDSHARE",
  "B2C_PORTALS",
  "BALANCED",
  "CIRCUIT",
  "COHERENT",
  "COMPATABILITY_MATRIX",
  "CONTINGENCY",
  "CROSS_PLATFORM",
  "CUSTOMIZABLE",
  "DIGITIZED",
  "DISCRETE",
  "DISINTERMEDIATE",
  "DOWN_SIZED",
  "ENCOMPASSING",
  "ENCRYPTION",
  "ENTERPRISE_WIDE",
  "EVEN_KEELED",
  "EXTENDED",
  "FACILITY",
  "FACILITY_SCHEDULE",
  "FOCUSED",
  "FOURTH_GENERATION",
  "FRESH_FINDS",
  "GRAPHICAL_USER_INTERFACE",
  "HOLISTIC",
  "HUMANS",
  "HUMAN_PROFILES",
  "INCREMENTAL",
  "INNOVATIVE",
  "INTEGRATED",
  "INTERFACE",
  "MISSION",
  "MONITORED",
  "MULTI_LATERAL",
  "NATIONAL",
  "NEEDS_BASED",
  "OPTIMAL",
  "PETS",
  "PET_PROFILES",
  "PORTAL",
  "PRODUCTIVITY",
  "PROFIT_FOCUSED",
  "PROJECT",
  "QUALITY_FOCUSED",
  "REALIGNED",
  "REDUCED",
  "TASKS",
  "TERTIARY",
  "TIME_FRAME",
  "UP_SIZED"
]```

GET /schemas/{schema_name}/tables/{table_name}
Description: List all column name, type and description within a table in the Snowflake database.
Example Response: 
```
[
  {
    "description": "COLUMN",
    "name": "PK",
    "type": "NUMBER(1,0)"
  }
]
```

GET /schemas/{schema_name}/tables/{table_name}/summary
Description: Provides a summary of table returning statistics in the Snowflake database.
Example Response: 
```
{
  "PK": {
    "max": 1,
    "mean": "1.000000",
    "min": 1,
    "non_null_count": 1
  }
}
```
