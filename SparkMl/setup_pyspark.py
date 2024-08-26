import os
import subprocess
from dotenv import load_dotenv


def setup_pyspark():
    load_dotenv()
    java_home = os.getenv("JAVA_HOME")
    spark_home = os.getenv("SPARK_HOME")
    if not java_home or not spark_home:
        raise EnvironmentError("JAVA_HOME or SPARK_HOME is not set in the .env file")
    # Set the environment variables
    os.environ["JAVA_HOME"] = java_home
    os.environ["SPARK_HOME"] = spark_home
    os.environ["PATH"] += os.pathsep + os.path.join(os.environ["SPARK_HOME"], "bin")

    # Verify the setup by printing the environment variables (optional)
    print("JAVA_HOME:", os.environ["JAVA_HOME"])
    print("SPARK_HOME:", os.environ["SPARK_HOME"])
    print("PATH:", os.environ["PATH"])

if __name__ == "__main__":
    setup_pyspark()