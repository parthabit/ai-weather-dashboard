from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "ed9aced660679da5e4fa2fe0f67e8ddf"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather = {
                "city": city.title(),
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"],
                "description": data["weather"][0]["description"].title()
            }
        else:
            error = "City not found. Please enter a valid city name."

    return render_template("index.html", weather=weather, error=error)


if __name__ == "__main__":
    app.run(debug=True)