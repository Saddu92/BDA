# ingest_sqlite.py
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import numpy as np

# Load CSV (download from Kaggle or use sample file)
df = pd.read_csv("water_potability.csv")

# Add extra columns
df["measurement_time"] = [datetime.now() - timedelta(hours=i) for i in range(len(df))]
df["sensor_id"] = "SENSOR_001"
df["parameter"] = "WaterQuality"
df["unit"] = "mg/L"
df["latitude"] = np.random.uniform(45.0, 47.0, len(df))
df["longitude"] = np.random.uniform(10.0, 12.0, len(df))

# Keep only needed columns & rename
df = df.rename(columns={"Hardness":"value"})[["measurement_time","sensor_id","parameter","value","unit","latitude","longitude"]]


# Connect SQLite & insert
conn = sqlite3.connect("water_quality.db")
df.to_sql("water_readings", conn, if_exists="append", index=False)
conn.close()
print("✅ Data uploaded to SQLite database.")
