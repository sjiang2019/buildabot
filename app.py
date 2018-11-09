from flask import Flask, request, jsonify, render_template
import os
import dialogflow
import requests
import json
from bot import Bot
import pusher
import sys

# pusher_client = pusher.Pusher(
#     app_id=os.getenv('PUSHER_APP_ID'),
#     key=os.getenv('PUSHER_KEY'),
#     secret=os.getenv('PUSHER_SECRET'),
#     cluster=os.getenv('PUSHER_CLUSTER'),
#     ssl=True)

app = Flask(__name__, static_url_path="/static/")

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