CRA Compliance Classifier

A web-based tool that automatically analyzes product documentation 
against the EU Cyber Resilience Act (Regulation 2024/2847) using 
Google Gemini AI.

 Features
- Upload any product PDF or TXT document
- Automatic CRA scope determination (In Scope / Out of Scope)
- Risk classification (Default / Important / Critical)
- 22-point compliance checklist based on CRA gate logic
- Powered by Google Gemini 2.5 Flash

 Tech Stack
- Python / Flask (web server)
- Google Gemini AI (analysis)
- PyPDF2 (PDF text extraction)
- pandas (checklist processing)

Project Structure
cra-compliance-classifier/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .env                    # API key config (not committed)
├── templates/
│   └── index.html          # Web interface
└── ../References/
    ├── checklist_simple.csv          # 22-point CRA checklist
    ├── Regulation - 2024_2847...pdf  # CRA regulation
    ├── Regulation - 2017_745...pdf   # MDR 2017/745
└── Regulation - 2017_746...pdf   # MDR 2017/746
└── Regulation - 2019_2144...pdf   # Automotive 2019/2144

Setup & Installation
1. Clone the repository
git clone https://github.com/yourusername/cra-compliance-classifier.git
cd cra-compliance-classifier

2. Create a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate        # Mac / Linux

3. Install dependencies
pip install -r requirements.txt

4. Configure your API key
Create a .env file inside cra-compliance-classifier/ with:
GEMINI_API_KEY=your_gemini_api_key_here
FLASK_SECRET_KEY=any-random-string
FLASK_DEBUG=True
Get a free Gemini API key at: https://aistudio.google.com/apikey

5. Run the app
python app.py
The app will start a local web server.
Open your browser at the adress that is displayed.
