from flask import Flask, jsonify
import lorem
from huffman import HuffmanCoding
app = Flask(__name__)

@app.route('/api/latin', methods=['GET'])
def generate_latin_text():
    latin_text = lorem.paragraph()

    # Compress the Latin text using Huffman coding
    compressed_data = HuffmanCoding.compress(latin_text)

    # Save the compressed data to a binary file
    with open('latin_text.bin', 'wb') as file:
        file.write(compressed_data)

    return jsonify({'latin_text': latin_text})

if __name__ == '__main__':
    app.run(debug=True)
