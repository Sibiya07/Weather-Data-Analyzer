import csv
import os

def save_weather(row):
    os.makedirs("data", exist_ok=True)

    with open("data/weather.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)