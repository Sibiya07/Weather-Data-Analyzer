import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

class WeatherVisualizer:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        df = pd.read_csv(self.file_path, names=["time", "temp", "humidity"])
        df['time'] = pd.to_datetime(df['time'])
        return df

    def plot_combined_graph(self):
        try:
            df = self.load_data()

            if df.empty:
                return None

            # Format time for clean UI
            df['time'] = df['time'].dt.strftime('%H:%M')

            fig, ax1 = plt.subplots(figsize=(10, 5))

            # Temperature (BAR)
            ax1.bar(df['time'], df['temp'], color='tomato', alpha=0.7)
            ax1.set_ylabel("Temperature (°C)", color='tomato')
            ax1.tick_params(axis='y', labelcolor='tomato')

            # Humidity (LINE)
            ax2 = ax1.twinx()
            ax2.plot(df['time'], df['humidity'], color='blue', marker='o', linewidth=2)
            ax2.set_ylabel("Humidity (%)", color='blue')
            ax2.tick_params(axis='y', labelcolor='blue')

            plt.xticks(rotation=30)
            plt.title("Weather Analytics Dashboard (Clean View)")
            plt.tight_layout()

            # Convert to base64
            img = io.BytesIO()
            plt.savefig(img, format='png', bbox_inches='tight')
            img.seek(0)

            encoded = base64.b64encode(img.getvalue()).decode()
            plt.close(fig)

            return encoded

        except Exception as e:
            print("Visualization error:", e)
            return None