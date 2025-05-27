# Mental-health-Ci-cd-project
# Mental Health Web Application – CI Setup with Jenkins and Docker

This project implements a **Continuous Integration (CI)** pipeline for a Mental Health web application using **Git**, **Jenkins**, **Docker**, and **Docker Compose**.

## 🧠 Project Overview

The goal of this project is to automate the building and testing of a web-based mental health assessment application. Using Jenkins and Docker, the pipeline automatically builds a containerized version of the app whenever changes are pushed to GitHub.

> **Note:** This project includes only CI (Continuous Integration). Continuous Deployment (CD) is planned for future implementation.

---

## 📦 Tech Stack

- **Frontend / Backend**:  Django
- **Version Control**: Git & GitHub
- **CI Tool**: Jenkins
- **Containerization**: Docker
- **Multi-Container Management**: Docker Compose
- **Persistence**: Docker Volumes

---

## ⚙️ Features Implemented

- GitHub webhook triggers Jenkins job on every push
- Jenkins pulls latest code and builds Docker image
- Docker Compose runs the app in isolated containers
- Build logs and status visible in Jenkins dashboard
- Volume mapping for persistent storage

---

## 📁 Project Structure

mental-health-app/
├── app/ # Application source code
│ ├── static/
│ ├── templates/
│ └── main.py
├── Dockerfile # Container build instructions
├── docker-compose.yml # Multi-container configuration
├── jenkins/
│ └── Jenkinsfile # CI pipeline script (optional)
├── .env # Environment variables
└── README.md


---

## 🚀 How to Run Locally

### Prerequisites

- Docker & Docker Compose installed
- Jenkins installed and running
- Git

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/mental-health-ci.git
   cd mental-health-ci
docker-compose up --build


