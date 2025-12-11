From python:3.10-slim

 WORKDIR /app

 copy src/ src/

 CMD ["python","src/app.py"]