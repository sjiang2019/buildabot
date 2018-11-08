CHAR_MATCHES = {
    r'(dartmouth|Dartmouth)(.*)': "Dartmouth",
    r'(wizard|Wizard)(.*)': "Wizard",
    r'(marine biologist|Marine Biologist)(.*)': "Marine Biologist",
    r'(doctor seuss|Doctor Suess)(.*)': "Doctor Seuss",
    r'(Jedi|jedi)(.*)': "Jedi"
}

PERS_MATCHES = {
    r'(Destructive|destructive)':"Destructive",
    r'(Fun|fun)':"Fun",
    r'(Negative|negative)':"Negative",
    r'(Happy|happy)':"Happy"
}

EMOT_MATCHES = {
    r'(Happy|happy)': "Happy",
    r'(Sad|sad)': "Sad"
}

RESPONSE_MAP = {
    r'What (.*) (like|enjoy)?': "Interests",
    r'(.*)want(.*)?': "Desires",
    r'What (.*) to do?': "Hobbies",
    r'What (.*) think (.*)?': "Opinions",
    r'What (.*) think': "Opinions"
}