from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import pytesseract
import re
import os
import tempfile  # Import tempfile module

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with your path

def extract_pressure(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return []

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    
    best_matches = []
    for psm in [11]:
        text = pytesseract.image_to_string(thresh, config=f'--psm {psm}')
        pressure_pattern = r"\b\d{2}\.\d{2}\b|\b\d{2} \d{2}\b"
        matches = re.findall(pressure_pattern, text)

        if matches:
            for match in matches:
                if '.' in match and match not in best_matches:
                    best_matches = [match]
                    break
                elif ' ' in match and match not in best_matches:
                    if not best_matches:
                        best_matches.append(match)

    formatted_matches = [match.replace(" ", ".") for match in best_matches]
    return formatted_matches

@app.route('/upload', methods=['POST'])
def extract_pressure_route():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Use tempfile to create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
        image_path = temp_file.name  # Get the name of the temporary file
        file.save(image_path)

    try:
        pressures = extract_pressure(image_path)
        return jsonify({'pressures': pressures})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        if os.path.exists(image_path):
            os.remove(image_path)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

