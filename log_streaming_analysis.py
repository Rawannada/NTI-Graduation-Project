from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col

# Step 1: Initialize Spark Session with streaming support
spark = SparkSession.builder \
    .appName("Streaming Train Logs Analysis") \
    .getOrCreate()

# Step 2: Read streaming data from HDFS
input_path = "hdfs://localhost:9000/flume/train_output"

df = spark.readStream.text(input_path)

# Step 3: Split log line into fields
split_df = df.select(split(col("value"), " - ").alias("parts"))

logs_df = split_df.select(
    col("parts")[0].substr(8, 20).alias("user"),
    col("parts")[1].substr(9, 10).alias("action"),
    col("parts")[2].substr(9, 20).alias("train"),
    col("parts")[3].substr(9, 10).alias("class"),
    col("parts")[4].substr(7, 15).alias("from_station"),
    col("parts")[5].substr(5, 15).alias("to_station"),
    col("parts")[6].substr(7, 20).alias("date")
)

# Step 4: Basic aggregation analysis
action_count = logs_df.groupBy("action").count()
from_station_count = logs_df.groupBy("from_station").count()
train_usage_count = logs_df.groupBy("train").count()

# Step 5: Write processed streaming logs to HDFS
output_path = "hdfs://localhost:9000/flume/stream_result"

query = logs_df.writeStream \
    .outputMode("append") \
    .format("csv") \
    .option("path", output_path) \
    .option("checkpointLocation", "/tmp/spark_streaming_checkpoint") \
    .start()

# Optional: Print action counts to console
action_query = action_count.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", False) \
    .start()

# Optional: Print from_station counts to console
from_station_query = from_station_count.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", False) \
    .start()

# Optional: Print train usage counts to console
train_usage_query = train_usage_count.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", False) \
    .start()

# Wait for the streams to finish
query.awaitTermination()
action_query.awaitTermination()
from_station_query.awaitTermination()
train_usage_query.awaitTermination()
