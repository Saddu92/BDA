import sqlite3

conn = sqlite3.connect("water_quality.db")  # <- updated
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS water_readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    measurement_time TEXT,
    sensor_id TEXT,
    parameter TEXT,
    value REAL,
    unit TEXT,
    latitude REAL,
    longitude REAL,
    is_anomaly INTEGER DEFAULT 0,
    anomaly_score REAL
)
""")

conn.commit()
conn.close()
print("✅ SQLite database created with table 'water_readings'.")
