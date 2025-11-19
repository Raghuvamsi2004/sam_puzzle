from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the root URL route
@app.route('/')
def home():
    """
    Renders index.html. Flask's render_template makes the 'url_for' function 
    available inside the index.html template for referencing static files.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Run the server
    print("----------------------------------------------------------")
    print("🚀 FLASK SERVER READY!")
    print("Open your browser and navigate to: http://127.0.0.1:5000/")
    print("----------------------------------------------------------")
    app.run(debug=True)