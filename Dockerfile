# 1. Use an official Python image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy your files into the container
COPY . .

# 4. Install the libraries
RUN pip install -r requirements.txt

# 5. Command to start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5080"]