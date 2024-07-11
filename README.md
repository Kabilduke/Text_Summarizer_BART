# BiDirectional Auto Regressive Transformer Summarizer
This project provides a web interface for uploading PDFs or entering text to generate a summarized output using the BiDirectional Auto Regressive Transformer (BART) model. 
The project is built using Flask for the backend and HTML, CSS, and JavaScript for the frontend.

## Screenshot/Output
<img src="https://github.com/Kabilduke/Text_Summarizer_BART/blob/main/Output%2C%20result%20or%20what%20ever%20you%20call%20it.png" alt="Project Screenshot" width="600">


### Features
- Upload a PDF file to extract text and generate a summary.
- Enter text directly into the text area to generate a summary.
- Real-time typing effect for displaying the summarized text.
- Flashy and interactive UI elements for an engaging user experience.

### Requirement 
- Python 3.x
- Flask
- PyPDF2
- Transformers
- JavaScript (Fetch API)

### Installation
1. Clone the repository
   ```sh
   git clone https://github.com/Kabilduke/Text_Summarizer_BART.git
   cd Text_Summarizer_BART
   ```

3. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install flask PyPDF2 transformers
   ```
   
4. Run the Flask app:
    ```sh
    python app.py
    ```

### Project Structure
```plaintext
Text_summarizer_BART/
│
├── app.py                  # Main Flask application
├── templates/
│   └── index.html          # Main HTML file
├── static/
│   ├── style.css           # CSS styles
├── uploads/                # Directory to store uploaded PDF files
└── README.md               # This README file
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.
