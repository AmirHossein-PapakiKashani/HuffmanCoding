from flask import Flask, jsonify
import lorem
from huffman import HuffmanCoding

app = Flask(__name__)
H = HuffmanCoding("C:/Users/rayanmehr/Desktop/ProjectForAlgorithemDesign/second problem/filehodhod.txt")

@app.route('/api/latin', methods=['GET'])
def generate_latin_text():
    latin_text = lorem.paragraph()
     # Save the lines to a text file
    with open('filehodhod.txt', 'w') as file:
        file.write(latin_text) 
    compress_data = H.compress()
   
    return jsonify({'latin_text': latin_text})

if __name__ == '__main__':
    app.run(debug=True)
