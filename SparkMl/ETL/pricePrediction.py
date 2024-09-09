from SparkML.pysparkSetup import setup_pyspark
from pyspark.sql import functions as F
import os 
from pyspark.sql.functions import col,count,when, isnan
from pyspark.sql.types import DoubleType,FloatType

from pyspark.sql import SparkSession

def count_missing_values(df):
    exprs = []
    for col_name in df.columns:
        # Check column data type
        dtype = df.schema[col_name].dataType
        # Apply conditional checks based on the data type
        if isinstance(dtype, (FloatType, DoubleType)):
            # For floating-point types, check for both NaN and Null
            expr = F.count(F.when(F.isnan(F.col(col_name)) | F.col(col_name).isNull(), col_name)).alias(col_name)
        else:
            # For non-floating types, just check for Null
            expr = F.count(F.when(F.col(col_name).isNull(), col_name)).alias(col_name)
        exprs.append(expr)

    # Compute the counts of missing values for each column
    missing_counts_df = df.select(*exprs)
    return missing_counts_df

spark = SparkSession.builder.appName("TextFileToDataFrame").getOrCreate()

# initialize spark session
spark = SparkSession.builder.appName("TextFileToDataFrame").getOrCreate()
data_path="SparkML/ETL/housing.csv"

full_path = os.path.join(os.getcwd(),data_path)
print("full path to csv:",full_path)
print("does the file exist:",os.path.exists(full_path))
df = spark.read.csv(data_path,header=True,inferSchema= True)
df.printSchema()

df.show(10)
missing = count_missing_values(df)
missing.show()
spark.stop()