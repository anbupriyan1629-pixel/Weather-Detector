import os
from flask import Flask, render_template, request

app = Flask(
    __name__,
    template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "templates")),
    static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static"))
)

weather_data = {
    "Ariyalur": {"temp": 34, "desc": "Sunny", "humidity": 55},
    "Chengalpattu": {"temp": 33, "desc": "Humid", "humidity": 72},
    "Chennai": {"temp": 36, "desc": "Rainy", "humidity": 78},
    "Coimbatore": {"temp": 30, "desc": "Pleasant", "humidity": 60},
    "Cuddalore": {"temp": 32, "desc": "Warm", "humidity": 70},
    "Dharmapuri": {"temp": 28, "desc": "Cloudy", "humidity": 60},
    "Dindigul": {"temp": 31, "desc": "Hot", "humidity": 56},
    "Erode": {"temp": 29, "desc": "Dry", "humidity": 52},
    "Kallakurichi": {"temp": 30, "desc": "Warm", "humidity": 63},
    "Kancheepuram": {"temp": 33, "desc": "Sunny", "humidity": 69},
    "Kanniyakumari": {"temp": 29, "desc": "Coastal", "humidity": 74},
    "Karur": {"temp": 32, "desc": "Clear", "humidity": 58},
    "Krishnagiri": {"temp": 27, "desc": "Cool", "humidity": 62},
    "Madurai": {"temp": 35, "desc": "Hot", "humidity": 45},
    "Mayiladuthurai": {"temp": 31, "desc": "Humid", "humidity": 74},
    "Nagapattinam": {"temp": 29, "desc": "Breezy", "humidity": 80},
    "Namakkal": {"temp": 30, "desc": "Sunny", "humidity": 60},
    "Nilgiris": {"temp": 20, "desc": "Cool", "humidity": 82},
    "Perambalur": {"temp": 33, "desc": "Warm", "humidity": 58},
    "Pudukkottai": {"temp": 32, "desc": "Sunny", "humidity": 57},
    "Ramanathapuram": {"temp": 34, "desc": "Hot", "humidity": 68},
    "Ranipet": {"temp": 31, "desc": "Clear", "humidity": 61},
    "Salem": {"temp": 32, "desc": "Hot", "humidity": 50},
    "Sivaganga": {"temp": 33, "desc": "Humid", "humidity": 67},
    "Tenkasi": {"temp": 24, "desc": "Windy", "humidity": 70},
    "Thanjavur": {"temp": 32, "desc": "Warm", "humidity": 62},
    "Theni": {"temp": 28, "desc": "Pleasant", "humidity": 64},
    "Thoothukudi": {"temp": 33, "desc": "Coastal Breeze", "humidity": 75},
    "Tiruchirappalli": {"temp": 31, "desc": "Clear", "humidity": 59},
    "Tirunelveli": {"temp": 30, "desc": "Warm", "humidity": 66},
    "Tirupattur": {"temp": 26, "desc": "Cool", "humidity": 63},
    "Tiruppur": {"temp": 29, "desc": "Mild", "humidity": 60},
    "Tiruvallur": {"temp": 34, "desc": "Sunny", "humidity": 73},
    "Tiruvarur": {"temp": 31, "desc": "Humid", "humidity": 78},
    "Tiruvannamalai": {"temp": 28, "desc": "Cloudy", "humidity": 61},
    "Vellore": {"temp": 30, "desc": "Warm", "humidity": 64},
    "Villupuram": {"temp": 32, "desc": "Sunny", "humidity": 66},
    "Virudhunagar": {"temp": 33, "desc": "Hot", "humidity": 55}
}

districts = sorted(weather_data.keys())

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
        if city in weather_data:
            data = weather_data[city]
            return render_template("result.html",
                                   city=city,
                                   temp=data["temp"],
                                   desc=data["desc"],
                                   humidity=data["humidity"])
    return render_template("index.html", districts=districts)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
