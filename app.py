from flask import Flask, render_template ,send_from_directory

app = Flask(__name__)

# Root URL -> home.html
@app.route("/")

def home():
    return render_template("index.html")  # looks in templates/home.html


@app.route("/download-resume")
def download_resume():
    return send_from_directory("protected_data", "resume.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)  # remove debug=True in production
