import os
import uuid
from flask import Flask, jsonify, request
from data_manager import JsonDataManager 

app = Flask(__name__)
data_manager = JsonDataManager()

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json')
SKILLS_FILE = os.path.join(DATA_DIR, 'skills.json')


@app.route('/')
def hello_world():
    return "Hello from Patryk's Topic and Skill Service!"

# ------------------- GET METHODS ------------------
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
    return jsonify({"[ERROR]": "Topic ID not found"}), 404


# --------------------- skills ---------------------
    # # loop through ID's to find the requested ID
@app.route('/skills', methods = ['GET'])
def get_skills():
    skills = data_manager.read_data(SKILLS_FILE)
    return jsonify(skills)


# --------------------- skills by ID ---------------
@app.route('/skills/<string:id>', methods = ['GET'])
def get_skills_by_id(id):
    skills = data_manager.read_data(SKILLS_FILE)
    # for debugging purposes, print the requested and available ID's to the console
    print(f"[DEBUG] Requested Skill ID: {id}")
    print(f"[DEBUG] Available Skill ID's: {[skill.get('id').lower() for skill in skills]}")
    # Iterator over the skill list on ID base - if found, get the insides, if not, give None back
    skill = next((skill for skill in skills if skill.get('id').lower() == id.lower()), None)
    if skill:
        return jsonify(skill)
    return jsonify({"[ERROR]": "Skill ID Not found"}), 404 
 
# ------------------- POST METHODS -----------------
# --------------------- topics ---------------------

@app.route('/topics', methods = ["POST"])
def create_topic():
    # this extracts all information from request as eine Dictionary
    new_topic_data = request.json
    # this checks if specific keys are not present in POST request
    if not new_topic_data or 'name' not in new_topic_data or 'description' not in new_topic_data:
        return jsonify({"[ERROR]":"'Name' or 'description' not in POST"}),400
    # this generates random ID with uuid.uuid4() 
    new_topic_id = str(uuid.uuid4())
    # this is a new dictionary, to which we assign values from the dict from POST request (apart from ID)
    topic = {
        "id": new_topic_id,
        "name": new_topic_data['name'],
        "description": new_topic_data["description"],
        "prerequisites": new_topic_data.get("prerequisites", "Unknown prerequisites"),
        "parentTopicId": new_topic_data.get("parentTopicId", "Unknown parent Topic ID")
    }
    # open the data with data_manager read_data()
    topics = data_manager.read_data(TOPICS_FILE)
    # as this is a list, we append the whole new topic dict to the end of the list
    topics.append(topic)
    # we save the data with write_data()
    data_manager.write_data(TOPICS_FILE, topics)
    # return the 
    return jsonify(topic), 201


# --------------------- Skills ---------------------

@app.route('/skills', methods = ["POST"])
def create_skills():
    # this extracts all information from request as eine Dictionary
    new_skill_data = request.json
    # this checks if specific keys are not present in POST request
    if not new_skill_data or 'name' not in new_skill_data or 'topicId' not in new_skill_data:
        return jsonify({"[ERROR]":"'Name' or 'topicId' not in POST"}),400    
    # this generates random ID with uuid.uuid4() 
    new_skill_id = str(uuid.uuid4())
    # this is a new dictionary, to which we assign values from the dict from POST request (apart from ID)
    skill = {
        "id": new_skill_id,
        "name": new_skill_data['name'],
        "topicId": new_skill_data.get("topicId", "Unknown Topic ID"),
        "difficulty": new_skill_data.get("difficulty", "Unknown Difficulty")
    }
    # open the data with data_manager read_data()
    skills = data_manager.read_data(SKILLS_FILE)
    # as this is a list, we append the whole new topic dict to the end of the list
    skills.append(skill)
    # we save the data with write_data()
    data_manager.write_data(SKILLS_FILE, skills)
    # return the 
    return jsonify(skill), 201



if __name__ == '__main__':
    app.run(debug=True, port=5000)