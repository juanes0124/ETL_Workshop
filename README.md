# ETL_Workshop

## Project Objective


## Star Schema Design

- Star Schema was chosen to optimize analytical queries.
- Surrogate keys were created for each dimension.
- Natural keys from the CSV were not used as primary keys.


## Grain definition

The grain of the Fact Table is defined as one row per candidate application.


## ETL logic

### Extract
- Loaded CSV file
- Validated data types

### Transform
- Applied HIRED business rule
- Handled null values
- Generated surrogate keys
- Built Fact Table

### Load
- Created tables in PostgreSQL
- Inserted dimension tables first
- Inserted Fact Table
- Ensured referential integrity


## Data quality assumptions

- Null values were removed.
- Scores were validated as numeric.
- Country and Technology fields were normalized.


## How to run the project
1. Clone repository
2. Install requirements
3. Upload CSV to data/raw
4. Run ETL notebook
5. Connect Power BI to PostgreSQL

## Example outputs
- Python
- Google Colab
- PostgreSQL
- SQL
- Power BI
