import requests
from flask import Flask, request, render_template

app = Flask(__name__)

def get_calories(food_name):
    url = "https://dietagram.p.rapidapi.com/apiFood.php"
    querystring = {"name": food_name, "lang": "de"}
    headers = {
        "X-RapidAPI-Key": "d7ba395c72mshe67acba0ccfc242p172e6bjsndaf1a2106f77",
        "X-RapidAPI-Host": "dietagram.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return int(response.json()["dishes"][0]["caloric"])

@app.route("/", methods=["GET", "POST"])
def home():
    total_calories = 0
    food_list = []

    if request.method == "POST":
        food_name = request.form["food_name"]
        grams = request.form["grams"]

        if food_name == "break":
            # Calculate and display total calories for all foods
            for food_item in food_list:
                total_calories += food_item["calories"]
            return render_template("result.html", food_list=food_list, total_calories=total_calories)

        food_calories = get_calories(food_name) / 100 * int(grams)
        food_list.append({"name": food_name, "grams": grams, "calories": food_calories})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)