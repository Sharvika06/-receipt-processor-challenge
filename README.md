# 🧾 Receipt Processor API

A FastAPI-based application for processing receipts and calculating points.

---

## 🚀 Features
- 📝 Submit receipts for processing.
- 📊 Retrieve points for processed receipts.
- 📜 Swagger UI and OpenAPI documentation.

---

## 🛠️ Technologies
- **Python 3.10**
- **FastAPI**
- **Pydantic**
- **Docker** (optional)

---

## 💻 Run Locally

1️⃣ Clone the repository:
git clone <repo-url>
cd receipt-processor-challenge

2️⃣ Create a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install dependencies:
pip install -r requirements.txt

4️⃣ Start the server:
uvicorn app:app --reload --host 0.0.0.0 --port 8000

5️⃣ Open Swagger UI:
Visit http://localhost:8000/docs

🐳 Run with Docker
1️⃣ Build the Docker image:
docker build -t receipt-processor .

2️⃣ Run the Docker container:
docker run -p 8000:8000 receipt-processor

3️⃣ Open Swagger UI:
Visit http://localhost:8000/docs

🧪 Run Tests
Run tests locally:
pytest

Run tests in Docker:
docker run -it receipt-processor pytest
