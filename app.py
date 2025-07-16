from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def hello():
    display = "<h1>Hello from Patryk's Topic & Skill Service!</h1>"
    display += '<a href="http://127.0.0.1:5000/topics">TOPICS</a>'
    return display


@app.route("/topics")
def get_topics():

    # filepath = "data/topics.json" <- nicht gute Weg
    filepath = os.path.join(os.path.dirname(__file__), "data", "topics.json") # <- optimale Weg
    
    with open(filepath, "r", encoding = "utf-8") as file:
        topics = json.load(file)
    return jsonify(topics)

if __name__ == '__main__':
    app.run(debug=True)