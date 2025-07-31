import time

def word_count_rdd(sc, input_path, output_path):
    start_time = time.time()

    lines = sc.textFile(input_path)
    words = lines.flatMap(lambda line: line.split()) \
                 .map(lambda word: (word.lower(), 1)) \
                 .reduceByKey(lambda a, b: a + b) \
                 .sortBy(lambda x: x[1], ascending=False)

    words.saveAsTextFile(output_path)
    return time.time() - start_time
