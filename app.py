from flask import Flask, request, jsonify, render_template
import os
import dialogflow
import requests
import json
from bot import Bot
import sys

app = Flask(__name__, static_url_path="/static/")
bot = None


@app.before_first_request
def create_bot():
    global bot
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    bot = Bot(project_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    response = bot.handle_input(message)
    return jsonify(response)

# run Flask app
# if __name__ == "__main__":
#     app.run()