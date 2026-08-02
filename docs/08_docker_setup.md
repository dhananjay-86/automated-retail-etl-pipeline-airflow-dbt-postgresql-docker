# Docker Setup

## Overview

The project uses Docker to provide a consistent environment for Apache Airflow and PostgreSQL.

---

## Services

| Service | Purpose |
|---------|---------|
| PostgreSQL | Stores raw and analytics data |
| Apache Airflow | Orchestrates the ETL workflow |

---

## Start Containers

```bash
docker compose up -d
```

---

## Stop Containers

```bash
docker compose down
```

---

## View Running Containers

```bash
docker ps
```

---

## Access Airflow

```
http://localhost:8080
```

---

## Access PostgreSQL

```
Host: localhost
Port: 5433
Database: retail_analytics_db
```