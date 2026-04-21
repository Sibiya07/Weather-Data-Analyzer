from flask import Flask, request
from app.services.weather_service import collect_weather
from app.services.analysis_service import analyze
from app.services.prediction_service import predict
from app.services.visualization_service import WeatherVisualizer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    temp = humidity = None
    analysis = {}
    prediction = None
    city = ""
    graph = None
    show_dashboard = False

    if request.method == "POST":
        city = request.form.get("city")

        if city:
            # Collect data
            temp, humidity = collect_weather(city)

            # Analysis + prediction
            analysis = analyze()
            prediction = predict()

            # Visualization (CLASS BASED)
            viz = WeatherVisualizer("data/weather.csv")
            graph = viz.plot_combined_graph()

            show_dashboard = True

    return f"""
    <html>
    <head>
        <title>Weather App</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #f4f6f8;
                text-align: center;
                padding-top: 50px;
            }}
            .card {{
                background: white;
                padding: 15px;
                margin: 15px auto;
                width: 400px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            }}
            input {{
                padding: 10px;
                width: 60%;
            }}
            button {{
                padding: 10px;
                background-color: #007BFF;
                color: white;
                border: none;
                cursor: pointer;
            }}
            img {{
                width: 90%;
                margin-top: 10px;
            }}
        </style>
    </head>

    <body>

        <form method="POST">
            <input type="text" name="city" placeholder="Enter city" value="{city}">
            <button type="submit">Get Weather</button>
        </form>

        {f'''
        <div class="card">
            <h3>Current Weather</h3>
            <p>Temperature: {temp}</p>
            <p>Humidity: {humidity}</p>
        </div>

        <div class="card">
            <h3>Analysis</h3>
            <p>Average Temp: {analysis.get('avg_temp')}</p>
            <p>Max Temp: {analysis.get('max_temp')}</p>
            <p>Latest Temp: {analysis.get('latest_temp')}</p>
            <p>Trend: {analysis.get('trend')}</p>
        </div>

        <div class="card">
            <h3>Prediction</h3>
            <p>Next Temperature: {prediction}</p>
        </div>

        <div class="card">
            <h3>Weather Visualization</h3>
            <img src="data:image/png;base64,{graph}">
        </div>
        ''' if show_dashboard else ""}

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)