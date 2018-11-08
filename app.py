from flask import Flask, request, jsonify, render_template
import os
import dialogflow
import requests
import json
import pusher
from bot import Bot

app = Flask(__name__, static_url_path="/static")

# initialize Pusher
pusher_client = pusher.Pusher(
    app_id=os.getenv('PUSHER_APP_ID'),
    key=os.getenv('PUSHER_KEY'),
    secret=os.getenv('PUSHER_SECRET'),
    cluster=os.getenv('PUSHER_CLUSTER'),
    ssl=True)

project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
bot = Bot(project_id)

@app.route('/')
def index():
    return render_template('index.html')

def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)
        return response.query_result.fulfillment_text

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    response = bot.handle_input(message)
    pusher_client.trigger('movie_bot', 'new_message', {'human_message': message, 'bot_message': response['message']})                   
    # return jsonify(response_text)
    return jsonify(response)

# # run Flask app
# if __name__ == "__main__":
#     app.run()