

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

### Syllabus and Tentative Lecture Schedule

- __Module I -- Foundational Concepts__<br><br>
  - Lecture 1 -- 24-Jan-2020:
    - Course overview, homework assignments, projects, grading.
    - Database concepts
    - Introduction to relational model, introduction to SQL.
  - Lecture 2 -- 31-Jan-2020:
    - ER modeling (continued)
    - Continuing relational data model. Realizing logical data models with relational model and relational databases.
  - Lecture 3 -- 07-Feb-2020:
    - Relational data model details
    - Data modeling design patterns and best practices
  - Lecture 4 -- 14-Feb-2020:
    - Formal model for relational data model and operations.
    - Relational algebra, and basis for relational databases.
  - Lecture 5 -- 21-Feb-2020: Structure Query Language (I)
    - Select, Aggregation/Group By, Order By
    - Join, Union, set operations
    - Subqueries
  - Lecture 6 -- 28-Feb-2020: SQL (II)
    - Contraints
    - Indexes
    - Triggers
    - Stored prodecures, user defined functions
    - Views
  - Lecture 7 -- 06-Mar-2020:
    - Applications using databases
    - Connections, sessions, cursors
    - Application data models and relational data model
    - Pandas
    - Basics of security
  - Lecture 8 -- 13-Mar-2020: Normalization and De-Normalization
    - Motivation: Integraity and avoiding anaomalies versus query/decision support.
    - Theory: Normal forms, lossless decomposition, functional dependencies, Armstrong's Axioms
    - Examples and best practices.
- 20-Mar-2020: No class. Spring break.<br><br>
- __Module II -- DBMS Implementation__<br><br>
  - Lecture 9 -- 27-Mar-2020:
    - Memory hierarchy
    - Disks, storage, data transfer, data placement
    - Indexes: concepts, hash index, B+ Tree, text indexing
  - Lecture 10 -- 03-Apr-2020:
    - Basics of query processing and query optimization.
    - Transaction processing, recovery and availability, isolation
    - Serializability, locking
- __Module III -- NoSQL__<br><br>
  - Lecture 11 -- 10-Apr-2020:
    - Motivation, NoSQL models and examples, scenarios
    - CAP Theorem, ACID vs Base
    - Graph databases and Neo4j
  - Lecture 12 -- 17-Apr-2020:
    - Document databases
    - Key-value databases
    - Application scenarios and examples.
- __Module 4__ -- Decision Support/Data Anaysis<br><br>
  - Lecture 13 -- 24-Apr-2020:
    - Data warehouses
    - Data preparation, MapReduce, Hadoop
    - OLAP, Pivot Tables
  - Lecture 14 -- 01-May-2020:
    - Pandas and SQL/databases
    - Data visualization
    - Data analysis
    
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

This section contains links to lecture material:

