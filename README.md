Flask Beginner Toolkit – Hello World API
Overview 
This is a minimal Flask project designed for beginners to learn how to build a simple API.
The app responds with "Hello World!" when accessed via a web browser or API client.

Technology: Python + Flask
Goal: Demonstrate a working “Hello World” API and provide setup instructions for beginners.

System Requirements
OS: Windows
Python: 3.10+
Editor: VS Code (recommended) or any code editor
Python Package: Flask

Setup Instructions
Clone the Repository
git clone https://github.com/YOUR_USERNAME/flask-beginner-toolkit.git
cd flask-beginner-toolkit

Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate

Install Dependencies
pip install Flask

Run the App
python app.py

Access the API
Open your browser and go to:
http://127.0.0.1:5000/

You should see: Hello World!

Project Structure
flask-beginner-toolkit/
├── app.py           # Main Flask application
├── README.md        # Project instructions
└── venv/            # Virtual environment folder

AI Prompt Usage
This project was scaffolded and guided using AI prompts for faster learning:

Prompt	Summary of AI Response	Notes
"Step-by-step guide to create Hello World API with Flask"	Provided setup instructions and code example	Scaffolded project quickly

"How to run Flask on a different port?"	Explained app.run(port=5001)	Solved port conflict issue

Common Issues & Fixes
ModuleNotFoundError: No module named 'flask' → Run pip install Flask
Port 5000 already in use → Run app.run(port=5001)
Virtual environment not activating → Make sure you ran venv\Scripts\activate

References
Flask Official Documentation
RealPython Flask Tutorial
StackOverflow Flask Questions
