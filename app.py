import os
from flask import Flask, jsonify
from data_manager import JsonDataManager 

app = Flask(__name__)
data_manager = JsonDataManager()

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json')
SKILLS_FILE = os.path.join(DATA_DIR, 'skills.json')


@app.route('/')
def hello_world():
    return "Hello from Topic and Skill Service!"

# --------------------- topics ---------------------
@app.route('/topics', methods=['GET'])
def get_topics():
    topics = data_manager.read_data(TOPICS_FILE)
    return jsonify(topics)

# --------------------- topics by ID ---------------
@app.route('/topics/<string:id>', methods = ['GET'])
def get_topic_by_id(id):
    # read the topic file
    topics = data_manager.read_data(TOPICS_FILE)
    # for debugging purposes, print the requested and available ID's to the console
    print(f"[DEBUG] Requested Topic ID: '{id.lower()}'.")
    print(f"[DEBUG] Available Topic ID's: {[topic.get('id').lower() for topic in topics]}")
    # next() function is more effective as list comprehension - does the same.
    topic = next((topic for topic in topics if topic.get('id').lower() == id.lower()), None)
    if topic:
        return jsonify(topic)
    # if not, return error 
    return jsonify({"[ERROR]": "Topic not found"}), 404


# --------------------- skills ---------------------
    # # loop through ID's to find the requested ID
@app.route('/skills', methods = ['GET'])
def get_skills():
    skills = data_manager.read_data(SKILLS_FILE)
    return jsonify(skills)


# --------------------- skills by ID ---------------
@app.route('/skills/<id>', methods = ['GET'])
def get_skills_by_id(id):
    skills = data_manager.read_data(SKILLS_FILE)
    



if __name__ == '__main__':
    app.run(debug=True, port=5000)