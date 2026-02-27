#dim_candidate
Task 4: GitHub Deliverables
Your repository should include:
 ETL Code (code for Extract, Transform, Load).
 Star Schema Diagram (image + explanation).
 Visualizations (e.g., exported as screenshots).
 README.md explaining your project, setup instructions, and key decisions.
 .gitignore file.


#dim_country
CREATE TABLE dim_country (
    id_country SERIAL PRIMARY KEY,
    country VARCHAR(100) NOT NULL
);

#dim_technology
CREATE TABLE dim_technology (
    id_technology SERIAL PRIMARY KEY,
    technology VARCHAR(100) NOT NULL
);

#dim_seniority
CREATE TABLE dim_seniority (
    id_seniority SERIAL PRIMARY KEY,
    seniority VARCHAR(50) NOT NULL
);

#dim_date
CREATE TABLE dim_date (
    id_date SERIAL PRIMARY KEY,
    application_date DATE NOT NULL,
    year INT NOT NULL,
    month INT NOT NULL,
    quarter INT NOT NULL
);

#FACT TABLE
CREATE TABLE fact_applications (

    id_application SERIAL PRIMARY KEY,

    id_candidate INT NOT NULL,
    id_country INT NOT NULL,
    id_technology INT NOT NULL,
    id_seniority INT NOT NULL,
    id_date INT NOT NULL,

    yoe INT NOT NULL,
    code_challenge_score NUMERIC(3,1) NOT NULL,
    technical_interview_score NUMERIC(3,1) NOT NULL,
    hired INT NOT NULL,

    FOREIGN KEY (id_candidate) 
        REFERENCES dim_candidate(id_candidate),

    FOREIGN KEY (id_country) 
        REFERENCES dim_country(id_country),

    FOREIGN KEY (id_technology) 
        REFERENCES dim_technology(id_technology),

    FOREIGN KEY (id_seniority) 
        REFERENCES dim_seniority(id_seniority),

    FOREIGN KEY (id_date) 
        REFERENCES dim_date(id_date),

    CHECK (code_challenge_score BETWEEN 0 AND 10),
    CHECK (technical_interview_score BETWEEN 0 AND 10),
    CHECK (hired IN (0,1))
);
