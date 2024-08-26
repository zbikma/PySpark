from setup_pyspark import setup_pyspark
setup_pyspark()
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("TextFileToDataFrame").getOrCreate()
df= spark.read.csv("SparkMl/ExerciseFiles/Ch01/01_04/employee.txt",header=True)
df.show(5,truncate=False)
