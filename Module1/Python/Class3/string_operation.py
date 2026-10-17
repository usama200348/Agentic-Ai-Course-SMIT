import os

# STRING OPERATION IN PYTHON PROGRAMMING
course = 'Agentic AI';
# Before UPPER
print("Normal ",course)
# AFTER UPPER
print("UPPER",course.upper())
print("Checing If The String Is In Upper OR NOt",course.isupper())

# Before Lower
print("Normal Before Lower",course)
# AFTER Lower
print("Lower ",course.lower())
# Before Title
print("Normal Before Title",course)
# AFTER Title
print("Title",course.title())
# Checking String Is In lower or not

print("Checing If The String Is In Lower OR NOt",course.islower());
print("Checing IF THe String is is number of not" , course.isnumeric())
print("Checing IF THe String is is Alphabets of not" , course.isalpha())


Description  = '''
I'm a Data & AI Engineer who builds both the data platforms and the AI that runs on them.
I came up through data science and national competitions, then spent the last four years deep in production data engineering. I've built pipelines, lakehouses and warehouses on Azure, Snowflake, Databricks and AWS for healthcare and FMCG teams, plus the RAG, ML and decision-support systems that sit on top. The pattern I keep seeing is simple: AI only works when the data underneath it does, so I build both layers.
'''
print(Description);


# To Close
os.system('cls')
# Slicing
courses = 'Agentic AI'
print(courses);
#  01234556789
# 02134591207
print(courses[0:3])
# Fist starting And after : it's excluded
# [start:end:interval];


# STart to AN END
print(courses[:6]);
print(courses[:-5]);
# Index OF AN END
print(courses[7:])
print(courses[-3:])
print(courses[-2:])

# Interval (ek chor ka dosra)
print(courses[::2])
# Interval (ek chor ka tesra)
print(courses[::3])
# Interval second sa start minus tak jaoo or interval on 3
# Agentic AI
# print(courses[0:3,7:9]) Error

print(courses[:3],courses[7:]);
print(courses[:3]+courses[7:],end='This Is The End');
# Ending State Print khatam hoo aus ka bad bhe kuch likhna ya lagana hoo 
