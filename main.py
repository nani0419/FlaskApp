from flask import Flask, render_template

app = Flask("__main__")

@app.route("/")
def index():
    return "Test!"

@app.route("/demo")
def demo():
    return "Demo!"

@app.route("/webpage")
def webpage():
    return render_template("test.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)