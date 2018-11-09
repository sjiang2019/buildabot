import dialogflow_v2 as dialogflow

# Chatbot class
class Bot:
    def __init__(self, project_id):
        self.project_id = project_id
        self.session_client = dialogflow.SessionsClient()
        self.session = self.session_client.session_path(self.project_id, "unique")

    def use_chat_bot(self, text):
        text_input = dialogflow.types.TextInput(text=text, language_code='en')
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = self.session_client.detect_intent(session=self.session, query_input=query_input)
        return response.query_result.fulfillment_text