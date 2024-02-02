from flask import Flask, request, jsonify
from docx import Document

app = Flask(__name__)

def check_wmf_in_docx(docx):
    doc = Document(docx)

    for rel in doc.part.rels:
        if "image" in doc.part.rels[rel].target_ref:
            image_ext = doc.part.rels[rel].target_ref.split('.')[-1].lower()
            if image_ext == 'wmf':
                return True
    return False

@app.route('/api/checkwmf', methods=['POST'])
def checkWMF():
    if 'file' not in request.files:
        return jsonify({"error": "Docx file is required"}), 400

    docx_file = request.files['file']

    if docx_file:
      contains_wmf = check_wmf_in_docx(docx_file)
      if contains_wmf:
        return jsonify({"isWmf": True,"result": "The document contains WMF images."}), 200
      else:
        return jsonify({"isWmf": False,"result": "No WMF images found in the document."}), 200
    else:
       return jsonify({"error": "Dox file is required"}), 400

if __name__ == '__main__':
    app.secret_key = ''
    app.run(debug=True, host='0.0.0.0',port=7000)
