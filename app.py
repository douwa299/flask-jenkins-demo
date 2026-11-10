from flask import Flask, jsonify, request

app = Flask(__name__)


def add(a, b):
    return a - b


@app.route("/")
def home():
    return jsonify(message="Hello from Flask + Jenkins!")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/add")
def add_route():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
    except ValueError:
        return jsonify(error="a and b must be numbers"), 400
    return jsonify(result=add(a, b))


if __name__ == "__main__":
    app.run(debug=True)