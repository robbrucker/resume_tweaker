from dotenv import load_dotenv
import os
from openai import OpenAI
import sys
from services.openai_service import OpenAiService

class Main():
    def __init__(self):
        self.openai_service = OpenAiService()
        self.resume_skills =  [
            # Programming Languages
            "Java", "Python", "Ruby", "JavaScript", "Kotlin", "PHP", "TypeScript",

            # Frameworks
            "Spring", "Node.js", "Rails", "Django", "Laravel", "Vue.js", "Angular",

            # Databases and Data Tools
            "PostgreSQL", "MySQL", "SQL Server", "SQLite", "Redshift", "MongoDB", "ElasticSearch", "Redis",

            # Cloud Platforms
            "AWS", "Azure", "Google Cloud Platform (GCP)",

            # Professional Expertise
            "API Development and Integration",
            "Backend Development",
            "Frontend Development",
            "System Design and Scalability",
            "Testing and Documentation",
            "Data Analysis and Reporting",
            "Team Leadership",
            "CI/CD Systems",

            # Soft Skills
            "Technical Analysis and Debugging",
            "Project Management and Collaboration",
            "Stakeholder Communication"
        ]

    def validate_file_path(self, file_path):
        if not os.path.exists(file_path) or not file_path.endswith('.docx'):
            return False
        return True

    @staticmethod
    def multiline_input(prompt):
        print(prompt)
        contents = []
        while True:
            line = input()
            if line:
                contents.append(line)
            else:
                break
        return '\n'.join(contents)

    def get_job_description(self):
        print("Paste job description below and press Enter twice when done")
        job_description = sys.stdin.read()
        return job_description.strip()

    def get_inputs(self):

        job_description = self.get_job_description()
        # #job_description = input("Paste job description here: \n")
        # while True:
        #     resume_file = input("Enter path to your existing resume (.docx):\n")
        #     if self.validate_file_path(resume_file):
        #         break
        #     else:
        #         print("Invalid file path or the file does not exist. Please try again.")
        return job_description, "rob_brucker_cv_2024.docx"



    def automate_workflow(self):
        job_description, resume_file = self.get_inputs()
        print(job_description)
        print(self.resume_skills)
        matched_skills = self.openai_service.match_skills(job_description, self.resume_skills)
        print(matched_skills)
        resume = self.openai_service.generate_resume(job_description, self.resume_skills)
        doc = self.openai_service.update_resume(resume_file, resume, matched_skills)
        output_file = "updated_resume.docx"
        doc.save(output_file)


main_instance = Main()
main_instance.automate_workflow()
#rob_brucker_cv_2024.docx