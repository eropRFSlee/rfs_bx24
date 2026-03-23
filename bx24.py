from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello, RUNPYTHON!"

if __name__ == "__main__":
app.run(debug=True)
