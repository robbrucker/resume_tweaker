FROM python:3.9-slim-buster

WORKDIR /.

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

# Run the application
CMD [ "python", "./app.py" ]