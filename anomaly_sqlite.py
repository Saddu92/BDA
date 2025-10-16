# anomaly_sqlite.py
import pandas as pd
import sqlite3
from sklearn.ensemble import IsolationForest

conn = sqlite3.connect("water_quality.db")
df = pd.read_sql("SELECT * FROM water_readings", conn)

# Anomaly detection
model = IsolationForest(contamination=0.05, random_state=42)
df["is_anomaly"] = (model.fit_predict(df[["value"]]) == -1).astype(int)
df["anomaly_score"] = -model.decision_function(df[["value"]])

# Update DB
for i, row in df.iterrows():
    conn.execute(
        "UPDATE water_readings SET is_anomaly=?, anomaly_score=? WHERE id=?",
        (int(row.is_anomaly), float(row.anomaly_score), int(row.id))
    )

conn.commit()
conn.close()
print("✅ Anomalies updated in SQLite database.")
