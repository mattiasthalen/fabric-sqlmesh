import os
from sqlmesh.core.config import (
    Config,
    ModelDefaultsConfig,
    GatewayConfig,
    MSSQLConnectionConfig
)
from dotenv import load_dotenv

load_dotenv(override=True)

# Create gateway config for MSSQL
mssql_gateway = GatewayConfig(
    connection=MSSQLConnectionConfig(
        host=os.environ.get("fabric__host"),
        user=os.environ.get("fabric__client_id"),
        password=os.environ.get("fabric__client_secret"),
        database=os.environ.get("fabric__database"),
        driver="pyodbc",
        driver_name="ODBC Driver 18 for SQL Server",
        odbc_properties={
            "authentication": "ActiveDirectoryServicePrincipal"
        }
    )
)

# Set model defaults
model_defaults = ModelDefaultsConfig(
    dialect="duckdb",
    start="2025-05-09"
)

# Create the main config
config = Config(
    gateways={"mssql": mssql_gateway},
    default_gateway="mssql",
    model_defaults=model_defaults
)