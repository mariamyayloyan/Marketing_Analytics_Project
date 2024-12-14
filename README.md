# Marketing Analytics Project (Group 2)

# Overview
This Marketing analytics service (Loyalytics) helps subscription-based applications improve customer retention by analyzing customer data and generating actionable insights. The service categorizes customers, identifies trends, and provides recommendations to enhance customer loyalty and reduce churn.

This demo project uses generated data from a popular music streaming service, Spotify, to showcase how data analysis can help businesses improve customer retention strategies.

## Installation

### Prerequisites
Before getting started, ensure you have the following prerequisites installed:
- Docker
- Docker Compose

### Clone the repository

```bash
git clone https://github.com/mariamyayloyan/Marketing_Analytics_Project.git
```
### Build the Docker containers
```bash
docker-compose up --build
```


# Access the Application

After building the docker containers each component of the application can be accessed with the following URLs:

Frontend UI: http://localhost:8501

The user interface where businesses can upload their customer data and view the analysis results.

Backend API: http://localhost:8008 or  [Swagger UI](http://localhost:8008/docs)

The API endpoints for interacting with the service. 

Database Management (pgAdmin): http://localhost:5050

An interface for managing the PostgreSQL database.

- Email: admin@admin.com

- Password: admin

## Project structure

```bash
.
├── .github
│   └── workflows
│       └── ci.yaml                        # Continuous integration configuration for automated testing
├── .idea
│   └── inspectionProfiles                 # IDE inspection profiles
├── .gitignore                             # Specifies files and directories to ignore in Git
├── Marketing_Analytics_Project.iml        # Project configuration file 
├── misc.xml                               # Miscellaneous configuration file (IDE-specific)
├── modules.xml                            # Project modules configuration (IDE-specific)
├── vcs.xml                                # Version control system configuration (IDE-specific)
├── app_components
│   └── back
│       ├── .env                           # Environment variables for backend
│       ├── Dockerfile                     # Docker configuration for backend service
│       ├── __init__.py                    # Marks this directory as a Python package
│       ├── database.py                    # Database connection and setup
│       ├── main.py                        # Main backend entry point (API setup)
│       ├── models.py                      # Database models and schema definitions
│       ├── requirements.txt               # Backend dependencies
│       └── schema.py                      # Pydantic models for API requests and responses
│   └── ds
│       ├── __pycache__                    # Compiled Python files 
│       ├── .env                           # Environment variables for data science 
│       ├── Clustering.py                  # Clustering models and related scripts
│       ├── Dockerfile                     # Docker configuration for data science services
│       ├── __init__.py                    # Marks this directory as a Python package
│       ├── cluster_summary.csv            # Summary of clustering results
│       ├── database.py                    # Database connection for data science components
│       ├── final_model.py                 # Final data science model 
│       ├── models.py                      # Machine learning models and training code
│       ├── requirements.txt               # Data science dependencies
│   └── etl
│       ├── Data                           # Raw data directory for ETL processing
│       ├── Database                       # Database setup and schema for ETL processes
│       ├── .env                           # Environment variables for ETL processes
│       ├── Dockerfile                     # Docker configuration for ETL service
│       ├── __init__.py                    # Marks this directory as a Python package
│       ├── etl.py                         # ETL pipeline code 
│       └── requirements.txt               # ETL dependencies
│   └── front
│       ├── pages                          # Frontend pages (for web UI)
│       ├── Dockerfile                     # Docker configuration for frontend service
│       ├── __init__.py                    # Marks this directory as a Python package
│       ├── front.py                       # Main entry point for frontend (UI logic)
│       └── requirements.txt               # Frontend dependencies 
├── docker-compose.yaml                   # Docker Compose configuration for setting up multi-container environment
├── docs
```

## Project parts:
- **Backend**: Manages the API requests and database interactions.
- **Frontend**: Provides the user interface for system interaction.
- **Data Science**: Analyzes and models data to provide insights for decision-making.
  
## Swagger screenshots

![localhost_8008_docs](https://github.com/user-attachments/assets/7dc2d85c-9d1c-429b-9d66-a124c5775abc)

## UI screenshots

![localhost_8501_ (1)](https://github.com/user-attachments/assets/6f886766-1769-4ba7-a2a9-b1d90477da0e)

![localhost_8501_](https://github.com/user-attachments/assets/19ac3440-5b04-4f15-9281-67c9ce8d20a0)

![image](https://github.com/user-attachments/assets/1e2ea397-2f90-43d4-b06d-327b0c5cc5d9)

![image](https://github.com/user-attachments/assets/ee962b3f-ebab-47b1-8050-69e0135f860b)

![image](https://github.com/user-attachments/assets/d1051085-cbe8-42fc-9fed-7af7aec242ae)

![image](https://github.com/user-attachments/assets/4db81487-cf12-46a6-9da0-e8e0071fd107)



## Other links:
- [Project Roadmap](https://miro.com/app/board/uXjVLNgys98=/)
- [Frontend UI Prototype](https://www.canva.com/design/DAGUmLz2NaA/52-N9z3R2h_vcs9RnpEqzQ/edit?utm_content=DAGUmLz2NaA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
  
