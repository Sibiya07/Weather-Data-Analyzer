from app.services.weather_service import collect_weather
from app.services.visualization_service import plot_graphs
from app.services.analysis_service import analyze
from app.services.prediction_service import predict

city = input("Enter city name: ")

temp, humidity = collect_weather(city)

print("\n--- Current Weather ---")
print("Temperature:", temp)
print("Humidity:", humidity)


analysis = analyze()

print("\n--- Analysis ---")
print(f"Average Temperature : {analysis['avg_temp']} °C")
print(f"Max Temperature     : {analysis['max_temp']} °C")
print(f"Latest Temperature  : {analysis['latest_temp']} °C")
print(f"Trend               : {analysis['trend']}")

print("\n--- Prediction ---")
print("Next Temp:", predict())

plot_graphs()