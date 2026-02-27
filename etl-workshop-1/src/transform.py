#Convert date

df["Application Date"] = pd.to_datetime(df["Application Date"])

#Business rule
df["hired"] = (
    (df["Code Challenge Score"] >= 7) &
    (df["Technical Interview Score"] >= 7)
).astype(int)
df["hired"].value_counts()
#Creating dimensions (with surrogate keys)


#dim_candidate
dim_candidate = df[["First Name","Last Name","Email"]].drop_duplicates().reset_index(drop=True)
dim_candidate["id_candidate"] = dim_candidate.index + 1

#dim_country
dim_country = df[["Country"]].drop_duplicates().reset_index(drop=True)
dim_country["id_country"] = dim_country.index + 1
dim_country = df[["Country"]].drop_duplicates().reset_index(drop=True)
dim_country["id_country"] = dim_country.index + 1

#dim_technology
dim_technology = df[["Technology"]].drop_duplicates().reset_index(drop=True)
dim_technology["id_technology"] = dim_technology.index + 1

#dim_seniority
dim_seniority = df[["Seniority"]].drop_duplicates().reset_index(drop=True)
dim_seniority["id_seniority"] = dim_seniority.index + 1
dim_date = df[["Application Date"]].drop_duplicates().reset_index(drop=True)

#dim_date
dim_date["year"] = dim_date["Application Date"].dt.year
dim_date["month"] = dim_date["Application Date"].dt.month
dim_date["quarter"] = dim_date["Application Date"].dt.quarter

dim_date["id_date"] = dim_date.index + 1

#FACT TABLE
fact = df.merge(dim_candidate, on=["First Name","Last Name","Email"])
fact = fact.merge(dim_country, on="Country")
fact = fact.merge(dim_technology, on="Technology")
fact = fact.merge(dim_seniority, on="Seniority")
fact = fact.merge(dim_date, on="Application Date")

fact_final = fact[[
    "id_candidate",
    "id_country",
    "id_technology",
    "id_seniority",
    "id_date",
    "Yoe",
    "Code Challenge Score",
    "Technical Interview Score",
    "hired"
]]

fact_final.columns = [
    "id_candidate",
    "id_country",
    "id_technology",
    "id_seniority",
    "id_date",
    "yoe",
    "code_challenge_score",
    "technical_interview_score",
    "hired"
]