from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return {"message": "Welcome to my app"}

if __name__ == "__main__":
    app.run(debug=True)