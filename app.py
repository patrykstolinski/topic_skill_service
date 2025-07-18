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



# --------------------- skills ---------------------

@app.route('/skills', methods = ['GET'])
def get_skills():
    skills = data_manager.read_data(SKILLS_FILE)
    return jsonify(skills)


if __name__ == '__main__':
    app.run(debug=True, port=5000)