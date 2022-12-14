FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

