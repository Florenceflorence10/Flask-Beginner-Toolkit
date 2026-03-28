from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "Hello, Flask is working perfectly!"

# Optional: another route
@app.route('/about')
def about():
    return "This is a beginner Flask app."

# Run the app
if __name__ == '__main__':
    app.run(debug=True)