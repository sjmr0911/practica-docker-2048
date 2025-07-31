from wordcount_rdd import word_count_rdd
from wordcount_dataframe import word_count_df
from pyspark.sql import SparkSession

# Inicialización de SparkSession
spark = SparkSession.builder \
    .appName("WordCountRDDvsDataFrame") \
    .getOrCreate()

sc = spark.sparkContext

if __name__ == "__main__":
    input_file = "dataset.txt"
    output_rdd = "resultados/output_rdd"
    output_df = "resultados/output_dataframe"

    print("\n--- Ejecutando Word Count con RDDs ---")
    rdd_time = word_count_rdd(sc, input_file, output_rdd)
    print(f"✅ Tiempo RDD: {rdd_time:.2f} segundos")

    print("\n--- Ejecutando Word Count con DataFrames ---")
    df_time = word_count_df(spark, input_file, output_df)
    print(f"✅ Tiempo DataFrame: {df_time:.2f} segundos")

    print(f"\n⚡️ Speedup (RDD / DF): {rdd_time / df_time:.2f}x")

    spark.stop()

