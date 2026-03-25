from flask import Flask, render_template, request
import pdfplumber
import os
from analyzer import extract_skills, calculate_similarity, get_missing_skills

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

def extract_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}

    if request.method == "POST":
        file = request.files["resume"]
        job_desc = request.form["job_desc"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            resume_text = extract_text(filepath)

            skills = extract_skills(resume_text)
            score = calculate_similarity(resume_text, job_desc)
            missing = get_missing_skills(skills, job_desc)

            result = {
                "score": score,
                "skills": skills,
                "missing": missing
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
