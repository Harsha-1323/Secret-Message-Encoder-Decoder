from flask import Flask, render_template, request
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        action = request.form.get("action")
        message = request.form.get("message")

        if action == "encode":
            result = base64.b64encode(message.encode()).decode()
        elif action == "decode":
            try:
                result = base64.b64decode(message).decode()
            except Exception:
                result = "Invalid input for decoding!"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
