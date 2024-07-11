from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from PyPDF2 import PdfReader
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load the pre-trained BART tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
  
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods =['POST'])
def upload_file():
    if 'file' not in request.files:
        flash("No File Path")
        return redirect(url_for('index'))
    file = request.files['file']


    if file.filename == '':
        flash("Not Selected File")
        return redirect(url_for('index'))
    
    if file and file.filename.endswith('.pdf'):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        flash("File Successfully Uploaded")
        file.save(file)
        text = extract_text_from_pdf(file)

        inputs = tokenizer(text, max_length=1024, return_tensors="pt", truncation=True)
        summary_ids = model.generate(inputs["input_ids"], num_beams=4, max_length=300, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True) 

        return render_template('index.html', summary=summary)

    
    else:
        flash("Only PDF file are alllowed")
        return redirect(url_for('index'))
    
@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.json
    text  = data.get('text', '')
    

    if text:
        inputs = tokenizer(text, max_length=1024, return_tensors="pt", truncation=True)
        summary_ids = model.generate(inputs["input_ids"], num_beams=4, max_length=300, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True) 

        return jsonify({'summary': summary})
    
    return jsonify({'summary': ''}), 400

if __name__ == "__main__":
    app.run(debug=True)