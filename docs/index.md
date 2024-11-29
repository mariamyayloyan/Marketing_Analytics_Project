# Welcome to the Subscription Management System

This project is designed to handle subscription data management, including CRUD operations for customers, plans, applications, and more. It uses a combination of different services to interact with a PostgreSQL database and provide a user-friendly experience. Below is an overview of the main services in this project:

## Services

### `Database`
- **Postgres database**: The data is stored in a PostgreSQL database, which provides a reliable and scalable solution for managing customer, subscription, and other related data.

### `API`
- **FastAPI**: The API layer connects with the PostgreSQL database, handling CRUD operations for customers, subscriptions, plans, and more. FastAPI provides a fast and modern framework for building the API.

### `App`
- **Streamlit**: The Streamlit app connects to the FastAPI and provides a web interface to interact with the data. It is used for displaying data and enabling user interaction.

### `Pgadmain`
- **Pgadmain**: This is a user interface (UI) that shows you the data you have inserted. It acts as a frontend for administrators or users to manage the subscriptions and other related data stored in the database.

### `Docs`
- **MkDocs**: MkDocs is used to document the codebase and provide an easy-to-read set of documentation for the project. It automatically generates the documentation from docstrings and Markdown files.

---

## Getting Started

To get started with the project, follow these steps:

1. **Install dependencies**: Ensure you have all the required dependencies installed. You can use the `requirements.txt` file to install them.
2. **Set up the database**: Follow the instructions to set up PostgreSQL and ensure the database schema is created correctly.
3. **Run the FastAPI server**: Use FastAPI to run the backend API and connect it to the database.
4. **Launch the Streamlit app**: Once the API is running, start the Streamlit app to interact with the data.
