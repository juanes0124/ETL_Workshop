
#dim_candidate

dim_candidate.columns = [
    "first_name",
    "last_name",
    "email",
    "id_candidate"
]
#dim_country
dim_country.columns = [
    "country",
    "id_country"
]
#dim_technology
dim_technology.columns = [
    "technology",
    "id_technology"
]
#dim_seniority
dim_seniority.columns = [
    "seniority",
    "id_seniority"
]
#dim_date
dim_date.columns = [
    "application_date",
    "year",
    "month",
    "quarter",
    "id_date"
]

dim_candidate.to_sql("dim_candidate", engine, if_exists="append", index=False)
dim_country.to_sql("dim_country", engine, if_exists="append", index=False)
dim_technology.to_sql("dim_technology", engine, if_exists="append", index=False)
dim_seniority.to_sql("dim_seniority", engine, if_exists="append", index=False)
dim_date.to_sql("dim_date", engine, if_exists="append", index=False)

fact_final.to_sql("fact_applications", engine, if_exists="append", index=False)