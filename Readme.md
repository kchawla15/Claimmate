# ClaimMate NZ

ClaimMate NZ is a Django-based web application designed to help users track receipts and warranties. Users can upload purchase records, monitor warranty expiry, view dashboards, calculate budgets, and generate downloadable PDF reports. This project was developed as part of the **SOFT806 CI/CD assignment**.



## 🔧 Features

- User registration and authentication  
- Upload receipts with product name, warranty period, and purchase price  
- Dashboard showing remaining warranty and product summary  
- Budget calculator by date range  
- Generate PDF reports of saved warranties  
- Dockerized for portable deployment  
- CI/CD pipeline using GitHub Actions and deployed on Microsoft Azure  



## 🧰 Tech Stack

- **Backend:** Python 3.10+, Django 4.x  
- **Database:** SQLite  
- **DevOps:** Docker, GitHub Actions, Azure App Service  
- **Planning Tools:** Trello (Agile), Jenkins (optional CI)  



## 🚀 Deployment (CI/CD Pipeline)

CI/CD is handled via **GitHub Actions**, with the following phases:

1. **Build** – Docker container is created on push to the main branch  
2. **Test** – Azure performs internal validation during deployment  
3. **Deploy** – App is automatically deployed to Azure App Service

✅ *Note: Explicit unit testing isn’t configured. Azure’s internal build validation ensures the app is functional before going live.*



## 📁 Project Structure

.github/workflows/        - CI/CD GitHub Actions YAML
Claimmate/                - Main Django app
Dockerfile                - Docker build file
Procfile                  - Azure deployment instructions
requirements.txt          - Python dependencies
.env.example              - Sample environment variables
SQL-Script-DDL.txt        - DB schema setup
SQL-Script-DML.txt        - Sample data for testing


## 🛠️ Environment Variables

The app requires a `.env` file in the root directory. An example `.env.example` is included:

```env
SECRET_KEY=django-insecure-a1rdp*@i@+rgnzv9kz@61txv*r-qlj!t5p0lvw)z7#i5@cxxrt
DEBUG=True
```

## 📦 Local Development Setup

bash
git clone https://github.com/kchawla15/Claimmate.git  
cd Claimmate  

# Create virtual environment  
python -m venv venv  
source venv/bin/activate   # Windows: venv\Scripts\activate  

# Install dependencies  
pip install -r requirements.txt  

# Apply migrations  
python manage.py migrate  

# Start the development server  
python manage.py runserver  


## 📷 Evidence & Screenshots

All screenshots and supporting documentation are provided in the Word file:
📄 Assignment1_Screenshots.docx
Includes:

* Azure deployment status
* GitHub Actions build logs
* SQL script usage
* Trello board with sprint tasks
* Project structure and .env setup


## 📂 SQL Scripts

* **SQL-Script-DDL.txt** – Creates the database schema for warranty tracking
* **SQL-Script-DML.txt** – Inserts sample data for testing


## 📅 Trello Agile Board

Used for sprint planning, backlog management, and tracking:
🔗 [Trello Board – ClaimMate CI/CD](https://trello.com/b/qHI8SydJ/ci-cd2025claimmate)


## 📑 License / Attribution

This project was created for **educational use** as part of the SOFT806 CI/CD coursework.
⚠️ Not intended for production deployment.


## 🔐 Security Disclaimer

**Warning:** The SECRET_KEY shown is for academic review only.
Do *not* commit secrets to public repositories in real-world scenarios.