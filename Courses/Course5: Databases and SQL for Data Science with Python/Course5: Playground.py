#============================================ Module 1 =======================================================================
# SQL is a language used for relational databases to get data out of a database
# What data? Facts (words, numbers), Pictures, Assets
# What is a database? Repository of data, provides functionality for adding, modyfing and querying that data
# Basic SQL commands: CREATE, SELECT, INSERT, UPDATE, DELETE

# Select: 
SELECT COLUMN1, COLUMN2, ... FROM TABLE_1 ; # General syntax
SELECT * FROM TABLE_1 ; # To retreive all columns
SELECT <COLUMNS> FROM TABLE_1 WHERE <predicate> ; # To filter data based on a predicate
# e.g. to select first 5 rows: SELECT * FROM TABLE_1 WHERE ID <= 5 ;
# another e.g.: select * from FilmLocations where Locations = 'City Hall'

# Count:
# Retreives number of rows that matches the query criteria (NOT ROW CONTENT, JUST HOW MANY ROWS MATCH THE CRITERIA)
select COUNT(COUNTRY) from MEDALS where COUNTRY = 'CANADA' 

# Distinct:
# Removes duplicate values from a result set
select DISTINCT COUNTRY from MEDALS where MEDALTYPE = 'GOLD' # In case some countries receive multiple gold medals

# Limit:
# Restricts the number of rows retreived from the database
select * from tablename LIMIT 10
select * from MEDALS where YEAR = 2018 LIMIT 5 # shows 5 rows in the MEDALS table for a particular year

# Insert:
# Add new rows to a table
insert into tablename (Name, Surname, Age) values ('Mateusz', 'Pawlaczyk', 20) # IMPORTANT no. of columns must = to no. of values
# we can also add multiple rows to our Name, Surname, Age columns, just do another bracket () under the one above

# Update:
# Welp it updates a row
UPDATE tablename SET Columnname = Value WHERE condition # if you don't specify where, all the rows will be updated
# UPDATE Author SET Lastname='KATTA', FIRSTNAME='Lakshmi' WHERE Author_ID='A2'

# Delete
# deletes rows
DELETE FROM Author WHERE Author_ID IN ('A2','A3') # if you don't specify where, all rows will be removed (careful buddy)

#============================================ Module 2 =======================================================================
# Data Definition Language (DDL) Statements
# Used to define, change, or drop data - tables
# E.g. CREATE, ALTER, TRUNCATE, DROP


# Data Manipulation Language (DML) Statements
# Used to read and modify data - rows
# E.g. INSERT, SELECT, UPDATE, DELETE - row (like in module 1)

# Create:
# Syntax: 
CREATE TABLE table_name
    (
      column_name_1 datatype optional_parameters,
      column_name_2 datatype,
      column_name_n datatype
    )
# datatypes include: CHAR(2) - string of fixed length 2 AND VARCAHAR(14) - variable length, up to 14 chatacters long
# optional parametrs include: PRIMARY KEY (prevents dulicates in the table), NOT NULL

# Better example:
CREATE TABLE EMPLOYEES (
                            EMP_ID CHAR(9) NOT NULL, 
                            F_NAME VARCHAR(15) NOT NULL,
                            L_NAME VARCHAR(15) NOT NULL,
                            SSN CHAR(9),
                            B_DATE DATE,
                            SEX CHAR,
                            ADDRESS VARCHAR(30),
                            JOB_ID CHAR(9),
                            SALARY DECIMAL(10,2),
                            MANAGER_ID CHAR(9),
                            DEP_ID CHAR(9) NOT NULL,
                            PRIMARY KEY (EMP_ID));
                            
  CREATE TABLE JOB_HISTORY (
                            EMPL_ID CHAR(9) NOT NULL, 
                            START_DATE DATE,
                            JOBS_ID CHAR(9) NOT NULL,
                            DEPT_ID CHAR(9),
                            PRIMARY KEY (EMPL_ID,JOBS_ID));
 
 CREATE TABLE JOBS (
                            JOB_IDENT CHAR(9) NOT NULL, 
                            JOB_TITLE VARCHAR(30),
                            MIN_SALARY DECIMAL(10,2),
                            MAX_SALARY DECIMAL(10,2),
                            PRIMARY KEY (JOB_IDENT));

CREATE TABLE DEPARTMENTS (
                            DEPT_ID_DEP CHAR(9) NOT NULL, 
                            DEP_NAME VARCHAR(15) ,
                            MANAGER_ID CHAR(9),
                            LOC_ID CHAR(9),
                            PRIMARY KEY (DEPT_ID_DEP));

CREATE TABLE LOCATIONS (
                            LOCT_ID CHAR(9) NOT NULL,
                            DEP_ID_LOC CHAR(9) NOT NULL,
                            PRIMARY KEY (LOCT_ID,DEP_ID_LOC));

# Alter:
# Add/remove columns, keys, constraints, or modify datatype
# Syntax:
ALTER TABLE <your_table_name> # and then, same line either:
ADD COLUMN <column_name_n> datatype
MODIFY <column_name_n> <data_type>
 # To change the data type of an existing column to varchar data type write:
ALTER TABLE table_name ALTER COLUMN column_name SET DATA TYPE VARCHAR(20);
#  To add a column ‘ID’ that contains 7 character alpha-numeric values to our database
ALTER TABLE Employees ADD ID char(7)


# Drop (delete)
DROP TABLE <table name>;
DROP COLUMN <column_name_n>

# Truncate (delete data in table without deleting table itself)
TRUNCATE TABLE <table_name>
  IMMEDIATE # specifies to process statement immediately, cannot be undone)

# SCENARIO:
# create a table with CREATE
# ALTER - create a new column
# UPDATE - add values e.g. update petsale set quantity = 24 where ID = 1
# after each modification, use select * from petsale to SEE THE TABLE (otherwise won't show up)

#============================================ Module 3 =======================================================================
# ===== REFINING YOUR RESULTS
# Retreiving rows when predicate unknown e.g. can't use ID because don't remember the specific number
SELECT firstname FROM Author WHERE firstname like 'R%' # finds all names that start with the letter R (% can be in front of R, after R or BEFORE AND AFTER - [THERE ARE RULES - see SOME EXAMPLES OF GROUPING/SORTING], but MUST BE within quotation marks)
SELECT title FROM Book WHERE pages >=290 AND pages<=300 # finds all books whose number of pages is between 290 and 300
SELECT title FROM Book WHERE pages BETWEEN 290 AND pages 300 # alternative version
# Now, what do we do when we can't select range, e.g. when we want to know which country the authors are from?
SELECT firstname, lastname, country FROM Author WHERE country="Australia" OR "country"=BR # this is if we know which country we're interested in
SELECT firstname, lastname, country FROM Author WHERE country IN('AU','BR','CH','PL') # this is if you want to use maaaany countries (less typing)

# Sorting Result Sets (e.g. alphabetically)
SELECT * FROM Book # this will show you the whole dataset, but what if you want to select titles only?
SELECT title FROM book # ok, but now the list isn't sorted in any order as we don't have IDs, let's sort alphabetically
SELECT title FROM book ORDER BY title # ascending order
SELECT title FROM book ORDER BY title DESC # descending order, now it's from Z to A 
SELECT title FROM book ORDER BY 2 # if you want to sort by indicating column sequence number, in this case we're talking about second column (pages)

# Grouping Result Sets
# E.g. eliminating duplicates and further restricting values
SELECT country FROM Author ORDER BY 1 # full list of countries where authors come from (alphabetically), there are duplicates
SELECT DISTINCT(country) FROM Author # no duplicates :D, but we don't know how many authors come from each country :<, so:
SELECT country, count(country) FROM Author GROUP BY country # wheeeyyyy, ok but now we have a new column that's called '2' yuck
SELECT country, count(country) as Count FROM Author GROUP BY country # sa,e as above but count column is actually called count
# wanna see countries where the number of authors is greater than say 4?
SELECT country, count(country) as Count FROM Author GROUP BY country HAVING COUNT(country)>4 # having is a condition for group by clause

# SOME EXAMPLES OF GROUPING/SORTING
# basics
SELECT F_NAME, L_NAME FROM EMPLOYEES WHERE ADDRESS LIKE '%Elgin,IL%'; # to find names and surnames who live in Elgin
...WHERE B_DATE LIKE '197%'; # those who were born in the 70's
# first example & before and after - indicates that address string can have more character, both before and after required text - results appear as Elgin, IL, X Street or Y Street, Elgin, IL, if % before Elgin, then only Elgin, IL, X Street would show up
# second example, extra values can only appear after 7 (1970-1979) not before 1
# actual grouping
SELECT DEP_ID, COUNT(*) FROM EMPLOYEES GROUP BY DEP_ID; # Grouping - for each department ID, we want to find the number of employees in department
SELECT DEP_ID, AVG(SALARY) FROM EMPLOYEES GROUP BY DEP_ID HAVING AVG(SALARY) >=60000; # group by dep_id and filter the ones that have avg. salary of >= 60,000
ORDER BY AVG(SALARY) DESC # ADD THIS TO THE ONE ABOVE TO SORT BY DESCENDING ORDER :)

# EXAMPLE OF SORTING
SELECT F_NAME, L_NAME, DEP_ID FROM EMPLOYEES ORDER BY DEP_ID;

# Practice Quiz answers
SELECT * FROM Employees ORDER BY Lastname # if you want to retreive a list of employees in alphabetial order of Lastname 
HAVING # Used in order to set a filtering condition when using GROUP BY clause
SELECT * FROM Author WHERE Country IN ('A','B','C') # you want to retreive a list of authors from 3 countries
SELECT Title, Price FROM Book WHERE Price >= 10 and Price <= 25; # TWO WAYS TO RETREIVE LIST OF BOOKS PRICES IN RANGE $10-$25
SELECT Title, Price FROM Book WHERE Price BETWEEN 10 and 25; # TWO WAYS TO RETREIVE LIST OF BOOKS PRICES IN RANGE $10-$25

# ===== FUNCTIONS, MULTIPLE TABLES AND SUB-QUERIES

# Aggregate or column functions
# 1) takes a collection of like values (e.g. takes all the values in a column as input and returns a single value or null)
# 2) SUM(), MIN(), MAX(), AVG()

SELECT SUM(column_name) FROM table_name # gives back a small column with a given number, if you want that column to have an actual name do:
SELECT SUM(column_name) as column_name FROM table_name 

# Similarly:
SELECT MIN/MAX()

# Get min value of ID column for dogs:
SELECT MIN(ID) FROM Pets WHERE Animal = 'Dog'

# Calculate avg. cost per dog:
SELECT AVG(COST / QUANTITY) FROM Pets WHERE Animal = 'Dog'


# Scalar functions
# 1) perform operations on every input value:
# 2) ROUND(), LENGTH(), UCASE, LCASE
SELECT ROUND(column_name, decimal_places) FROM table_name
SELECT ROUND(Cost, 2) FROM Pets

SELECT UCASE(ANIMAL) FROM PETRESCUE # prints out all animal names in upper case
# Date and Time functions
# SQL contains DATE, TIME, TIMESTAMP types:
# DATE = 8 digits = YYYYMMDD
# Time has 6 = HHMMSS
# TIMESTAMP has 20 = YYYYXXDDHHMMSSZZZZZ where XX = month and ZZZZZ = microseconds

# To select a year from a given RescueDate column:
SELECT YEAR(RESCUEDATE) FROM PETRESCUE;

# To add 1 year to all dates in the rescuedate column:
SELECT DATE_ADD(RESCUEDATE, INTERVAL 1 YEAR) FROM PETRESCUE # to do days/months, keep everything the same, just change 1 year to idk 3 DAY 4 month

# Similarly
SELECT DATE_SUB(RESCUEDATE, INTERVAL 3 DAY) FROM PETRESCUE

# Difference between today and the dates in the table (in days)
SELECT DATEDIFF(CURRENT_DATE, RESCUEDATE) FROM PETRESCUE

# How much time has passed since each date in the column relative to current date)
SELECT FROM_DAYS(DATEDIFF(CURRENT_DATE, RESCUEDATE)) FROM PETRESCUE

# ===== Sub-queries and nested selects
# Query inside another query
# e.g.:
SELECT column1 FROM table WHERE column2 = (SELECT MAX(column2) FROM TABLE)

# Why use them? Say you want to select all employees where salary > avg(salary)
SELECT * FROM EMPLOYEES WHERE SALARY < AVG(SALARY)
# oh noes D: le *bigge erroré*, but wait! I know what to do:
SELECT * FROM EMPLOYEES WHERE SALARY < (SELECT AVG(SALARY) FROM EMPLOYEES);
# sub-query works :DD

# Another example: (first and last names of the oldest employee - smallest date of birth) 
SELECT F_NAME, L_NAME FROM EMPLOYEES WHERE B_DATE = (SELECT MIN(B_DATE) FROM EMPLOYEES);

# Another one: retreive job information for employees earning >$70,000.
# Retreive details from JOBS table, which has common IDs with those available in EMPLOYEES table, provided the salary
# in the EMPLOYEES table is greater than 70k, do:
SELECT JOB_TITLE, MIN_SALARY, MAX_SALARY, JOB_IDENT
FROM JOBS
WHERE JOB_IDENT IN (select JOB_ID from EMPLOYEES where SALARY > 70000 );

# Yet another one: (creating derived table - can be used to query specific info)
# Say you want to know avg salary of top 5 earners in company, you first extract a table of top 5 salaries as a table
# then, from that table you can query the avg vale of salary:
SELECT AVG(SALARY) 
FROM (SELECT SALARY 
      FROM EMPLOYEES 
      ORDER BY SALARY DESC 
      LIMIT 5) AS SALARY_TABLE;
# Note that it is necessary to give an alias to any derived tables.

# ===== WORKING WITH MULTIPLE TABLES
# Ways to access multiple tables in the same query:
# 1) sub-queries
# 2) implicit JOIN
# 3) JOIN operators (INNER JOIN, OUTER JOIN, and so on)

# e.g. Retreive JOB information and a list of employees whose b_year is after 1976:
# sub-query:
SELECT JOB_TITLE, MIN_SALARY, MAX_SALARY, JOB_IDENT
FROM JOBS
WHERE JOB_IDENT IN (SELECT JOB_ID
                    FROM EMPLOYEES
                    WHERE YEAR(B_DATE)>1976 );
# implicit join
SELECT J.JOB_TITLE, J.MIN_SALARY, J.MAX_SALARY, J.JOB_IDENT
FROM JOBS J, EMPLOYEES E
WHERE E.JOB_ID = J.JOB_IDENT AND YEAR(E.B_DATE)>1976;

# e.g. Retrieve only the list of employees whose JOB_TITLE is Jr. Designer
# Sub-query:
SELECT *
FROM EMPLOYEES
WHERE JOB_ID IN (SELECT JOB_IDENT
                 FROM JOBS
                 WHERE JOB_TITLE= 'Jr. Designer');
# Implicit joins:
SELECT *
FROM EMPLOYEES E, JOBS J # 
WHERE E.JOB_ID = J.JOB_IDENT AND J.JOB_TITLE= 'Jr. Designer';

# notice how we're assigning aliases in joins, helpful in cases where specific columns are to be accessed from different tables
# also notice how both sub-queries and joins give the same results :)

#============================================ Module 4 =======================================================================
# Creating & Accessing SQLite database using Python

# 1) Create database using SQLite
#Install & load sqlite3
#!pip install sqlite3 # uncomment if already installed
import sqlite3

# Connecting to sqlite
# connection object
conn = sqlite3.connect('INSTRUCTOR.db')

# cursor object
cursor_obj = conn.cursor() # cursor class is an instance using which you can invoke methods thay execute SQLite statements, fetch data from the result sets of the queries
# in other words, a cursor enables traversal over the records in a database

# 2) Create a table in the database:
table = """ create table IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2));"""
cursor_obj.execute(table)

# 3) Insert data into the table
cursor_obj.execute('''insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')''')

# 4) Query data in the table
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)

print("All the data")
output_all = cursor_obj.fetchall()
for row_all in output_all:
  print(row_all)
    
# If you want to fetch few rows from the table we use fetchmany(numberofrows) and mention the number how many rows you want to fetch
output_many = cursor_obj.fetchmany(2) # fetchmany instead of fetchall
for row_many in output_many:
  print(row_many)

# Fetch only FNAME from the table
statement = '''SELECT FNAME FROM INSTRUCTOR'''
cursor_obj.execute(statement)

print("All the data")
output_column = cursor_obj.fetchall()
for fetch in output_column:
  print(fetch)

# Change Rav's city to Moosetown
query_update='''update INSTRUCTOR set CITY='MOOSETOWN' where FNAME="Rav"'''
cursor_obj.execute(query_update)

statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)

print("All the data")
output1 = cursor_obj.fetchmany(1)
for row in output1:
  print(row)

# Retrive data into Pandas
import pandas as pd
#retrieve the query results into a pandas dataframe
df = pd.read_sql_query("select * from instructor;", conn)

df # print the dataframe

df.LNAME[0] # print just the LNAME for first row in the pandas data frame

df.shape # see how many rows and columns there are in the dataset

# Close the connection
conn.close() # VERY IMPORTANT, NEED TO AVOID UNUSED CONNECTIONS TAKING UP RESOURCES

# ===== SQL MAGIC
# Magic statements - special commands with special functionalities, not valid for Python but affect the behaviour of the notebook
# 2 types: Line Magic and Cell Magic
# Line Magic: Commands prefixed with a single % and operate on a single line of input
# In order to use SQL Magic, we need install some dependencies: 
# iPython-sql = !pip install --user ipython-sql
# Enable SQL Magic in Jupyter = %load_ext sql
# Syntax for connecting to magic sql using sqlite: %sql sqlite://DatabaseName (where DatabaseName will be your .db file)
# Cell Magic: 2 %% and operate on multiple lines of input
# examples:
%pwd # prints the current working directory
%ls # lists all files in the current directory
%history # shows command history
%reset # resets the namespace by removing all names defined by the user
%who # lists all variables in the namespace
%whos # provides more details about all variables in the namespace
%matplotlib inline # makes matplotlib appear within the notebook
%timeit # times the execution of a single statement
%ismagic # list of all available line magics

%timeit <statement> # time for executing single statement
%%timeit
<statement>
<statement>
<statement> # time for executing the multiple

# Mahic statement can also be run in other languages:
%%HTML # write HTML code in cells to render it

%%HTML
<h>Hello world</h1> # example

%%javascript # same but writes java script code

%%bash cell # bash commands, in command terminal

# ===== Using Python Variables in my SQL statements
# I can use python variables by adding a : prefix to my python variable names, e.g.:
country = "Canada"
%sql select * from INTERNATIONAL_STUDENT_TEST_SCORES where country = :country

# Assigning results of queries to Python variables works normallly:
test_score_distribution = %sql SELECT test_score as "Test_Score", count(*) as "Frequency" from INTERNATIONAL_STUDENT_TEST_SCORES GROUP BY test_score;
test_score_distribution

# Converting query results to dataframes (but why? because dataframes are much more versatile, we can use them to create *graphs* :3
dataframe = test_score_distribution.DataFrame()
%matplotlib inline
# uncomment the following line if you get an module error saying seaborn not found
# !pip install seaborn==0.9.0
import seaborn
plot = seaborn.barplot(x='Test_Score',y='Frequency', data=dataframe)

# example sql table: 
%%sql 
SELECT country, first_name, last_name, test_score FROM INTERNATIONAL_STUDENT_TEST_SCORES; 

# ================ Practice
# (in Jupyter)

# CONNECT TO THE DATABASE
%load_ext sql

import csv, sqlite3
con = sqlite3.connect("socioeconomic.db")
cur = con.cursor()
!pip install -q pandas==1.1.5

%sql sqlite:///socioeconomic.db # as mentioned before, this is the syntax for connecting to magic sql

# STORE DATASET IN A TABLE
import pandas
df = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
df.to_sql("chicago_socioeconomic_data", con, if_exists='replace', index=False,method="multi")

# Verify that it works
%sql SELECT * FROM chicago_socioeconomic_data

# PROBLEM 1) HOW MANY ROWS IN DATASET?
%sql SELECT COUNT(*) FROM chicago_socioeconomic_data

# PROBLEM 2) HOW MANY COMMUNITY AREAS IN CHICAGO HAVE A HARDSHIP INDEX GREATER THAN 50?
%sql SELECT COUNT(*) FROM chicago_socioeconomic_data WHERE hardship_index > 50.0;

# PROBLEM 3) MAXIMUM VALUE OF HARDSHIP IN THIS DATA
%sql SELECT MAX(hardship_index) FROM chicago_socioeconomic_data

# PROBLEM 4) WHICH COMMUNITY AREA HAS THE HIGHEST HARDSHIP INDEX
%sql SELECT community_area_name FROM chicago_socioeconomic_data WHERE hardship_index = 98.0 # we know it's 98.0 because result to PROBLEM 3
# or
%sql SELECT community_area_name FROM chicago_socioeconomic_data ORDER BY hardship_index DESC LIMIT 1;
# or use sub-query to determine max hardship index
%sql select community_area_name from chicago_socioeconomic_data
where hardship_index = ( select max(hardship_index) from chicago_socioeconomic_data );

# PROBLEM 5) WHICH CHICAGO COMMUNITY AREAS HAVE PER-CAPITA INCOMES GREATER THAN 60K?
%sql SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income_ > 60000;

# PROBLEM 6) CREATE A SCATTER PLOT USING THE VARIABLES per_capita_income AND hardship_index
# if the import command gives ModuleNotFoundError: No module named 'seaborn'
# then uncomment the following line i.e. delete the # to install the seaborn package 
# !pip install seaborn

import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

income_vs_hardship = %sql SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())

#============================================ Module 5 =======================================================================
# Working with Real World Datasets

# Prerequisites
import csv, sqlite3

con = sqlite3.connect("RealWorldData.db")
cur = con.cursor()

!pip install -q pandas==1.1.5

%load_ext sql

%sql sqlite:///RealWorldData.db

# Store dataset in a table
import pandas

df = pandas.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv")
df.to_sql("CHICAGO_PUBLIC_SCHOOLS_DATA", con, if_exists='replace', index=False, method="multi")

# Query database system to retreive table metadata - verify that table creation was successful by doing this:
%sql SELECT name FROM sqlite_master WHERE type='table'

# Query database system to retreive column metadata - shows how many columns there are
%sql SELECT count(name) FROM PRAGMA_TABLE_INFO('CHICAGO_PUBLIC_SCHOOLS_DATA');

# Retreive list of columns, column type and length:
%sql SELECT name,type,length(type) FROM PRAGMA_TABLE_INFO('CHICAGO_PUBLIC_SCHOOLS_DATA');

# Q/A

# Q1: How many Elementary Schools are there?
%sql select count(*) from CHICAGO_PUBLIC_SCHOOLS_DATA where "Elementary, Middle, or High School"='ES'
# A: 462


# Q2: What is the highest Safety Score?
%sql select MAX(Safety_Score) AS MAX_SAFETY_SCORE from CHICAGO_PUBLIC_SCHOOLS_DATA
# A: TABLE WITH MAX SCORE 99

# Q3: Which schools have highest Safety Score?
%sql select Name_of_School, Safety_Score from CHICAGO_PUBLIC_SCHOOLS_DATA where Safety_Score = 99
# A: LIST OF ALL SCHOOLS WITH HIGHEST SCORE

# Q4: What are the top 10 schools with the highest "Average Student Attendance"?
%sql select Name_of_School, Average_Student_Attendance from CHICAGO_PUBLIC_SCHOOLS_DATA \
    order by Average_Student_Attendance desc nulls last limit 10 
# A: LIST OF TOP 10 SCHOOLS

# Q5: List of 5 Schools with the lowest Average Student Attendance sorted in ascending order based on attendance
%sql SELECT Name_of_School, Average_Student_Attendance  \
     from CHICAGO_PUBLIC_SCHOOLS_DATA \
     order by Average_Student_Attendance \
     LIMIT 5
# A: ANOTHER LIST OF 5
    
# Q6: Now remove the '%' sign from the above result set for Average Student Attendance column
%sql SELECT Name_of_School, REPLACE(Average_Student_Attendance, '%', '') \
     from CHICAGO_PUBLIC_SCHOOLS_DATA \
     order by Average_Student_Attendance \
     LIMIT 5
# A: SAME LIST BUT NO % IN COLUMN AVG STUDENT ATTENDANCE
    
# Q7: Which Schools have Average Student Attendance lower than 70%? 
%sql SELECT Name_of_School, Average_Student_Attendance  \
     from CHICAGO_PUBLIC_SCHOOLS_DATA \
     where CAST ( REPLACE(Average_Student_Attendance, '%', '') AS DOUBLE ) < 70 \
     order by Average_Student_Attendance
# A: TABLE SIMILAR TO LAST 2 BUT AVG STUDENT ATTENDANCE IS <= 70%

# Q8: Get the total College Enrollment for each Community Area 
%sql select Community_Area_Name, sum(College_Enrollment) AS TOTAL_ENROLLMENT \
   from CHICAGO_PUBLIC_SCHOOLS_DATA \
   group by Community_Area_Name 
# A: 2 COLUMNS: COMMUNITY AREA NAME AND TOTAL ENROLLMENT
    
# Q9: Get the 5 Community Areas with the least total College Enrollment sorted in ascending order
%sql select Community_Area_Name, sum(College_Enrollment) AS TOTAL_ENROLLMENT \
   from CHICAGO_PUBLIC_SCHOOLS_DATA \
   group by Community_Area_Name \
   order by TOTAL_ENROLLMENT asc \
   LIMIT 5 
# A: SAME AS BEFORE BUT SMALLER AND GROUPED

# Q10: List 5 schools with lowest safety score.
%sql SELECT name_of_school, safety_score \
FROM CHICAGO_PUBLIC_SCHOOLS_DATA  where safety_score !='None' \
ORDER BY safety_score \
LIMIT 5
# A: SIMILAR TO ONE BEFORE

# Q11: Get the hardship index for the community area of the school which has College Enrollment of 4368
# A: N/A as for this solution to work, another table from last week should already exist

# Q12: Get the hardship index for the community area which has the highest value for College Enrollment
# A: N/A as for this solution to work, another table from last week should already exist

# Last bit of info:
You are provided with a python statement “df.to_sql(‘Sample’, conn)”. What do ‘df’, ‘Sample’ and ‘conn’ refer to?
df – data frame; Sample – table name ; conn – connection variable



