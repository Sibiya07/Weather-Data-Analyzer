import pandas as pd
import numpy as np

def analyze():
    try:
        df = pd.read_csv("data/weather.csv", names=["time", "temp", "humidity"])

        if df.empty:
            return {"error": "No data available"}

        # Clean data
        df = df.dropna()

        avg_temp = df['temp'].mean()
        max_temp = df['temp'].max()
        min_temp = df['temp'].min()
        latest_temp = df['temp'].iloc[-1]

        # Better trend using linear slope
        x = np.arange(len(df))
        slope = np.polyfit(x, df['temp'], 1)[0]

        if slope > 0:
            trend = "Increasing"
        elif slope < 0:
            trend = "Decreasing"
        else:
            trend = "Stable"

        return {
            "avg_temp": round(avg_temp, 2),
            "max_temp": float(max_temp),
            "min_temp": float(min_temp),
            "latest_temp": float(latest_temp),
            "trend": trend
        }

    except Exception as e:
        return {"error": str(e)}