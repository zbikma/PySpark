from setup_pyspark import setup_pyspark
from pyspark.ml.feature import MinMaxScaler
from pyspark.ml.linalg import Vectors
import numpy as np
from pyspark.sql.functions import min,max,lit,col,to_date,to_timestamp,lower,upper,substring
#setup_pyspark()
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("TextFileToDataFrame").getOrCreate()
df= spark.read.csv("/Users/LearningUser/Documents/Repos/PySpark/SparkMl/ExerciseFiles/Ch01/01_04/employee.txt",header=True)
df.show(5,truncate=False)
df.printSchema()
print(f"item count {df.count()}")
fdf = spark.createDataFrame([(1, Vectors.dense([10.0, 10000.0, 1.0]),),(2, Vectors.dense([20.0, 30000.0, 2.0]),),(3, Vectors.dense([30.0, 40000.0, 3.0]),)], ["id", "features"])
#fdf= spark.createDataFrame([(1,np.array([10.0,10.0]),), (2,np.array([20.0,30.0]),)], ["id","features"])
fdf.show()
feature_scaler = MinMaxScaler(inputCol="features",outputCol="scaled_features")
smodel=feature_scaler.fit(fdf)
sfeatures_df = smodel.transform(fdf)
sfeatures_df.show(3,truncate=False)
fdf.describe().show()
print(smodel.originalMin)
print(smodel.originalMax)

