from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def predict():
    try:
        df = pd.read_csv("data/weather.csv", names=["time", "temp", "humidity"])

        if len(df) < 2:
            return "Not enough data for prediction"

        # Convert time properly (optional improvement)
        df['time'] = pd.to_datetime(df['time'])
        df['time_index'] = np.arange(len(df))

        X = df[['time_index']]
        y = df['temp']

        model = LinearRegression()
        model.fit(X, y)

        next_index = np.array([[len(df)]])
        prediction = model.predict(next_index)[0]

        return round(prediction, 2)

    except Exception as e:
        return f"Error: {e}"