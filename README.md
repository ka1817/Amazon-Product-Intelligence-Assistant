## 🛍️ Amazon Product Intelligence Assistant

---
## ❓ Problem Statement

Searching for the right product among millions of listings on e-commerce platforms like Amazon can be overwhelming. Traditional keyword-based search often fails to understand user intent or context. This project addresses that challenge by building a **Retrieval-Augmented Generation (RAG)** system that enables users to query product data in natural language.

By integrating query rewriting, vector similarity search, and large language models (LLMs), the assistant refines ambiguous queries, retrieves the most relevant product information, and generates intelligent, context-aware responses—enhancing the shopping and research experience.

---

- Project overview
- Folder structure
- Setup instructions
- Git commands
- Docker usage
- GitHub Actions for CI/CD
- EC2 deployment steps

---

```markdown
# 🛍️ Amazon Product Intelligence Assistant

A FastAPI-powered web app that allows users to query a product dataset using **natural language**. This system refines queries, retrieves relevant product data using vector similarity search (FAISS), and generates contextually accurate answers using **Large Language Models** (LLMs).

---

## 🚀 Features

- 🔍 Query Rewriting using LLMs (via Groq’s `gemma2-9b-it`)
- 📚 Data Ingestion & Preprocessing from a CSV file
- 🧠 Vector Search with FAISS + HuggingFace Embeddings
- 💬 Answer Generation with LLMs (Groq’s `llama-3.3-70b-versatile`)
- 🌐 FastAPI Backend (running on `http://localhost:8000`)
- 🎨 HTML/CSS Frontend
- 🐳 Containerized with Docker
- 🛠️ CI/CD using GitHub Actions
- ☁️ Deployment on Amazon EC2

---

## 📁 Project Structure

```
Amazon-Product-Intelligence-Assistant/
│
├── .github/workflows/        # GitHub Actions for CI/CD
│   └── cicd.yml
│
├── data/                     # CSV and source data
│
├── src/                      # Core application logic
│   ├── __init__.py
│   ├── data_ingestion.py
│   ├── data_preprocess.py
│   ├── query_rewritting.py
│   └── retrival_generation.py
│
├── static/css/               # Styling for frontend
│   └── style.css
│
├── templates/                # Jinja2 HTML templates
│   └── index.html
│
├── .dockerignore
├── .env
├── .gitignore
├── Dockerfile                # Docker build instructions
├── main.py                   # FastAPI entry point
├── README.md
├── requirements.txt          # Python dependencies
└── venv/                     # Virtual environment
```

---

## 🧪 Local Development Setup

```bash
# Clone the repository
git clone https://github.com/ka1817/Amazon-Product-Intelligence-Assistant.git
cd Amazon-Product-Intelligence-Assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload --port 8000
```

Access at: [http://localhost:8000](http://localhost:8000)

---

## 🐳 Docker Commands

### Build the Docker Image

```bash
docker build -t pranavreddy123/product-assistent .
```

### Run the Container

```bash
docker run -d -p 8000:8000 pranavreddy123/product-assistent
```

### Push to DockerHub

```bash
# Login to DockerHub
docker login

# Tag and push
docker push pranavreddy123/product-assistent
```

---

## 🔄 CI/CD with GitHub Actions

Located in `.github/workflows/cicd.yml`  
Triggers on push to main. Steps include:

- ✅ Install dependencies
- ✅ Run tests (optional)
- ✅ Build Docker image
- ✅ Push to DockerHub

---

## ☁️ Deployment on Amazon EC2

### 1. Launch EC2 Instance (Ubuntu 20.04)

### 2. SSH into your instance

```bash
ssh -i "your-key.pem" ubuntu@your-ec2-ip
```

### 3. Install Docker

```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
```

### 4. Pull and Run Docker Image

```bash
docker pull pranavreddy123/product-assistent
docker run -d -p 80:8000 pranavreddy123/product-assistent
```

Access your app via `http://<your-ec2-public-ip>`

---

## 🔗 Repository & Image

- **GitHub Repo**: [Amazon-Product-Intelligence-Assistant](https://github.com/ka1817/Amazon-Product-Intelligence-Assistant)
- **DockerHub**: [`pranavreddy123/product-assistent`](https://hub.docker.com/r/pranavreddy123/product-assistent)

---

## ✨ Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

[MIT](LICENSE)

```

---

Developed By Pranav Reddy