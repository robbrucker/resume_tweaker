from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
from services.openai_service import OpenAiService
from services.resume_service import ResumeService
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tailor", methods=["POST"])
def tailor_resume():

    openai_service = OpenAiService()
    resume_service = ResumeService()
    job_description = request.form["job_description"]

    matched_skills = resume_service.match_skills(job_description, openai_service.get_resume_skills())

    generated_resume_blurb = openai_service.generate_resume(job_description, openai_service.get_resume_skills())

    tailored_resume = resume_service.update_resume(request.files["resume_file"], generated_resume_blurb, matched_skills)

    file_name = openai_service.generate_file_name(job_description)
    full_file_name = file_name+".docx"

    tailored_resume.save(full_file_name)

    return send_file(full_file_name)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)