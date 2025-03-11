from flask import Flask
import sklearn  

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, nice to meet you snyk"

if __name__ == "__main__":
    app.run(debug=True)
