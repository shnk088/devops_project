FROM python:3.10-slim

 WORKDIR /app

 COPY requirements.txt .
 RUN pip install --no-cache-no-dir -r requirements.txt || true
 COPY app.py .
 ENV PORT=8080
 EXPOSE 8080
 CMD ["python","app.py"]