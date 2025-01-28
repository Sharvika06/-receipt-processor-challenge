# -receipt-processor-challenge

Receipt Processor API
A FastAPI-based application for processing receipts and calculating points.

Features
Submit receipts for processing.
Retrieve points for processed receipts.
Swagger UI and OpenAPI documentation.

Technologies
Python 3.10
FastAPI
Pydantic
Docker (optional)

<!-- Getting Started -->

Run Locally

Clone the repo:
git clone <repo-url>
cd receipt-processor-challenge

Create a virtual environment:
python3 -m venv venv
source venv/bin/activate 

Install dependencies:
pip install -r requirements.txt

Start the server:
uvicorn app:app --reload --host 0.0.0.0 --port 8000

Open Swagger UI:
http://localhost:8000/docs

Run with Docker
Build the Docker image:
docker build -t receipt-processor .

Run the Docker container:
docker run -p 8000:8000 receipt-processor

Open Swagger UI:
http://localhost:8000/docs

Run Tests :

Run test locally:
pytest

Run tests in Docker:
docker run -it receipt-processor pytest
