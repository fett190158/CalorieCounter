import requests

def get_calories(food_name):
    url = "https://dietagram.p.rapidapi.com/apiFood.php"
    querystring = {"name":food_name,"lang":"de"}
    headers = {
        "X-RapidAPI-Key": "d7ba395c72mshe67acba0ccfc242p172e6bjsndaf1a2106f77",
        "X-RapidAPI-Host": "dietagram.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return int(response.json()["dishes"][0]["caloric"])

total_calories = 0

while True:
    print("Enter Food:")
    food_name = input()
    if food_name == "break":
        break
    print("Enter grams:")
    grams = input()
    food_calories = get_calories(food_name) / 100 * int(grams)
    total_calories = food_calories + total_calories

print(total_calories + "ckal")