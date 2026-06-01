# Business Listings Dashboard

## Tech Stack

* Frontend: React.js
* Backend: FastAPI
* Database: MySQL
* Charts: Recharts

## Features

* City Wise Business Count
* Category Wise Business Count
* Source Wise Distribution
* MySQL Database Integration
* REST APIs using FastAPI
* Interactive Dashboard

## Database Schema

Table: listing_master

Fields:

* id
* business_name
* category
* city
* address
* phone
* source
* created_at

## APIs

### GET /city-wise

Returns city-wise business count.

### GET /category-wise

Returns category-wise business count.

### GET /source-wise

Returns source-wise business count.

## Setup Instructions

### Backend

Install dependencies:

pip install fastapi uvicorn sqlalchemy pymysql pandas

Run:

uvicorn main:app --reload

### Frontend

Install dependencies:

npm install

Run:

npm run dev

## Challenges Faced

* Setting up Python and FastAPI environment
* Connecting MySQL with SQLAlchemy
* Integrating React frontend with FastAPI backend
* Creating dashboard visualizations using Recharts

## Output

A dashboard displaying business analytics through charts and aggregated reports.
