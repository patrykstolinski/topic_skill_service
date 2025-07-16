from flask import Flask, jsonify
from data_manager import JsonDataManager #<- import new class for OOP read/write  
import json
import os

# Create the Flask app instance
app = Flask(__name__)
# Initialize the JSON data manager
data_manager = JsonDataManager()

# Define paths to the JSON data files
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
TOPICS_FILE = os.path.join(DATA_DIR, "topics.json")
SKILLS_FILE = os.path.join(DATA_DIR, "skills.json")

# Root route - returns a simple homepage with links to topics and skills
@app.route('/')
def hello():
    display = "<h1>Hello from Patryk's Topic & Skill Service!</h1>"
    display += '<a href="http://127.0.0.1:5000/topics">TOPICS</a>'
    display += "<br>"
    display += '<a href= "http://127.0.0.1:5000/skills">SKILLS</a>'
    return display

# ---------------------- Topics Routes ----------------------

# Route to return all topics
@app.route("/topics")
def get_topics():

    topics = data_manager.read_data(TOPICS_FILE)
    return jsonify(topics)

# Route to return a specific topic by its ID
@app.route("/topics/<string:topic_id>")
def get_topics_by_id(topic_id):

    topics = data_manager.read_data(TOPICS_FILE)
    # Debug output: show requested and available topic IDs
    print(f"[DEBUG] Requested Topic ID: {topic_id}")
    print(f"[DEBUG] Available Topic ID's: {[topic.get('id') for topic in topics]}")

    # Case-insensitive comparison to match topic ID
    for topic in topics:
        if topic.get("id").lower() == topic_id.lower():
            return jsonify(topic)
    # If no match is found, return error with 404
    return jsonify({"Error":"Topic not found"}), 404

# ---------------------- Skills Routes ----------------------

# Route to return all skills
@app.route("/skills")
def get_skills():

    skills = data_manager.read_data(SKILLS_FILE)    
    return jsonify(skills)

# Route to return a specific skill by its ID
@app.route("/skills/<string:skill_id>")
def get_skills_by_id(skill_id):

    skills = data_manager.read_data(SKILLS_FILE)
    # Debug output: show requested and available skill IDs
    print(f"[DEBUG] Requested Skill ID: {skill_id}")
    print(f"[DEBUG] Available Skill ID's: {[skill.get('id') for skill in skills]}")

    # Case-insensitive comparison to match skill ID
    for skill in skills:
        if skill.get("id").lower() == skill_id.lower():
            return jsonify(skill)
            
    # If no match is found, return error with 404
    return jsonify({"Error": "Skill not found."}), 404

# Stark the Flask app (only if this file is run directly, not when imported elsewhere)
if __name__ == '__main__':
    app.run(debug=True) #Enable debug mode for development