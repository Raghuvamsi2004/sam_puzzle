from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the root URL route
@app.route('/')
def home():
    """
    This function renders the index.html file found inside the 'templates' folder.
    All the game logic (HTML, CSS, JavaScript) is handled by the frontend file.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Start the server on port 5000. 
    # The debug=True flag allows the server to restart automatically when you save changes.
    print("----------------------------------------------------------")
    print("🚀 FLASK SERVER READY!")
    print("Open your browser and navigate to: http://127.0.0.1:5000/")
    print("----------------------------------------------------------")
    app.run(debug=True)