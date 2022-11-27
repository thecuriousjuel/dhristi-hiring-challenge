# Importing the required modules
from flask import Flask
from flask import request

# Creating the flask app
app = Flask(__name__)


# Function to generate the valid substrings
def generate_sequence(word_list):
    # First 3 words are picked to generate substring
    word1 = word_list[0]
    word2 = word_list[1]
    word3 = word_list[2]

    # Generating all valid substring for the first word
    seq1 = []
    for i in range(len(word1)):
        t = word1[:i]
        if len(t) > 0:
            seq1.append(t)

    # Generating all valid substring for the second word
    word2 = word2[1:-1]
    seq2 = []

    for i in range(len(word2)):
        for j in range(i, len(word2)):
            t = word2[i:(j + 1)]
            if len(t) > 0:
                seq2.append(t)

    # Generating all valid substring for the third word
    seq3 = []
    for i in range(len(word3)):
        t = word3[i + 1:]
        if len(t) > 0:
            seq3.append(t)

    # Combining all the generated substrings
    generated_sequences = []
    for i1 in seq1:
        for i2 in seq2:
            for i3 in seq3:
                out = i1 + i2 + i3
                generated_sequences.append(out)

    # Returning the generated substrings to the calling function
    return generated_sequences


# Creating a POST endpoint to receive the JSON containing the list of words
@app.route("/words", methods=['POST'])
def words():
    # Receiving the JSON object and converting it to dictionary
    l = request.get_json()
    try:
        # Extracting the list of words from the dictionary and
        # passing the list of words to generate the sequence.
        generated_sequences = generate_sequence(l['words'])

        # If the above function return an empty list, an exception is raise
        # stating that the operation was not successful
        if len(generated_sequences) == 0:
            raise Exception
    except Exception:
        # Any Exception occurred during the runtime is handled and
        # a status code with a response message is sent to the client.
        return dict(response='No Words Found'), 404

    # If there happens to be no exceptions and the list of substrings
    # are generated correctly then the list of words are returned to the
    # client with a success status code.
    return dict(words=generated_sequences), 200


if __name__ == '__main__':
    # The flask app starts only when called by the main.py file (main thread)
    app.run(debug=False)
