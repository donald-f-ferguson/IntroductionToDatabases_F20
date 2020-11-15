

<br>
<br>
<br>
<br>
<br>
__NOTE:__ The site for the Spring section of the course is in-progress. Please
see [previous semster's site](https://donald-f-ferguson.github.io/w4111-Databases/)
for additional details. I am modifying the course but the spring version will be an evolution
of previous semester's course.



## Overview

This is the course page, project page and repository for Prof. Donald Ferguson's Columbia University course _W4111 - Introduction to Databases._ The content
evolves from semester to semester. The material in the repository contain the material for the spring 2020 sections: 
[COMS W4111 -- Introduction to Databases, sections 02, H02 and C02](https://www.cs.columbia.edu/education/courses/course/COMSW4111-2/26942/)
for the spring semester, 2020.


## Textbook and Course Material

Databases is a broad and rapidly evolving area. No single textbook covers the breadth of material and recent advances. 
The foundational concepts are mature and stable, however, and there are textbooks. The _recommended_ textbook for the 
course is _Database System Concepts, 7th Edition_ (by Abraham Silberschatz), ISBN: 978-0078022159. 
The textbook is very strongly recommended, and much of the course content will come from textbook material.

The [book's website](https://www.db-book.com/db7/) contains a lot of material, including lecture slides, database examples, study questions, ...

The [GitHub repository](https://github.com/donald-f-ferguson/COMSW4111_S20_Introduction_to_Databases) for the class will contains lecture material,
examples, homework definition, etc.

## Topics and Syllabus

### Course Description

From the university's course bulletin:


"The course covers what a database system is, how to design databases effectively and in a principled manner, how to query databases, 
and how to develop applications using databases: entity-relationship modeling, logical design of relational databases, relational algebra, SQL, 
database application development, database security, and an overview of query optimization and transaction processing. 
Additional topics generally include NoSQL, graph, object-relational, and cloud databases, as well as 
data preparation and cleaning of real-world data. The course offers both programming and non-programming paths for homework and projects, 
to accommodate students with different programming skills and backgrounds."

The course logically has four modules/sections:
1. __Foundational concepts:__ This module covers concepts like data models, relational model, relational databases 
and applications, schema, normalization, ... The section focuses on the relational model and relational databases. 
The concepts are critical or all types of databases and data centric applications.
2. __Database management system architecture and implementation:__ This module covers the software architecture, algorithms and
implementation techniques that allow databases management systems to deliver functions. 
Topics include memory hierarchy, storage systems, caching/buffer pools, indexes, query processing, query 
optimization, transaction processing, isolation and concurrency control.
3. __NoSQL -- "Not Only SQL" databases:__ This section provides motivation for "NoSQL" data models 
and databases, and covers examples and use cases. The section also includes cloud databases and databases-as-a-service.
4. __Data Enabled Decision Support:__ This section covers data warehouses, data import and cleanse, OLAP, 
Pivot Tables, Star Schema, reporting and visualization, and 
provides and overview of analysis techniques, e.g. clustering, classification, analysis, mining.

### Sections General Approach

This section of _W4111 - Introduction to Databases_ focuses on real world database applications and use cases. The use
cases come from the instructor's 35 year experience building software systems and solutions that build on databases.

The course covers the core material that all sections cover. There is greater emphasis on projects and less emphasis
on exams. Previous semesters' sections of the course have been too programming intensive. We are changing to better
accomodate non-CS majors and students less interested in hardcore programming. The section will offer
choices of projects that meet the capabilities and interests of both CS and non-CS students. This includes a
"No Programming Track" for the course projects.

The course will (attempt) cover the _some_ of the following databases and tools (as time permits):
- Databases:
    - Relational 
    - Bucket/BLOB/Block (Amazon S3)
    - Key/Value (Redis, AWS Memcache, AWS DynamoDB)
    - Document (DynamoDB)
    - Graph (Neo4j)
    - Wide Columns (Cassandra)
- Tools:
    - Tools for database application developers/administrators (DBAs), e.g. MySQL Workbench
    - Pivot Tables, QuickSight, Kylin
    - Pandas, Numpy, Jupyter Notebooks
    - scikit-learn
    - MapReduce
    - Data Pipelines

### Topics Details

- Overview

- ER Model
    - Diagrams with entity sets, primary and candidate keys, relationship sets (including at least binary and ternary relationship sets), key and participation constraints for relationship sets, weak entity sets, is-a hierarchies, aggregation
    -Understanding of how to model real-world data into ER diagrams
    - Ability to read, write, and interpret complex ER diagrams, with many entity and relationship sets, and to understand what data is allowed and disallowed by the constraints expressed in the diagram

- Relational Model
    - Introduction to basics of data definition portion of relational model and SQL
    - Data types, schemas, constraints
    - Principled translation from ER diagrams to SQL schemas, including understanding of constraints in ER diagrams that cannot be translated precisely

- Relational Algebra
    - Importance of relational algebra as foundation of query portion of SQL, both to understand the semantics of relational queries deeply (and hence to learn to write SQL queries in a well founded manner) and to understand when queries are equivalent to each other, which in turn enables relational operator reordering during query optimization
    - Relational algebra operators (selection, projection, cross product, condition join, equijoin, natural join, union, intersection, set difference, renaming)
    - Inference of output schema for relational algebra expressions
    - Translation of English statements into equivalent relational algebra expressions

- SQL
    - Conceptual execution model of a SQL query
    - Basics
        - Select, From, Where, Distinct, Group by, Having, Order clauses
        - Inner, Left/Right/Outer Joins
        - Nulls
        - Any, All, Unique
        - Aggregate operators
        - Union, Intersect, Except
        - Multi-set/bag semantics
        - Translation from relational algebra into SQL and vice-versa
        - Constraints: primary key, unique, foreign key, attribute-based check constraints, tuple-based check constraints, assertions
    - Advanced
        - Nested queries, correlated subqueries
        - Not Exists, double negation
        - UDFs, Stored Procedures
        - Triggers
        - (Non-recursive) With, View
        
- Application Programming and Database APIs 
    - Database engine, connection, cursors
    - Why cursors?
    - Impedance mismatch and programming API to database
    - LINQ-style query composition (Spark or Pandas)
    
    
- Security Foundations (1 lecture)
    - Access controls
    - GRANT statements, understanding how giving and revoking privileges propagates across users
    - Views as data access control

- Normalization
    - Importance in real-world applications of detecting and avoiding data redundancy, as well as update and delete anomalies
    - Motivation and definition of functional dependencies and their role to detect and avoid redundancy and update and delete anomalies
    - Reasoning about functional dependencies, closure of an attribute set, Armstrong’s axioms
    - Definition of Boyce-Codd Normal Form
    - Definition of lossless-join and dependency-preserving decompositions
    - Decomposition of a relation into BCNF
    - Discussion of best practices, design choices, and tradeoffs, grounded on normalization theory

- Overview of Storage and Indexes
    - Memory hierarchy
        - Latency and throughput of memory, SSD, disk
        - Seeks vs. scans
        - Persistent vs. non-persistent memory
    - High level discussion of how disk and SSD work
        - Disks rotate and have arms
        - SSDs have banks that burn out; write amplification
    - Implication: data should be stored as pages and cached in “buffer pool”
    - Importance of indexes for speeding up queries
        - Why and when indexes speed up lookups and joins
        - Search keys
        - Covering indexes
        - CREATE INDEX statements
        
- Overview of Query Optimization
    - Access methods, cost models
    - Join optimization
        - Nested loops vs. index nested loops
        - Join order and cardinality
        - Discussion of use of cost models to decide join order and index selection for 2-way joins
    - High-level discussion of complexity and general approach for optimizing execution of complex queries


- Overview of Transaction Processing
    - Why are transactions needed with ACID properties?
    - BEGIN COMMIT statements
    - Schedules: serial schedules, schedule equivalence
    - Conflict serializability, strict 2-phase locking
    - Explanation of need for fine-grained locks

- NoSQL
    - Document, Key-Value
        - Data model, JSON, nested data model
        - Schema first vs. schema later
        - Document and key-value stores
        - Discussion of use cases for document and key-value stores vs. relational databases
    - Graph DB
        - Experience with a graph database (e.g., Neo4j)
        - Representing graphs as nodes and edges
        - Paths and path queries in Cypher
        - Expressing graph queries as joins
        - Discussion of relative merits of graph databases vs. relational databases
    - Object DB concepts
        - Inheritance
        - Composite attributes
        - References, linked data

- Cloud databases:
    - Scale-up, scale-out
    - Use cases
    - Consistency and integrity models
    
- Security Extensions
    - Overviews of different security models concerning databases
    - SQL injection
    - Basics of encryption and encrypted query processing
    - Concept of differential privacy in databases
    
- Data Preparation and Cleaning
    - Prevalence and impact of data errors and inconsistencies in real-world data
    - Data preparation: extraction, data wrangling (e.g., Trifacta)
    - Discussion of fact that multiple data sources generally disagree in practice
    - Need for data cleaning: constraint violations, value errors, schema integration, entity resolution
    - MapReduce, Hadoop
    
- Decision Support/Big Data
    - Normalization vs Wide-Flat
    - OLAP
    - Data warehouses
    - Data preparation, MapReduce, Hadoop
 

### Syllabus and Tentative Lecture Schedule


    
## Logical Tracks

There are two distinct groups of students in this class:
1. Students experienced with and interested in programming, solution development and software development.
2. Students with little experience and interest in software engineering, and who are interested in using data in IEOR, 
economics, applied science and other disciplines.

For this reason there are two tracks students can take in the class. Both tracks cover the same material but differ in 
homework assignment, projects and exams. The tracks are:
1. _Non-programming_ focuses on using databases through interfaces and tools. Most tools require some very basic and
simple scripting, we minimize the need to program. Students will design, implement and use databases to solve
problems using tools common in data analysis, operations research, economics, scientific computing.
2. _Software/Applications_ focuses on building simple but realistic/representative SW systems and applications. This
includes applications like 3-tier, interactive web applications that build on databases.

The first lecture will provide an overview of the tracks.

## Exams and Grading

The course grading is on a point scale from 0-100.
- There are 5 homework assignments, each worth 10 points. The assignments build on previous assignments, 
and the student will have completed a project by the end of the course.
- Midterm exam is worth 20 points.
- Final exam is work 30 points.


## Lecture

This section contains links to lecture material. Most lecture material is a mix of:
    - Jupyter notebook.
    - Python slides.
    - Sample code.

- __Lecture 1: Introduction, Overview, Core Concepts:__
    - [Jupyter Notes](Lectures/Lecture_1/w4111-F2020-Lecture_1a.ipynb)
    - [HTML version of notebook](Lectures/Lecture_1/w4111-F2020-Lecture_1a.html)
    - [Power Point Slides](Lectures/Lecture_1/Lecture_1_Introduction_and_Concepts_v2.pptx)


- __Lecture 2: Fundamental Concepts - Data Models, ER Models, Relational Model, SQL:__
    - [Jupyter Notes](Lectures/Lecture_2/w4111-F2020-Lecture_2.ipynb)
    - [HTML version of notebook](Lectures/Lecture_2/w4111-F2020-Lecture_2.html)
    - [Power Point Slides](Lectures/Lecture_2/Lecture_2_ER_Relational_SQL_v1.pptx)
    
    
- __Lecture 3: Fundamental Concepts - Data Models, ER Models, Relational Model, SQL (Cont):__
    - [Jupyter Notes](Lectures/Lecture_3/w4111-F2020-Lecture_3.ipynb)
    - [HTML version of notebook](Lectures/Lecture_3/w4111-F2020-Lecture_3.html)
    - [Power Point Slides](Lectures/Lecture_3/Lecture_3_ER_Relational_SQL_v1.pptx)
    
    
- __Lecture 4: Fundamental Concepts - Data Models, ER Models, Relational Model, SQL (Cont):__
    - [Power Point Slides](Lectures/Lecture_4/Lecture_4_ER_Relational_SQL_v2.pptx)
    

- __Lecture 5: Fundamental Concepts - Data Models, ER Models, Relational Model, SQL (Cont):__
    - [Power Point Slides](Lectures/Lecture_5/Lecture_5_ER_Relational_SQL_v1.pptx)
    
    
- __Lecture 6: Fundamental Concepts - Data Models, ER Models, Relational Model, SQL (Cont):__
    - [Power Point Slides](Lectures/Lecture_6/Lecture_6_ER_Relational_SQL_v1.pptx)
    
    
- __Lecture 7: Fundamental Concepts - Data Models, ER Models, Relational Model (Closure) (Cont):__
    - [Power Point Slides](Lectures/Lecture_7/Lecture_7_ER_Relational_SQL_Closure_v2.pptx)
    
    
- __Lecture 8: Module II -- Disks and Indexes:__
    - [Power Point Slides](Lectures/Lecture_8/Module_Lecture_8_II__DIsks_Indexes.pptx)
    
    
- __Lecture 9: Module II -- Index, Transactions, Query Processing:__
    - [Power Point Slides -- Query Processing/Transactions]:(Lectures/Lecture_9/Module_II_Lecture_9_Query_Transactions_NoSQL.pptx)
    - [Power Point -- No SQL](Lectures/Lecture_9/F2020_no_sql.pptx) 
    
    
- __Lecture 10: Module III -- NoSQL Continued:__
    - [Power Point SLides](Lectures/Lecture_10/Module_II_Lecture_10_NoSQL_2.pptx) 



## Homework Links

- Homework 2: Data Files
    - [People](Homework/HW2_All/people.csv)
    - [Departments](Homework/HW2_All/departments.csv)
    - [Courses](Homework/HW2_All/courses.csv)
    
<br>
    
## Approximate Syllabus

- __Module I -- Foundational Concepts__<br><br>
  - Lecture 1:
    - Course overview, homework assignments, projects, grading.
    - Database concepts
    - Introduction to relational model, introduction to SQL.
  - Lecture 2:
    - ER modeling (continued)
    - Continuing relational data model. Realizing logical data models with relational model and relational databases.
  - Lecture 3:
    - Relational data model details
    - Data modeling design patterns and best practices
  - Lecture 4:
    - Formal model for relational data model and operations.
    - Relational algebra, and basis for relational databases.
  - Lecture 5: Structure Query Language (I)
    - Select, Aggregation/Group By, Order By
    - Join, Union, set operations
    - Subqueries
  - Lecture 6: SQL (II)
    - Contraints
    - Indexes
    - Triggers
    - Stored prodecures, user defined functions
    - Views
  - Lecture 7:
    - Applications using databases
    - Connections, sessions, cursors
    - Application data models and relational data model
    - Pandas
    - Basics of security
  - Lecture 8: Normalization and De-Normalization
    - Motivation: Integraity and avoiding anaomalies versus query/decision support.
    - Theory: Normal forms, lossless decomposition, functional dependencies, Armstrong's Axioms
    - Examples and best practices.
- __Module II -- DBMS Implementation__<br><br>
  - Lecture:
    - Memory hierarchy
    - Disks, storage, data transfer, data placement
    - Indexes: concepts, hash index, B+ Tree, text indexing
  - Lecture 10:
    - Basics of query processing and query optimization.
    - Transaction processing, recovery and availability, isolation
    - Serializability, locking
- __Module III -- NoSQL__<br><br>
  - Lecture 11:
    - Motivation, NoSQL models and examples, scenarios
    - CAP Theorem, ACID vs Base
    - Graph databases and Neo4j
  - Lecture 12:
    - Document databases
    - Key-value databases
    - Application scenarios and examples.
- __Module 4__ -- Decision Support/Data Anaysis<br><br>
  - Lecture 13:
    - Core concepts
    - Data pipelines, MapReduce
    - Streams
  - Lecture 14 -- 01-May-2020:
    - Pandas and SQL/databases
    - Data visualization
    - Data analysis

