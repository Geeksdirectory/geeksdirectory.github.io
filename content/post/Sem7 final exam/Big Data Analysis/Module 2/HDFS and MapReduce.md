![[Pasted image 20241106170212.png]]



### What is HDFS?
   - **Hadoop Distributed File System (HDFS)** is the ==primary storage system== used by Hadoop to store large datasets in a distributed manner across multiple nodes in a ==cluster==.
   - ==Inspired by Google File System== (GFS), HDFS is ==designed for high fault tolerance, scalability, and support for high-throughput data access==.
   - It handles data storage needs for applications that process vast amounts of structured and unstructured data, making it ideal for Big Data processing.

---

#### Key Characteristics of HDFS
   - **Distributed Storage**: HDFS splits large files into smaller blocks (default size is 128 MB or 64 MB) and distributes these blocks across multiple nodes.
   - **Fault Tolerance**: Data blocks are replicated across different nodes to prevent data loss in case of hardware failures.
   - **High Throughput**: Optimized for large, sequential data reads and batch processing, rather than low-latency access to small data files.
   - **Scalability**: Scales horizontally across thousands of nodes without requiring major architectural changes.
   - **Write Once, Read Many**: Files are typically written once and read many times, allowing for efficient and simple data access patterns in analytics.

---

#### **HDFS Architecture**
![[Pasted image 20241106175519.png]]
HDFS has a ==master-slave architecture== with two main components:

##### 1. **NameNode** master node
   - **Role**: Acts as the ==master node in HDFS==, ==managing== the file system ==metadata==.
   - **Responsibilities**:
     - Keeps track of the *file directory structure*, such as file names, locations, permissions, and hierarchies.
     - Maintains the *block locations* and *replication information* for every file stored in HDFS.
     - ==Does not store actual data blocks==; it only keeps metadata.
   - **Reliability**: ==Single point of failure (SPOF) in Hadoop ==1.x, though Hadoop 2.x introduced High Availability (HA) configurations to prevent downtime by using a standby NameNode.

##### 2. **DataNode** slave node
   - **Role**: The ==worker nodes== that store actual data blocks on local storage.
   - **Responsibilities**:
     - Stores, retrieves, and manages the data blocks requested by clients or the NameNode.
     - Periodically sends **heartbeat signals** to the NameNode to confirm it is operational.
     - Sends **block reports** to the NameNode, which include information on stored data blocks and their health status.
   - **Fault Tolerance**: If a DataNode fails, the NameNode reassigns the data blocks to other nodes based on the replication factor, ensuring no data loss.

##### 3. **Secondary NameNode**
   - **Role**: A helper to the NameNode, though not a true backup. It periodically takes snapshots of the NameNode’s metadata.
   - **Responsibilities**:
     - Merges the *edit log* with the *File System Image* (FsImage), which helps reduce the NameNode’s workload and keeps metadata up-to-date.
     - If the primary NameNode fails, this metadata snapshot can help reconstruct the system but is not a direct substitute.
   - **Not for Failover**: Hadoop 2.x introduced Standby NameNodes for High Availability rather than relying on the Secondary NameNode.

---

#### Key Concepts in HDFS

##### 1. Blocks and Block Size
   - **Block Concept**: Large files are split into smaller, fixed-size blocks, typically 128 MB by default (configurable).
   - **Advantages**:
     - Easier distribution across nodes.
     - Optimized read/write throughput since processing can happen in parallel.
   - **Replication**: Blocks are replicated across DataNodes for redundancy (default replication factor is 3).

##### 2. Replication and Fault Tolerance
   - **Replication Factor**: The number of copies of each block stored across different nodes (default is 3).
   - **Fault Tolerance**: If a DataNode fails, HDFS ensures data availability by replicating the missing blocks on other nodes.
   - **Rack Awareness**: HDFS is aware of the physical location of nodes and can store data copies across different racks to minimize data loss in case of rack failures.

##### 3. **Data Read and Write Operations in HDFS**
   - **Write Operation**:
     - Data is split into blocks and sent to DataNodes.
     - The NameNode assigns which DataNodes to store the replicas.
     - Data is stored on the primary DataNode, then replicated to the other DataNodes.
   - **Read Operation**:
     - The client requests the file from the NameNode.
     - The NameNode provides the block locations, and the client reads data blocks directly from the relevant DataNodes in parallel.

##### 4. **Heartbeat and Block Report Mechanism**
   - **Heartbeat**: DataNodes send regular signals to the NameNode indicating they are active.
   - **Block Report**: Periodic report from each DataNode to the NameNode about all the blocks it stores, helping the NameNode maintain block locations and detect any block-level failures.

##### 5. **Rack Awareness**
   - **Definition**: A topology-aware feature in HDFS that understands the physical layout of nodes and racks.
   - **Purpose**: Data blocks are distributed across racks to minimize data loss risk if an entire rack fails.
   - **Benefits**: Increases fault tolerance and reduces inter-rack network traffic, as replicas are placed on different racks.

---

#### **Advantages of HDFS**
   - **==Scalability==**: Can handle petabytes or even exabytes of data by scaling horizontally.
   - **==Cost-Efficiency==**: Runs on commodity hardware, reducing the need for high-cost storage solutions.
   - ==**High Fault Tolerance==**: Replication and distributed architecture provide strong data reliability.
   - ==**High Throughput Access==**: Optimized for batch processing and large datasets, which are common in Big Data analytics.
   - ==**Data Locality**:== Moves computation close to where data is stored, reducing network congestion and increasing processing speed.

#### **Limitations of HDFS**
   - **==Latency for Small Files==**: HDFS is inefficient for handling a large number of small files, as each file’s metadata is stored in the NameNode, which can lead to memory overload.
   - **==Single Point of Failure==** (in Hadoop 1.x): The NameNode failure would bring down the entire system, though HA was introduced in Hadoop 2.x to mitigate this.
   - **==Limited Random Access==**: HDFS is optimized for high-throughput and large sequential reads, not random reads or updates.
   - ==**Write Once, Read Many==**: Files in HDFS are immutable after they are written; updating a file requires rewriting it.

---

#### **HDFS and Data Access Patterns**
   - **Batch Processing**: HDFS excels in scenarios where data access is required in bulk, typically in batch processing jobs, making it suitable for MapReduce and other large-scale data analytics.
   - **Sequential Data Access**: Optimized for reading large files in a sequential manner, rather than random data access like traditional file systems.
---

### Map Reduce

**MapReduce** is a ==programming model and processing technique for distributed computing==, primarily used within the Hadoop ecosystem to process large datasets in parallel across clusters of computers. ==Developed by Google==, MapReduce is the core component that enables Hadoop to perform high-performance and fault-tolerant distributed data processing. Let’s dive into the details of MapReduce, including how it works, its key concepts, and use cases.

---

#### **Overview of Map-reduce**

   - **Purpose**: Map-reduce enables processing of vast amounts of data in a ==parallel, distributed fashion.==
   - **Components**: It consists of two main phases, the ==**Map phase**== and the **==Reduce phase==**, which split the task into smaller subtasks, execute them in parallel, and then aggregate the results.
   - **Fault Tolerance**: Automatically handles node failures by redistributing tasks to other nodes in the cluster.

---

#### **How MapReduce Works**
MapReduce operates in two main stages:

#### 1. **Map Phase**
   - **Function**: The ==Map phase processes input data and generates== ==a set of intermediate== ==key-value pairs==.
   - **Process**:
     - Each input data file is divided into blocks, which are assigned to different nodes in the cluster.
     - Each node executes a **Map function** on its assigned data blocks, which processes records individually.
     - The output is in the form of **key-value pairs** (for example, for counting words, the key could be a word, and the value could be the count of occurrences).
   - **Intermediate Data**: This phase generates intermediate data in key-value pairs, which is then sorted and grouped by key for the next phase.

#### 2. **Shuffle and Sort Phase**
   - **Function**: The Shuffle and Sort phase sorts all the intermediate data by key and groups it together for the Reduce phase.
   - **Process**:
     - Intermediate data from each Map task is grouped by key, so that all values corresponding to a particular key are together.
     - This sorting and grouping make it easier for the Reduce phase to aggregate results for each key.

#### 3. **Reduce Phase**
   - **Function**: The Reduce phase ==consolidates the intermediate data==, ==applying the logic to combine or aggregate values associated with each key.==
   - **Process**:
     - The Reduce function takes each key and processes the list of values associated with it.
     - This aggregation could be a sum, count, average, or any other operation, depending on the analysis required.
   - **Output**: The final output is typically stored in HDFS, representing the result of the entire MapReduce job.

---

#### **Detailed Steps of a MapReduce Job Execution**

#### 1. **Input Splitting**
   - **Data Splitting**: Hadoop splits the input data into fixed-size chunks (default 128 MB) called **splits**.
   - **Assignment to Mappers**: Each split is assigned to a Mapper, which processes one split independently of others.

#### 2. **Mapping**
   - **Mapper Execution**: Each Mapper processes the split data line-by-line, applying the user-defined Map function to each record.
   - **Key-Value Generation**: Mappers produce intermediate key-value pairs as output.

#### 3. **Shuffling and Sorting**
   - **Shuffle**: Intermediate key-value pairs are shuffled to group identical keys together.
   - **Sort**: The keys are sorted to prepare data for the Reduce phase, allowing efficient aggregation of values by key.

#### 4. **Reducing**
   - **Reducer Execution**: Each unique key is sent to a Reducer along with its corresponding list of values.
   - **Aggregation**: Reducer applies the aggregation or combination logic on the values, producing a consolidated result for each key.

#### 5. **Output Writing**
   - **Final Storage**: The results of the Reduce phase are written back to HDFS or other storage systems, typically as output files (one file per Reducer).

---

#### **Key Concepts in MapReduce**

#### 1. **Key-Value Pairs**
   - **Definition**: Data in MapReduce is represented as key-value pairs, both as input and output.
   - **Flexibility**: This structure allows MapReduce to process different data types in a uniform way.

#### 2. **Mappers and Reducers**
   - **Mapper**: Processes data and emits intermediate key-value pairs. Multiple Mappers work in parallel.
   - **Reducer**: Consolidates data based on keys and applies a final aggregation, such as summing or counting.

#### 3. **Combiner (Optional)**
   - **Purpose**: An optional step that acts as a “mini-reducer” to reduce the amount of intermediate data passed to Reducers, minimizing network traffic.
   - **Usage**: Useful for scenarios where partial aggregation can be done at the Mapper level (e.g., local word counts before sending to Reducer).

#### 4. **Partitioner**
   - **Function**: Determines how key-value pairs are distributed to Reducers by controlling which key-value pairs are sent to which Reducer.
   - **Example**: A default partitioner might hash the key to decide the Reducer, ensuring an even distribution of workload.

#### 5. **Job Tracker and Task Tracker (Hadoop 1.x) / Resource Manager and Node Manager (Hadoop 2.x)**
   - **Job Tracker**: Oversees the job’s execution (assigning tasks and monitoring nodes) in Hadoop 1.x.
   - **Task Tracker**: Executes individual tasks (Map or Reduce) on worker nodes.
   - In Hadoop 2.x, **YARN’s Resource Manager** and **Node Managers** replaced Job Tracker and Task Tracker for better scalability and fault tolerance.

---

#### **MapReduce Example: Word Count**

This example shows how MapReduce processes a word count job:

#### **1. Input Data**
   ```
   "big data and hadoop"
   "hadoop and mapreduce"
   ```

#### **2. Map Phase**
   - **Mapper Output**:
     ```
     ("big", 1), ("data", 1), ("and", 1), ("hadoop", 1)
     ("hadoop", 1), ("and", 1), ("mapreduce", 1)
     ```

#### **3. Shuffle and Sort Phase**
   - **Grouped Data**:
     ```
     ("and", [1, 1]), ("big", [1]), ("data", [1]), ("hadoop", [1, 1]), ("mapreduce", [1])
     ```

#### **4. Reduce Phase**
   - **Reducer Output**:
     ```
     ("and", 2), ("big", 1), ("data", 1), ("hadoop", 2), ("mapreduce", 1)
     ```

#### **5. Final Output**
   - The final output is stored in HDFS, providing a count of each word in the input data.

---

#### **Advantages of MapReduce**
   - **==Scalability==**: Can scale to handle petabytes of data across thousands of nodes.
   - **==Fault Tolerance==**: Automatic data replication and task re-execution in case of node failures.
   - ==**Data Locality==**: Tasks are assigned to nodes where data is stored, minimizing network traffic.
   - **==Parallel Processing==**: Executes tasks in parallel, optimizing processing time for large datasets.

#### **Limitations of MapReduce**
   - **==Inefficient for Small Tasks==**: MapReduce is optimized for large-scale batch processing, and overhead can be high for smaller tasks.
   - **==High Latency for Real-Time Processing==**: Designed for batch processing, not for real-time analytics. Frameworks like Apache Spark are better suited for low-latency applications.
   - ==**Single Data Flow**:== MapReduce is not suitable for iterative computations (e.g., machine learning algorithms), as each iteration requires a separate MapReduce job, increasing complexity and time.

#### **Use Cases for MapReduce**
   - ==**Log Analysis==**: Processing large volumes of logs for insights on server usage, error rates, or web traffic patterns.
   - **==Search Indexing==**: Building an inverted index for search engines, where documents are mapped to the keywords they contain.
   - **==Data Aggregation==**: Summing, counting, and averaging large datasets, such as in customer analytics or transaction histories.
   - **==ETL Operations==**: Transforming and loading data from various sources into data warehouses or storage systems for further analysis.

---


