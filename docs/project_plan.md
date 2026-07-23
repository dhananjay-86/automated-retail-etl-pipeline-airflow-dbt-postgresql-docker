Business Problem

Imagine you're working in a retail company.

Every day,

the company receives

Orders
Products
Customers

The manager wants a dashboard every morning at 8:00 AM.

Currently,

employees

Download CSVs manually
Clean Excel manually
Import into Power BI manually

This wastes time.

Our goal is

Automate everything.

Data Sources

Write

Orders → Fake Store API

Customers → CSV

Products → CSV
Target
API

↓

Python

↓

PostgreSQL

↓

dbt

↓

Power BI
Tech Stack
Python

PostgreSQL

Airflow

dbt

Power BI

Docker

Git
Task 5

Create

docs/

Architecture.md

Write only this.

Customers CSV
         │
Products CSV
         │
Orders API
         │
         ▼
     Python ETL
         │
         ▼
 PostgreSQL (Raw)
         │
         ▼
      dbt Models
         │
         ▼
 PostgreSQL (Mart)
         │
         ▼
     Power BI

That's it.

No code.

Why are we doing this?

Imagine you're joining TCS.

Your manager says:

Build an ETL pipeline.

Would you immediately start coding?

No.

First, you understand:

What problem are we solving?
Where does the data come from?
Where does it go?
What tools will we use?

That's exactly what you're doing now.