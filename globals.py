RESPONSE_MAP = {
    r'(.*)think(.*)?': "Opinions",
    r'(.*)think?': "Opinions",
    r'(.*)want(.*)?': "Desires",
    r'(.*)want?': "Desires",
    r'(.*)(to do|doing)?': "Hobbies",
    r'(.*)(like|enjoy)(.*)?': "Interests",
    r'(.*)(like|enjoy)?': "Interests",
}