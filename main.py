from flask import Flask, request
from app.services.weather_service import collect_weather
from app.services.analysis_service import analyze
from app.services.prediction_service import predict
from app.services.visualization_service import get_graphs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    temp = humidity = None
    analysis = {}
    prediction = None
    city = ""
    temp_graph = hum_graph = None

    if request.method == "POST":
        city = request.form.get("city")

        if city:
            temp, humidity = collect_weather(city)
            analysis = analyze()
            prediction = predict()
            temp_graph, hum_graph = get_graphs()

    return f"""
    <html>
    <head>
        <title>Weather Dashboard</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #f4f6f8;
                text-align: center;
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
                width: 80%;
                margin-top: 10px;
            }}
        </style>
    </head>

    <body>

        <h1>🌦️ Weather Dashboard</h1>

        <form method="POST">
            <input type="text" name="city" placeholder="Enter city" value="{city}">
            <button type="submit">Get Weather</button>
        </form>

        <div class="card">
            <h3>Current Weather</h3>
            <p>Temperature: {temp if temp else '-'}</p>
            <p>Humidity: {humidity if humidity else '-'}</p>
        </div>

        <div class="card">
            <h3>Analysis</h3>
            <p>Average Temp: {analysis.get('avg_temp', '-')}</p>
            <p>Max Temp: {analysis.get('max_temp', '-')}</p>
            <p>Latest Temp: {analysis.get('latest_temp', '-')}</p>
            <p>Trend: {analysis.get('trend', '-')}</p>
        </div>

        <div class="card">
            <h3>Prediction</h3>
            <p>Next Temperature: {prediction if prediction else '-'}</p>
        </div>

        <div class="card">
            <h3>Temperature Graph</h3>
            {f'<img src="data:image/png;base64,{temp_graph}"/>' if temp_graph else '<p>No data</p>'}
        </div>

        <div class="card">
            <h3>Humidity Graph</h3>
            {f'<img src="data:image/png;base64,{hum_graph}"/>' if hum_graph else '<p>No data</p>'}
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)