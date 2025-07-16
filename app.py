from flask import Flask, jsonify
from data_manager import JsonDataManager #<- import new class for OOP read/write  
import json
import os

app = Flask(__name__)
data_manager = JsonDataManager()

@app.route('/')
def hello():
    display = "<h1>Hello from Patryk's Topic & Skill Service!</h1>"
    display += '<a href="http://127.0.0.1:5000/topics">TOPICS</a>'
    display += "<br>"
    display += '<a href= "http://127.0.0.1:5000/skills">SKILLS</a>'
    return display


# def get_topics():

#     # filepath = "data/topics.json" <- nicht gute Weg
#     filepath = os.path.join(os.path.dirname(__file__), "data", "topics.json") # <- optimale Weg
    
#     with open(filepath, "r", encoding = "utf-8") as file:
#         topics = json.load(file)
#     return jsonify(topics)

############# Topics #############
@app.route("/topics")
def get_topics():

    topics = data_manager.read_data("data/topics.json")
    return jsonify(topics)

@app.route("/topics/<string:topic_id>")
def get_topics_by_id(topic_id):

    topics = data_manager.read_data("data/topics.json")
    #### Debug ###
    print(f"[DEBUG] Requested ID: {topic_id}")
    print(f"[DEBUG] Available ID's: {[topic.get('id') for topic in topics]}")

    for topic in topics:
        if topic.get("id").lower() == topic_id.lower():
            return jsonify(topic)
    return jsonify({"Error":"Topic not found"}), 404

############# Skills #############
@app.route("/skills")
def get_skills():

    skills = data_manager.read_data("data/skills.json")    
    return jsonify(skills)

@app.route("/skills/<string:skill_id>")
def get_skills_by_id(skill_id):

    skills = data_manager.read_data("data/skills.json")
    #### Debug ####
    print(f"[DEBUG] Requested ID: {skill_id}")
    print(f"[DEBUG] Available ID's: {[skill.get('id') for skill in skills]}")
    for skill in skills:
        if skill.get("id").lower() == skill_id.lower():
            return jsonify(skill)
    return jsonify({"Error": "Skill not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)

    