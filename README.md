# 🏭 Smart Manufacturing Machines Efficiency Prediction – Advanced MLOps Project

![MLOps](https://img.shields.io/badge/MLOps-Kubernetes-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-success)
![Python](https://img.shields.io/badge/Python-3.10%2B-brightgreen)
![License](https://img.shields.io/badge/License-GPL--3.0-orange)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

End-to-end MLOps project for predicting the efficiency of smart manufacturing machines using advanced machine learning pipelines. This repository features data processing, model training, containerization, CI/CD with Jenkins, Kubernetes deployment, and a web application for real-time efficiency inference. Built for scalability, robustness, and production-readiness in industrial AI.

> 📁 **Repository:** `Advanced_Mlops_Project7_Smart_Manufacturing_Machines_Efficiency_Predection`

---

## 🚀 Project Highlights

- 🏭 **Industrial AI:** Predicts operational efficiency of manufacturing machines from IoT/process data
- 🛠️ **Modular MLOps Workflow:** Clean separation of code, data, pipeline, and deployment manifests
- 🐳 **Dockerized:** Easily build, test, and deploy as containers
- ☸️ **Kubernetes-Ready:** Includes manifests for scalable production deployment
- 🔄 **CI/CD with Jenkins:** Automated build, test, and deployment pipeline
- 🌐 **Web App:** User interface for live efficiency prediction

---

## 🧠 Technical Stack

### 🛠️ Core Technologies
![Python](https://img.shields.io/badge/Python-3.10%2B-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deploy-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-success)
![Flask](https://img.shields.io/badge/Flask-WebApp-lightgrey)

### 📦 Libraries & Utilities
- Pandas, NumPy, Scikit-learn (ML/data)
- Flask (web app)
- YAML (config management)
- HTML/CSS (UI)
- Jupyter Notebook (EDA, prototyping)

---

## 🏗️ Project Structure

```bash
Advanced_Mlops_Project7_Smart_Manufacturing_Machines_Efficiency_Predection/
├── DATA/
│   └── data.csv                     # Manufacturing/IoT efficiency dataset
├── CODE/
│   ├── manifests/
│   │   ├── deployment.yaml          # Kubernetes deployment manifest
│   │   └── service.yaml             # Kubernetes service manifest
│   ├── notebook/
│   │   └── notebook.ipynb           # EDA & prototyping
│   ├── pipeline/
│   │   ├── __init__.py
│   │   └── training_pipeline.py     # ML pipeline orchestration
│   ├── src/
│   │   ├── __init__.py
│   │   ├── custom_exception.py
│   │   ├── data_processing.py
│   │   ├── logger.py
│   │   └── model_training.py
│   ├── static/
│   │   └── style.css                # Web app styling
│   ├── templates/
│   │   └── index.html               # Web app template
│   ├── Dockerfile                   # Docker build file
│   ├── Jenkinsfile                  # Jenkins pipeline for CI/CD
│   ├── application.py               # Flask app entry point
│   ├── requirements.txt             # Python dependencies
│   ├── setup.py                     # Package info
│   ├── LICENSE
│   ├── PDF and NOTES.pdf            # Documentation/workflow
│   └── README.md
├── SETUP INSTRUCTIONS               # Deployment & usage guidance
├── .gitignore
```

---

## ⚡ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/mdzaheerjk/Advanced_Mlops_Project7_Smart_Manufacturing_Machines_Efficiency_Predection.git
cd Advanced_Mlops_Project7_Smart_Manufacturing_Machines_Efficiency_Predection/CODE
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the ML pipeline
```bash
python pipeline/training_pipeline.py
```

### 5. Launch the web application
```bash
python application.py
```
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🐳 Docker, Kubernetes & CI/CD

- **Docker:**  
  Build and run the project in a container using the provided `Dockerfile`.

- **Kubernetes:**  
  Deploy on a Kubernetes cluster with `manifests/deployment.yaml` and `manifests/service.yaml`.

- **Jenkins:**  
  Use the `Jenkinsfile` for CI/CD automation of build, test, and deployment.

- **Setup Guidance:**  
  See `SETUP INSTRUCTIONS` and `PDF and NOTES.pdf` for deployment and configuration help.

---

## 📊 Example Use Cases

- **Machine Efficiency Prediction:** Real-time prediction of manufacturing machine performance and maintenance needs
- **Industrial Web App Demo:** UI for operational staff to upload process data and get predictions
- **MLOps Showcase:** Demonstrates CI/CD, containerization, and scalable cloud deployment

---

## ✍️ Author

**Mohammed Zaheeruddin**  
🎓 First-Year B.Tech Student | AI/ML & GenAI Enthusiast  
🏫 Shetty Institute of Technology, Gulbarga  
📧 info.zaheerjk@gmail.com

---

## 📜 License

This project is licensed under the **GPL-3.0 License** – see the LICENSE file for details.

---

#### Key Features:
1. Modular, end-to-end MLOps pipeline for smart manufacturing
2. CI/CD with Jenkins, scalable deployment with Docker & Kubernetes
3. User-friendly web interface for real-time efficiency prediction
4. Designed for industrial, research, and educational adaptation
