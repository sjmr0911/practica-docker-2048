import time
from pyspark.sql.functions import explode, split, lower, trim, col

def word_count_df(spark, input_path, output_path):
    start_time = time.time()

    df = spark.read.text(input_path)
    word_counts = df.select(explode(split(lower(col("value")), "\\s+")).alias("word")) \
                    .filter(trim(col("word")) != "") \
                    .groupBy("word") \
                    .count() \
                    .orderBy(col("count").desc())

    word_counts.write.mode("overwrite").csv(output_path, header=True)
    return time.time() - start_time
