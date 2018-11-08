import os

def read_att_file(file):
    f_name = os.getcwd() + "/static/nlp/%s"%file
    att_map = {}
    with open(f_name, "r") as f:
        for line in f.readlines():
            line = line.split(",")
            att_map[line[0]] = line[1:]
    return att_map

def read_attributes():
    character_map = read_att_file("characters.txt")
    personality_map = read_att_file("personalities.txt")
    emotion_map = read_att_file("emotions.txt")
    return character_map, personality_map, emotion_map

def clean_sentence(sentence):
    sentence = sentence[0].upper() + sentence[1:-1] + "."
    return sentence