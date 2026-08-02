# Project Structure

```
Automated-ETL-Data-Pipeline/
│
├── airflow/
│   ├── dags/                  # Airflow DAGs
│   ├── config/                # Airflow configuration
│   ├── docker-compose.yaml    # Docker Compose configuration
│   └── Dockerfile             # Custom Airflow image
│
├── database/
│   └── sql/
│       └── init/              # Database initialization scripts
│
├── docs/                      # Project documentation
├── powerbi/                   # Power BI dashboard (.pbix)
│
├── python/
│   ├── api/                   # API integration
│   ├── config/                # Database configuration
│   ├── database/              # Database operations
│   ├── etl/                   # ETL pipelines
│   ├── mappers/               # Data mapping
│   ├── validators/            # Data validation
│   └── utils/                 # Logging utilities
│
├── retail_dbt/                # dbt project
├── screenshots/               # README images
├── README.md
├── requirements.txt
└── .env.example
```

---

## Folder Description

- **airflow/** – Airflow DAGs, Docker Compose, and Dockerfile.
- **database/** – SQL scripts for schema and table creation.
- **python/** – Python modules for ETL, validation, mapping, and database operations.
- **retail_dbt/** – dbt sources, models, transformations, and tests.
- **powerbi/** – Power BI dashboard.
- **docs/** – Project documentation.
- **screenshots/** – Images used in the README.