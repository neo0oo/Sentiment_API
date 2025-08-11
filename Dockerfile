FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host","0.0.0.0","--port", "80"]


# in bash:
# docker build -t sentiment-api .
# docker run -p 8000:80 sentiment-api

