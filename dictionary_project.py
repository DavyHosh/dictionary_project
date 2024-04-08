import json
from difflib import get_close_matches

#Loading the JSON data into the dictionary
def load_data():
    with open('data.json', 'r') as file:
        return json.load(file)
    
# Function to get definition of a word
def get_definition(word, data):
    word = word.lower() # Convert the word to lowercase for case insensitivity
    if word in data:
        return data[word]
    elif word.title() in data: # Check for capitalized words
        return data[word.title()]
    elif word.upper() in data: # Check for all uppercase words
        return data[word.upper()]
    else:
    # Try to find similar words using difflib
        suggestions = get_close_matches(word, data.keys(), n=3, cutoff=0.8)
        if suggestions:
            return f"Word not found. Did you mean {','.join(suggestions)}?"
        else:
            return "Word not found."

#Main funtion to interact with the user
def main():
    data = load_data()
    while True:
        word = input("Enter a word to get its definition (q for quit): ")
        if word.lower() == 'q':
            break
        definition = get_definition(word, data)
        print(definition)


if __name__ == "__main__":
    main() 

    












#https://github.com/DavyHosh/dictionary_project