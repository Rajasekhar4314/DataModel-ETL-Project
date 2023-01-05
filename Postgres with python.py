#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install psycopg2')


# In[3]:


import psycopg2


# In[6]:


try:
    conn = psycopg2.connect("host =127.0.0.1 dbname=postgres user=postgres password=7997")
except Error as e:
    print("Error: Could not make connection to postgres database")
    print(e)



# In[7]:


try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get cursor to the database")
    print(e)


# In[8]:


conn.set_session(autocommit = True)


# In[9]:


try:
    cur.execute("create database myfirstdb")
except Error as e:
    print("Error: Could not able to execute database")
    print(e)


# In[14]:


try:
    conn.close()
except Exception as e:
    print("Error: Unable to close the connection")
    print(e)


# In[15]:


try:
    conn = psycopg2.connect("host =127.0.0.1 dbname=myfirstdb user=postgres password=7997")
except Error as e:
    print("Error: Could not make connection to postgres database")
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get cursor to the database")
    print(e)    

conn.set_session(autocommit = True)    
    


# In[18]:


try:
    cur.execute("CREATE TABLE IF NOT EXISTS STUDENTS \
                (student_id int, name varchar(100), age int, gender varchar(20), subject varchar(30), marks int);")
except psycopg2.Error as e:
    print("Error: Unable to create ta table")
    print(e)


# In[27]:


try: 
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject, marks) \
                 VALUES (%s, %s, %s, %s, %s, %s)", \
                 (1, "Raj", 23, "Male", "Python", 85))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO students2 (student_id, name, age, gender, subject, marks) \
                  VALUES (%s, %s, %s, %s, %s, %s)",
                  ( 2, "Priya", 22, "Female", "Python", 86))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)


# In[28]:


try:
    cur.execute("select * from students")
except Error as e:
    print("Error: Select *")
    
row = cur.fetchone()
while row:
    print(row)
    row= cur.fetchone()


# In[30]:


cur.close()
conn.close()


# In[ ]:




