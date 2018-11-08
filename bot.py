import numpy as np
import re
from utils import *
from grammar import Grammar
from globals import *
import dialogflow_v2 as dialogflow

# Chatbot class
class Bot:
    def __init__(self, project_id):
        self.profession = None
        self.emotion = None
        self.personality = None
        self.character_map, self.personality_map, self.emotion_map = read_attributes()
        self.grammar = None
        self.project_id = project_id
        self.session_client = dialogflow.SessionsClient()
        self.session = self.session_client.session_path(self.project_id, "unique")

    def use_chat_bot(self, text):
        text_input = dialogflow.types.TextInput(text=text, language_code='en')
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = self.session_client.detect_intent(session=self.session, query_input=query_input)
        return response.query_result.fulfillment_text

    def handle_input(self, user_input):
        result_message = { "message":  "" }
        if user_input == "quit":
            result_message["message"] = "That was a great conversation!"
            return result_message
        if not self.profession:
            result_message["message"]  = "What is my profession? (Dartmouth Student, Wizard, Marine Biologist, Doctor Seuss, Jedi)"
            for p in CHAR_MATCHES.keys():
                if re.match(p, user_input):
                    self.profession = self.character_map[CHAR_MATCHES[p]]
                    result_message["message"]  = "My profession is now: " + user_input 
                    break
            return result_message
        elif not self.personality:
            result_message['message'] = "What is my personality? (Destructive, Fun, Negative, Happy)"
            for p in PERS_MATCHES.keys():
                if re.match(p, user_input):
                    self.personality = self.personality_map[PERS_MATCHES[p]]
                    result_message['message'] = "My personality is now: " + user_input 
                    break
            return result_message
        elif not self.emotion:
            result_message['message'] = "What is my emotion? (Happy, Sad)"
            for p in EMOT_MATCHES:
                if re.match(p, user_input):
                    self.emotion = self.emotion_map[EMOT_MATCHES[p]]
                    result_message['message'] = "My emotion is now: " + user_input 
                    break
            return result_message
        elif not self.grammar:
            custom_words = self.profession + self.personality + self.emotion
            self.grammar = Grammar(custom_words)
        response = self.grammar.generate_response(user_input)
        if len(response) == 0:
            response = self.use_chat_bot(user_input)
        if not response:
            response = clean_sentence(self.grammar.gen_sent("Sentence"))
        result_message['message'] = response
        return result_message