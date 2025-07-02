import pandas as pd
import os
import mysql.connector

# Modify these based on your MySQL setup
db_config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'DSMP2',
    'port': 3306
}

# Folder containing CSV files
folder_path = "/Users/I578070/Desktop/100DaysML/Data Aanalysis/SQL/session35/drive-download-20250629T132528Z-1-001"

# Connect to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Helper: Infer SQL type from pandas dtype
def mysql_type(col):
    if pd.api.types.is_integer_dtype(col):
        return "INT"
    elif pd.api.types.is_float_dtype(col):
        return "FLOAT"
    elif pd.api.types.is_datetime64_any_dtype(col):
        return "DATE"
    else:
        return "VARCHAR(255)"

# Read and import each CSV
files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
for file in files:
    path = os.path.join(folder_path, file)
    table_name = os.path.splitext(file)[0]
    df = pd.read_csv(path)

    # Attempt to parse datetime columns
    for col in df.columns:
        try:
            df[col] = pd.to_datetime(df[col], format='%d-%m-%Y')
        except Exception:
            pass

    df = df.where(pd.notnull(df), None)  # Replace NaN with None

    # Step 1: Create Table if not exists
    column_defs = ", ".join([f"`{col}` {mysql_type(df[col])}" for col in df.columns])
    create_query = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({column_defs});"
    cursor.execute(create_query)

    # Step 2: Insert data
    columns = ", ".join([f"`{col}`" for col in df.columns])
    placeholders = ", ".join(["%s"] * len(df.columns))
    insert_query = f"INSERT INTO `{table_name}` ({columns}) VALUES ({placeholders})"

    for row in df.itertuples(index=False, name=None):
        try:
            cursor.execute(insert_query, row)
        except Exception as e:
            print(f"❌ Failed to insert row in `{table_name}`: {row}")
            print(f"   Error: {e}")

    print(f"✅ Imported {file} into `{table_name}`")

# Commit and close connection
conn.commit()
cursor.close()
conn.close()

print("✅ All CSVs successfully imported into MySQL.")
