# End-to-End Snowflake & dbt Data Pipeline

A complete data engineering pipeline built using Docker, Apache Airflow, dbt, Snowflake, and Streamlit.

## Architecture

1. **Ingestion & Raw Layer**: Raw order data stored in Snowflake `RAW` schema.
2. **Transformation Layer (dbt)**:
   - `Staging`: Cleaning and casting raw data types.
   - `Intermediate`: Aggregating customer order metrics.
   - `Marts`: Dimension and Fact tables (`FCT_ORDERS`) for reporting.
3. **Orchestration**: Apache Airflow DAG managing automated `dbt run` and `dbt test`.
4. **Data Visualization**: Interactive Streamlit Dashboard connected directly to Snowflake.

## How to Run from Scratch

1. **Prerequisites**: Docker Desktop and Git installed.
2. **Setup Credentials**: Update `dbt_project/profiles.yml` and `streamlit_app/.streamlit/secrets.toml` with your Snowflake credentials.
3. **Start Services**:
   ```bash
   docker compose up -d --build
