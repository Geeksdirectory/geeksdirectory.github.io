---
title: BDA Assignment
date: 2024-10-02
---

![Syllabus](https://i.imgur.com/R5O9hNh.png)


## 1.  Summarize Bloom’s filter with example and its application

## 2. Explain DGIM algorithm.

## 3. Explain cure algorithm (2)
## 4.What is Recommender System? Explain Types of recommender system.
## 5. Distance measure (2)

## 6. Page Rank Algorithm  (2)
## 7. Explain Issues in Data stream query processing
## 8. Explain Collaborative filtering system. How is it different from content  based system 

![](https://i.imgur.com/g1JdDdN.png)



![](https://i.imgur.com/mLA8CIF.png)



# Module 5

## The stream data model 

The stream data model represents continuous, real-time data flows

- **Continuous Data Flow**: Data arrives in a continuous stream rather than in fixed sets.
- **Real-time Processing**: Data is processed immediately as it arrives.
- **Unbounded Data**: The data stream may not have a known end, making it different from traditional static data sets.
- **Time Sensitivity**: Data processing and analysis often depend on the order and timestamp of events.
- **Incremental Processing**: Data is processed in small increments, as opposed to batch processing.
- **Windowing**: Data is analyzed over specific time windows (e.g., last 10 seconds of data).
- **High Throughput**: Stream models handle a large volume of data in real-time.
- **Low Latency**: Quick response times are required for immediate processing.
- **Stateful Operations**: The system may maintain some state (memory of past data) to compute future events.
- **Use Cases**: Suitable for applications like live analytics, IoT, financial transactions, and sensor data.
### **Advantages of Stream Data Model**:

1. **Real-time Insights**: Enables instant analysis and decision-making as data is received.
2. **Low Latency**: Immediate data processing ensures fast responses to events.
3. **Scalability**: Designed to handle high-throughput applications like IoT, social media feeds, etc.
4. **Continuous Processing**: Efficient for monitoring and managing data without delays.
5. **Event-Driven**: Well-suited for applications that need to react to real-time changes (e.g., fraud detection, stock market analysis).
6. **Resource Efficiency**: In some cases, it reduces resource usage by avoiding the need to store large amounts of data for batch processing.

### **Disadvantages of Stream Data Model**:

1. **Complex Development**: Implementing a real-time data pipeline is often more complex than traditional batch systems.
2. **Fault Tolerance**: Ensuring system reliability and recovering from errors in a real-time system can be challenging.
3. **High Cost**: Real-time processing may require significant infrastructure and computational resources.
4. **Data Loss Risk**: If there is a system failure, there’s a risk of losing incoming data since it is not stored persistently.
5. **Debugging Challenges**: Debugging and testing real-time applications can be difficult due to the continuous flow of data.

### **Problems and Limitations**:

1. **Data Ordering**: Maintaining the correct sequence of events in a high-throughput environment can be difficult.
2. **State Management**: Managing the state for processing, especially in distributed systems, can be complex.
3. **Latency vs Accuracy**: Real-time processing often sacrifices accuracy for speed, which may not work for all applications.
4. **Windowing Limitations**: Some data might fall outside the time windows used for analysis, leading to incomplete results.
5. **Data Overload**: Handling continuous streams at scale can overwhelm systems if not carefully managed.
6. **Inconsistent Data Quality**: Stream data might have inconsistent quality, missing values, or require cleansing.s

## 2. What is Stream Computing ???

**Stream computing** (or **stream processing**) refers to the real-time processing of continuous data streams as they are produced.

Unlike traditional batch processing, where data is collected, stored, and then processed later, stream computing handles data in motion—processing it immediately as it arrives.

### Key Features of Stream Computing:

1. **Real-Time Data Processing**: Processes data as soon as it is generated, without delays.
    
2. **Continuous Data Flow**: Data comes in continuously from sources like sensors, social media, financial transactions, or IoT devices.
    
3. **Low Latency**: Stream computing aims to provide near-instant insights with minimal delay between data generation and action.
    
4. **Scalability**: Can handle high-velocity, high-volume data by scaling horizontally (across multiple servers).
    
5. **Stateful and Stateless Operations**:
    
    - **Stateless**: Each event is processed independently (e.g., filtering out specific types of data).
    - **Stateful**: Keeps track of the state across events (e.g., counting occurrences over time).

### Examples of Stream Computing Use Cases:
1. Financial Services
2. IoT (Internet of Things)
3. Social Media
4. Network Monitoring
5. Healthcare
### Common Stream Processing Frameworks:

- **Apache Kafka**: Distributed event streaming platform for building real-time data pipelines.
- **Apache Flink**: Stream processing framework for distributed data streams.
- **Apache Storm**: Real-time computation system that processes unbounded streams of data.
- **Spark Streaming**: Extension of Apache Spark for processing real-time data streams.

### Benefits of Stream Computing:

1. **Immediate Insights**: Enables real-time decision-making and actions based on incoming data.
2. **Efficient Resource Utilization**: Continuous processing reduces the need to store and process massive batches of data later.
3. **Scalable**: Can handle large volumes of fast-moving data by distributing the workload across clusters.
4. **Flexibility**: Supports a wide variety of real-time applications, from real-time dashboards to automated triggers and actions.




## 3. Page Rank 


> [!Defination]
> **PageRank** is an algorithm that assigns a numerical value to web pages, based on the quantity and quality of links pointing to them, to measure their importance and influence within the web.

**PageRank Algorithm** is a method developed by **Larry Page** and **Sergey Brin**, the founders of Google, to rank web pages in search engine results.

It works by evaluating the quality and quantity of links pointing to a page and assigning it a "rank" or importance score.


![](https://i.imgur.com/g5kxKle.png)


### 1. **Webpages as Nodes**

   - Imagine the entire web as a graph, where **web pages are nodes**, and **hyperlinks between pages are edges** connecting them.
   - Each page in this graph points to other pages via links and receives links from others.

### 2. **The Importance of Links (Votes)**

   - A **link to a page is considered a vote** of confidence or importance for that page.
   - Not all votes (links) are equal; the importance of a page that gives the vote matters.

### 3. **Recursive Nature of PageRank**

   - The PageRank of a page is determined by the **PageRank of other pages linking to it**.
   - Pages that are linked from **many high-ranked pages** will receive a higher score.
   
### 4. **Random Surfer Model**

   - PageRank is based on the assumption of a "random surfer" who starts on a random page and **randomly follows links**.
   - With each step, the surfer either clicks a link to another page or jumps to a random page with some probability.

### 5. **Damping Factor

   - The algorithm introduces a **damping factor** (usually around 0.85), representing the probability that a user follows a link.
   - With a probability of **(1 - damping factor)**, the user jumps to a random page instead of following a link.
   - This ensures the model doesn’t get stuck in loops or dead-end pages.

### 6. **Rank Calculation Formula**

   - For any given page (P), its PageRank is calculated as:

>[!formula]
> $PR(P) = \frac{1 - d}{N} + d \left( \sum_{i=1}^{n} \frac{PR(P_i)}{L(P_i)} \right)$
    
 Where:
 - **d** is the damping factor (typically 0.85),
 - **N** is the total number of pages,
 - **PR(Pi)** is the PageRank of the pages linking to page P,
 - **L(Pi)** is the number of outbound links from page Pi.

### 7. **Initial PageRank**

   - Every page is assigned an **initial equal rank** before calculations begin, usually \( 1/N \) where N is the total number of pages.
   - The PageRank values are updated iteratively until they converge (i.e., stop changing significantly).

### 8. **Handling Dead Ends (Sink Pages)**

   - Some pages might not link to any other pages, creating **dead ends**.
   - The damping factor helps to handle these situations, as it prevents such pages from trapping the random surfer indefinitely.

### 9. **Iterative Process**

   - The calculation of PageRank is performed in an iterative process where the ranks of all pages are updated multiple times.
   - The process repeats until the PageRank values of all pages stabilize.

### 10. **Relevance of High PageRank**

   - A high PageRank means a page is linked to by many important pages, making it more authoritative or popular.
   - However, PageRank is just one of many factors Google uses to rank pages in search results.

PageRank provides a scalable way to evaluate the importance of millions (or billions) of web pages, helping search engines deliver more relevant results.



### Importance of page rank

- measure page authority
- Improves search relevace
- link popularity factor
- reduce spam
- Democratic nature
- Encourages quality content
- seo foundation
- enhances web navigation 
- foundation for modern search algorithm


## 3. Structure of web (bowtie)

The **structure of the web** can be understood as a vast network of interconnected documents (web pages), where each page is linked to others through **hyperlinks**.

### 1. **Nodes (Web Pages)**

   - Each web page is represented as a **node** in the web's graph-like structure.
   - Pages can contain text, images, videos, and other media, along with links to other pages.

### 2. **Edges (Hyperlinks)**

   - **Hyperlinks** between pages act as **edges** connecting the nodes.
   - A hyperlink from one page to another creates a directed connection, indicating a relationship or reference.

### 3. **Directed Graph**

   - The web forms a **directed graph**, where links have direction (from one page to another).
   - Not all links are reciprocal, meaning one page may link to another without receiving a link back.

### 4. **Hub-and-Spoke Model**

   - Popular or highly authoritative pages act as **hubs**, receiving many inbound links.
   - These hubs often link to **spoke pages**, which are smaller, more specific resources or less popular pages.

### 5. **Clusters or Communities**
   - Pages are often grouped into **clusters** or communities based on shared topics or common links.
   - Pages within a cluster tend to have more interlinks with each other than with pages outside the cluster.

### 6. **Dead Ends and Sink Pages**
   - **Dead ends** occur when a page has no outbound links, leaving no way for users to navigate to other pages.
   - **Sink pages** have inbound links but no  outbound links, potentially trapping users.

### 7. **Small-World Property**
   - The web exhibits the **small-world phenomenon**, where most pages are separated by only a few links, making it relatively easy to navigate between distant pages.

### 8. **Hierarchical Structure**
   - Web pages are often organized hierarchically, with **homepage** or main pages at the top, linking to various subpages that provide more specific information.

### 9. **Dynamic and Static Content**
   - The web includes **static content** (fixed HTML pages) and **dynamic content** (pages generated based on user interaction or database queries).

### 10. **Crawling and Indexing**

   - Search engines use **web crawlers** to explore the web's structure by following links from page to page, gathering and indexing content for retrieval in search results.


![bowtie](https://i.imgur.com/63rndNS.jpeg)

### 1. **Bow-Tie Structure of the Web**

- The web can be broken down into a **bow-tie shape** with distinct regions based on how pages are connected to each other via hyperlinks.

### 2. **Strongly Connected Component (SCC)**

- **SCC** is the **central core** of the web, consisting of pages that are **strongly connected** to each other.
- **Any page in the SCC can be reached from any other page within the SCC**, and vice versa.
- This component contains the most tightly interlinked and authoritative pages, often highly ranked websites.

### 3. **IN Component**

- Pages in the **IN** component are those that **can link to the SCC**, but pages in the SCC **cannot link back** to them.
- These are pages that can access the core but are not reachable from the SCC, often newly created or less authoritative pages.

### 4. **OUT Component**

- Pages in the **OUT** component are those that **can be reached from the SCC** but **do not link back** to the SCC.
- These are often result pages or pages that provide specific resources but aren't heavily linked to by other pages.

### 5. **Tendrils**

- **Tendrils** are pages that are not part of the SCC, IN, or OUT components.
- They **link to either the IN or OUT components but not to both**, forming pathways that connect these regions but **never reach the central SCC**.
- Tendrils can be thought of as isolated paths or dead-end areas of the web, leading to content that is not as well connected.

### 6. **Disconnected Components (Islands)**

- Some pages are completely isolated, meaning they neither connect to the SCC nor to the IN or OUT components.
- These are often referred to as **islands** in the web's structure, completely separate from the bow-tie.

### 7. **Tubes**

- **Tubes** are special pathways that directly connect **IN** to **OUT** without going through the SCC.
- These serve as direct routes between peripheral parts of the web.


