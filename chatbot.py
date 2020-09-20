import json
from string import punctuation
import random

# Dict file with (word: topic) translation
DICT_FILE = 'translate.json'

# Dict file with (topic: [questions]) translation
QUESTION_FILE = 'questions.json'

# Load files
with open(DICT_FILE, 'r') as in_file:
    trans_dict = json.load(in_file)

with open(QUESTION_FILE,'r') as in_file:
    question_dict = json.load(in_file)    


def main():
    try:
        while True:
            user_message = input()
            bot_answear = chat(user_message)
            print(bot_answear)
    except KeyboardInterrupt:
        print("Bye...")

def chat(user_message: str):
    """Find appropriate answear for user message."""
    # Delete punctuation and format
    s = user_message.translate(str.maketrans('', '', punctuation))
    s = s.split()
    #print(s)
    # Mix array with words
    for word in random.sample(s, len(s)):
        if word in trans_dict:
            topic = trans_dict[word]
            return random.choice(question_dict[topic])
    return random.choice(question_dict["$default"])


if __name__ == '__main__':
    main()
