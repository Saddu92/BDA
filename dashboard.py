import pandas as pd
import sqlite3
import plotly.express as px
from dash import Dash, dcc, html

# Connect to SQLite and load data
conn = sqlite3.connect("water_quality.db")
df = pd.read_sql("SELECT * FROM water_readings", conn)
conn.close()

df['measurement_time'] = pd.to_datetime(df['measurement_time'])

# Convert is_anomaly to string for color grouping
df['is_anomaly'] = df['is_anomaly'].astype(str)

app = Dash(__name__)

# Line chart: color by anomaly
fig = px.line(
    df,
    x="measurement_time",
    y="value",
    color="is_anomaly",  # categorical: "0" or "1"
    title="Water Quality Over Time"
)

app.layout = html.Div([
    html.H1("Water Quality Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    # Use the new method
    app.run(debug=True)
