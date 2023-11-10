#!/usr/bin/env python
# coding: utf-8

# # Day1

# In[1]:


import re
import PyPDF2
sentence1="Here it is phone:1234567890,asd@fgh.com"
sentence2="1234567890,asd@gdhsg.com"
sentence3="(123)-456-7890,fgf@jidhf.com"
pattern1=r'\d{10}|\(\d{3}\)-\d{3}-\d{4}'
pattern2=r'[a-zA-Z0-9]*@[a-z]*\.com'
pattern3=r'age(\d+)'


# In[2]:


pattern =r'\d{10}'
match=re.findall(pattern,sentence1)
match


# In[3]:


match2=re.findall(pattern2,sentence2)
match2


# In[4]:


match3=re.findall(pattern2,sentence1)
match3


# In[5]:


text='''Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner and CTO of X, formerly Twitter
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)'''


# In[6]:


f = open("abc.txt",'a')
f.write(text)
f.close()
pattern5="age (\d+)"
match5=re.findall(pattern5,text)
match5


# In[7]:


pattern5="Born(.*)"
match5=re.findall(pattern5,text)
match5[0].strip() #remove white spaces


# In[8]:


pattern5="Born.*\n(.*)\(age"
match5=re.findall(pattern5,text)
match5[0].strip()


# In[9]:


pattern5="\(age.*\n(.*)"
match5=re.findall(pattern5,text)
match5[0].strip()


# In[10]:


def get_pattern_match(pattern5,text):
    match5=re.findall(pattern5,text)
    if match5:
        return match5[0]


# In[11]:


get_pattern_match('\(age.*\n(.*)',text)


# In[12]:


def get_personal_information(text):
    Age=get_pattern_match('age (\d+)',text)
    Name=get_pattern_match('Born(.*)',text)
    Dateofbirth=get_pattern_match('Born.*\n(.*)\(age',text)
    Birthplace=get_pattern_match('\(age.*\n(.*)',text)
    return{
        Age:int(Age),
        Name:Name.strip(),
        Dateofbirth:Dateofbirth.strip(),
        Birthplace:Birthplace.strip()
    }


# In[13]:


get_personal_information(text)


# In[ ]:




