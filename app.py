from flask import Flask, render_template, request
from agent import ask_agent

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""

    if request.method == "POST":
        question = request.form["question"]
        answer = ask_agent(question)

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)