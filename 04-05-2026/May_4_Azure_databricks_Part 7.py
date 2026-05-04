import dlt
from pyspark.sql.functions import col, upper, sum, count


@dlt.table(name="bronze_patient_visits_new")
def bronze_patient_visits():
    data = [
        (101,"Arjun Reddy","Hyderabad","Cardiology",5000,1),
        (102,"Sneha Kapoor","Delhi","Orthopedics",3000,2),
        (103,"Rahul Sharma","Mumbai","Dermatology",1500,1),
        (104,"Priya Nair","Bangalore","Cardiology",5000,2),
        (105,"Vikram Singh","Chennai","Neurology",7000,1),
        (106,"Ananya Das","Kolkata","Orthopedics",3000,3),
        (107,"Karan Patel","Ahmedabad","Cardiology",5000,1),
        (108,"Meera Iyer","Bangalore","Dermatology",1500,2)
    ]

    columns = [
        "visit_id",
        "patient_name",
        "city",
        "department",
        "consultation_fee",
        "tests_count"
    ]

    return spark.createDataFrame(data, columns)



@dlt.table(name="silver_patient_visits_new")
def silver_patient_visits():
    df = dlt.read("bronze_patient_visits_new")

    return df.select(
        col("visit_id"),
        col("patient_name"),
        col("city"),
        upper(col("department")).alias("department"),
        col("consultation_fee"),
        col("tests_count"),
        (col("tests_count") * 2000).alias("test_cost"),
        (col("consultation_fee") + (col("tests_count") * 2000)).alias("total_bill")
    ).filter(col("consultation_fee") > 0)


@dlt.table(name="gold_hospital_summary_new")
def gold_hospital_summary():
    df = dlt.read("silver_patient_visits_new")

    return df.groupBy("department").agg(
        count("*").alias("total_patients"),
        sum("tests_count").alias("total_tests"),
        sum("total_bill").alias("total_revenue")
    )