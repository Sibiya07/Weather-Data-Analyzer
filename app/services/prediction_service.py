from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def predict():
    try:
        df = pd.read_csv("data/weather.csv", names=["time", "temp", "humidity"])

    
        if len(df) < 2:
            return "Not enough data for prediction"

        X = np.array(range(len(df))).reshape(-1,1)
        y = df['temp']

        model = LinearRegression()
        model.fit(X, y)

        next_value = model.predict([[len(df)]])[0]

        return round(next_value, 2)

    except Exception as e:
        return f"Error: {e}"