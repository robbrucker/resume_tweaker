from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
from services.openai_service import OpenAiService
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tailor", methods=["POST"])
def tailor_resume():

    openai_service = OpenAiService()
    job_description = request.form["job_description"]

    matched_skills = openai_service.match_skills(job_description, openai_service.get_resume_skills())

    resume = openai_service.generate_resume(job_description, openai_service.get_resume_skills())

    doc = openai_service.update_resume(request.files["resume_file"], resume, matched_skills)
    doc.save("generated_resume.docx")
    return send_file("generated_resume.docx")


if __name__ == "__main__":
    app.run(debug=True,port=5001)