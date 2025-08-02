\# Train Booking Logs Analysis (Streaming)



This project processes real-time train booking logs using Apache Spark Structured Streaming. It reads logs generated continuously by a Python script, streams them via Apache Flume into Hadoop HDFS, and performs live analysis and filtering using Spark.



\## Project Overview



\- A Python script generates train booking logs with user actions.

\- Apache Flume continuously monitors the log file and sends the data to HDFS.

\- Spark Structured Streaming reads the data from HDFS in real-time and performs parsing, aggregation, and filtering.

\- The results are stored in HDFS for further analysis or reporting.



\## Technologies Used



\- Python

\- Apache Flume

\- Apache Hadoop HDFS

\- Apache Spark (Structured Streaming)

\- Jupyter Notebook (optional)



\## File Structure



\- `log\_generator.py`: Generates random train booking logs.

\- `train\_booking.log`: Log file created by the script.

\- `flumeHdfs.conf`: Flume configuration to send log data to HDFS.

\- `log\_streaming\_analysis.py`: Spark streaming job that reads, analyzes, and filters incoming log data.

\- `README.md`: Project description and instructions.



\## How to Run the Project



1\. \*\*Generate Logs\*\*  

&nbsp;  Run the Python script:

python3 log\_generator.py





2\. \*\*Start HDFS\*\*  

Make sure Hadoop services are running and HDFS is ready.



3\. \*\*Run Flume Agent\*\*  

Use the provided configuration: 

flume-ng agent --conf conf --conf-file flumeHdfs.conf --name agent1 -Dflume.root.logger=INFO,console







4\. Run Spark Streaming Analysis  

Submit the Spark streaming script:

spark-submit log\_streaming\_analysis.py







5\. \*\*View Results\*\*  

Processed results are stored in:

hdfs://localhost:9000/flume/stream\_result/ 



\## Output Example



The analysis includes:

\- Count of each action type (`book`, `cancel`, `update`)

\- Most active departure stations

\- Most used trains





