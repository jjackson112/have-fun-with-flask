from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "I'm going to crush Flask!"

# Run the flask server
if __name__ == "__main__":
    app.run(debug=True)