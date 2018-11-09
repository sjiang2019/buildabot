# Build-a-Bot

Steven Jiang

Writing with Algorithms Final Project

See the live demo [here](https://dialego.herokuapp.com/).

## Overview

Chatbots are typically created for functional, pragmatic purposes. As a result, our interactions with chatbots are limited to shallow, one-sided experiences. This project aims to provide an unconventional chatbot experience by introducing elements of character, personality, and emotion.

## How it works

### Customizablity
The chatbot has three customizable elements: character, personality, and emotion. Character is signified by nouns. For example, if the character is "Marine Biologist", then some of the nouns may be "lobsters", "crabs", "dolphins", "fish", etc. Personalities are exemplified through verbs. For example, if the personality is "Happy", the verbs may be "amuse", "delight", etc. Finally, emotion is characterized by adjectives. For example, if the emotion is "Sad", some of the adjectives may be "rejected", "neglected", etc.

### Handling User Input
When a user sends a message, the program looks for keywords that relate to certain sentence structures. For example, if the message is "What do you want?", the keywords "you" and "want" will trigger a sentence structure that exhibits a desire, i.e. "I want..." The program then generates a sentence of the desired sentence structure using a probabilistic Context Free Grammar, with the selected nouns, verbs, and adjectives. However, given the scope of this project, the number of keywords and sentence sentence structures are limited. If the program doesn't detect any keywords, the message is sent to DialogFlow's pre-built Small Talk bot, which handles generic greetings and questions. Finally, if Small Talk bot doesn't recognize the input, then a random sentence is generated using the Context Free Grammar provided.

## Getting Started

### Prerequisites
 - Python 3.6 
 - JavaScript (jQuery)
 - Flask
 - [Dialogflow] (https://dialogflow.com/)
 - [Ngrok](https://ngrok.com/)

### Dialogflow

- Create a Dialogflow account [here](https://console.dialogflow.com/api-client/#/login)
- Enable the pre-built small talk chatbot
- Click on Fulfillment and enable webhook
- Get your Dialogflow API key and connect to [Google Cloud] (https://console.cloud.google.com/apis/credentials/serviceaccountkey)
  - Select `Dialogflow integrations` under `Service account`
  - Then select `JSON` under `key type`. 
- Copy the API key JSON file to the root folder of the project
- Update keys in the `.env` file with the correct information

### Running the App

 - From a command line, cd into the project root folder - `buildabot`
 - Install the dependencies:
 ```
 pip install -r requirements.txt
 ```
 - Run the app:
 ```
  flask run
 ```
- The app should now be running on http://localhost:5000

## Acknowledgements

* [Flask](http://flask.pocoo.org/): A microframework for Python
* [Dialogflow](https://dialogflow.com/): A Google-owned developer of human–computer interaction technologies based on natural language conversations
* [Materialize](https://materializecss.com/): A modern responsive front-end framework based on Material Design
* Boilerplate code borrowed from [this repo](https://github.com/dongido001/flask_chatbot)
