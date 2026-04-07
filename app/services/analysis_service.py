import pandas as pd

def analyze():
    try:
        df = pd.read_csv("data/weather.csv", names=["time", "temp", "humidity"])


        if df.empty:
            return {"error": "No data available"}

        avg_temp = df['temp'].mean()
        max_temp = df['temp'].max()
        latest_temp = df['temp'].iloc[-1]

      
        if len(df) > 1:
            trend = "Increasing " if df['temp'].iloc[-1] > df['temp'].iloc[0] else "Decreasing"
        else:
            trend = "Not enough data"

        return {
            "avg_temp": float(round(avg_temp, 2)),
            "max_temp": float(max_temp),
            "latest_temp": float(latest_temp),
            "trend": trend.strip()
        }

    except Exception as e:
        return {"error": str(e)}