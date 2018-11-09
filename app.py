from flask import Flask, request, jsonify, render_template
import os
import dialogflow
import requests
import json
from bot import Bot
from grammar import Grammar
from utils import *

app = Flask(__name__)

project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
character_map, personality_map, emotion_map = read_attributes()
bot = Bot(project_id)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    c = request.form['character']
    p = request.form['personality']
    e = request.form['emotion']
    if not c or not p or not e:
        return jsonify({ "message":  "Please configure all options." })
    character = character_map[c]
    personality = personality_map[p]
    emotion = emotion_map[e]
    grammar = Grammar(character + personality + emotion)
    response = grammar.generate_response(message)
    if len(response) == 0:
        response = bot.use_chat_bot(message)
    if not response:
        response = clean_sentence(grammar.gen_sent("Sentence"))
    result_message = { "message":  response }
    return jsonify(result_message)

# run Flask app
if __name__ == "__main__":
    app.run()