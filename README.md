# Data Engineering Coding Challenge

## Project Overview

This project was developed as a solution to the Data Engineering Coding Challenge. The project focuses on creating a robust data pipeline that ingests data, processes it, and makes it available through SQL queries and API endpoints.

## Project Structure

project/
├── main.py               # Entry point for FastAPI application
├── db/
│   ├── database.py       # Database connection and session configuration
│   └── models.py         # SQLAlchemy models for the database tables
├── routes/
│   ├── data_upload.py    # Routes for uploading data
├── env/                  # Virtual environment folder in gitignore file
├── requirements.txt/                  
├── pdf_solution requirements files/ #take a look at the sql outputs, edr in dbeaver and the fastapi ui. 
└── README.md             # Project documentation

## Requirements

run in your terminal: pip install -r requirements.txt

contains the next requirements:

Python 3.7 or later
FastAPI
SQLite
SQLAlchemy
Pandas
DBeaver (optional for database visualization)

## Installation

Clone the repository:
git clone https://github.com/CristianCaro-portfolio/CodeChallengeGlobant.git

cd project

Create and activate a virtual environment:
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

Install dependencies in the previous list of requirements

## Run the application:

uvicorn main:app --reload

## Usage

1. Upload Data

Upload data by sending CSV files to the API endpoints. Supported endpoints:

/upload/departments
/upload/jobs
/upload/hired_employees

You can use a tool like curl to upload files:

curl -X 'POST' \
  'http://localhost:8000/upload/departments' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@departments.csv;type=text/csv'

2. SQL Queries

The solution includes SQL queries to meet the coding challenge requirements, such as:

Counting hires per department and job for 2021, grouped by quarter.
Identifying departments that hired more employees than the average in 2021.
Refer to the queries.sql file for detailed queries also to see the output please refer to the pdf files in the sql_solution_requirements folder.

## Project Components

1. Database Models

The database consists of three main tables:

departments
jobs
hired_employees

2. API Endpoints

Implemented using FastAPI, the project provides endpoints to upload data and perform operations on the data using Python and SQLAlchemy.

3. Data Processing

Pandas is used to handle and preprocess data before inserting it into the database, ensuring data validation and consistency, bearing in mind that file sizes are small.


## Future Improvements

Add more validations for data input.
Implement error-handling improvements.
Extend the API with more endpoints for data analysis.
Migrate to a cloud-based database for scalability.
In case of Big Data, change pandas with spark.