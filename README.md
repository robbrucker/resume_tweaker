# resume_tweaker
Put in a job description and your resume, and use AI to tweak your resume to the job description

## Getting started
- Generate OpenAI key and put it in a file called .env 
```OPENAI_API_KEY=yourkey```
- Change the constants file, `skills` and `personal_name`
- Make sure your resume has a header called Overview and another called Technologies

## Installing
# 1. Navigate to your project directory:
`cd /path/to/your/project`

# 2. Create a new virtual environment in a directory named "venv":
`python3 -m venv venv`

# 3. Activate the virtual environment:
# On macOS/Linux:
`source venv/bin/activate`

# On Windows:
`.\venv\Scripts\activate`

# 4. Install dependencies
`pip install -r requirements.txt`

# 5. Run flask app
`python app.py`

# 6. Open 
http://127.0.0.1:5001/ (or whatever port you used)