import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

def plot_graphs():
    try:
        df = pd.read_csv("data/weather.csv", names=["time", "temp", "humidity"])

        if df.empty:
            print("No data to display")
            return

        df['time'] = pd.to_datetime(df['time'])

  
        plt.figure()
        plt.plot(df['time'], df['temp'])
        plt.title("Temperature Trend")
        plt.xlabel("Time")
        plt.ylabel("Temperature (°C)")
        plt.xticks(rotation=45)
        plt.tight_layout()

        if len(df) > 1:
            trend = "Increasing" if df['temp'].iloc[-1] > df['temp'].iloc[0] else "Decreasing"
            plt.figtext(0.15, 0.85, f"Trend: {trend}", fontsize=10)

        plt.show()

        # -------- Humidity Graph --------
        plt.figure()
        plt.plot(df['time'], df['humidity'])
        plt.title("Humidity Trend")
        plt.xlabel("Time")
        plt.ylabel("Humidity (%)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("Error in visualization:", e)


def get_graphs():
    try:
        df = pd.read_csv("data/weather.csv", names=["time", "temp", "humidity"])

        if df.empty:
            return None, None

        df['time'] = pd.to_datetime(df['time'])

    
        plt.figure()
        plt.plot(df['time'], df['temp'])
        plt.title("Temperature Trend")
        plt.xlabel("Time")
        plt.ylabel("Temperature (°C)")
        plt.xticks(rotation=45)
        plt.tight_layout()

        temp_img = io.BytesIO()
        plt.savefig(temp_img, format='png')
        temp_img.seek(0)
        temp_graph = base64.b64encode(temp_img.getvalue()).decode()
        plt.close()

        # -------- Humidity Graph --------
        plt.figure()
        plt.plot(df['time'], df['humidity'])
        plt.title("Humidity Trend")
        plt.xlabel("Time")
        plt.ylabel("Humidity (%)")
        plt.xticks(rotation=45)
        plt.tight_layout()

        hum_img = io.BytesIO()
        plt.savefig(hum_img, format='png')
        hum_img.seek(0)
        hum_graph = base64.b64encode(hum_img.getvalue()).decode()
        plt.close()

        return temp_graph, hum_graph

    except Exception as e:
        print("Error in visualization:", e)
        return None, None