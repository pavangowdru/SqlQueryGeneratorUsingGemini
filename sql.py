from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#Function to load Google gemini ai model

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

#function to retrive query from database

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

#define your prompt
prompt=[
    """
    You are an expert in converting English sentences to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION \n\n For example,\n Example 1 - How many entries of records are present?,
    the SQL command will be something likw this SELECT COUNT(*) FROM STUDENT;
    \n EXAMPLE 2 - Tell me all the students studying in Data Science class?,
    the SQL command will be something like this SELECT * FROM STUDENT where CLASS="DATA Science";
    also the sql code should not have ``` in beginning or end and sql qord in output
    """
]

#streamlit app

st.set_page_config(page_title="I can retrieve any SQL wquery")
st.header("Gemini APp to Retrieve SQL DATA")

question=st.text_input("Input : ", key="input");

submit = st.button("Ask the question")

#when submit is clicked
if (submit):
    query = get_gemini_response(question, prompt)
    print(query) 
    response = read_sql_query(query, "student.db")
    st.subheader("The response is")
    for row in response:
        print(row)
        st.header(row)

