FROM python:3.10

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY run.py .
COPY project project
ENV FLASK_APP=run.py

CMD gunicorn run -h 0.0.0.0 -p 5000