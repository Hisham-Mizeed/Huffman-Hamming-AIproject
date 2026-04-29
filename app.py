from flask import Flask, render_template, request

# Import algorithms
from huffman import huffman_process
from hamming import hamming_process

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    algorithm = None

    if request.method == "POST":
        text = request.form["text"]

        # اختيار الخوارزمية
        algorithm = request.form.get("algorithm")

        # Uppercase option
        if request.form.get("uppercase") == "on":
            text = text.upper()

        # تنفيذ حسب الاختيار
        if algorithm == "huffman":
            result = huffman_process(text)

        elif algorithm == "hamming":
            result = hamming_process(text)

    return render_template("index.html", result=result, algorithm=algorithm)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)