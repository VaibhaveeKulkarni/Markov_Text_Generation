from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Re-define the dataset and build the Markov Chain
# In a real application, you might load this from a pre-trained file
text_data = """
Once upon a time there was a brave king.
The king ruled a beautiful kingdom.
The people loved the king because he was kind.
One day a dragon attacked the kingdom.
The brave king fought the dragon.
The dragon flew away.
Everyone celebrated the victory.
"""
words_app = text_data.split()

markov_chain_app = {}
for i in range(len(words_app) - 1):
    current_word = words_app[i]
    next_word = words_app[i + 1]

    if current_word not in markov_chain_app:
        markov_chain_app[current_word] = []
    markov_chain_app[current_word].append(next_word)

def generate_text_app(start_word, length=30):
    if start_word not in markov_chain_app:
        return "Starting word not found in dataset."

    current_word = start_word
    result = [current_word]

    for _ in range(length - 1):
        if current_word not in markov_chain_app:
            break
        current_word = random.choice(markov_chain_app[current_word])
        result.append(current_word)

    return " ".join(result)

@app.route('/generate', methods=['GET'])
def generate():
    start_word = request.args.get('start_word', 'The')
    length = int(request.args.get('length', 30))
    
    generated = generate_text_app(start_word, length)
    return jsonify({"generated_text": generated})

@app.route('/')
def home():
    return "Welcome to the Markov Chain Text Generator! Use /generate?start_word=<word>&length=<num> to generate text."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
