#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install nltk


# In[ ]:


from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I am just a chatbot. You can call me likhi.",]
    ],
    [
        r"how are you ?",
        ["I'm just a computer program, so I don't have feelings, but I'm here to help you.",]
    ],
    [
        r"what can you do for me ?",
        ["I can answer your questions, provide information, or just chat with you. How can I assist you today?",]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day.", "Farewell! Feel free to return if you have more questions."]
    ],
      [
        r"what does SKIT mean in SKITBOT?",
        ["SKIT means Sri Krishna Institute of Technology.",]
    ],
      [
        r"What is the average package of Sri Krishna Institute of Technology Bangalore?",
        ["he highest salary package offered was 15 LPA. The lowest salary package offered was 2.5 LPA. The average salary package offered was 8 LPA..",]
    ],
     [
        r"what are the courses in SKIT?",
        ["Artificial Intelligence and Machine Learning,Computer Science and Engineering,Information Science and Engineering,Electronics and Communication Engineering,Mechanical Engineering,Civil Engineering.",]
    ],
]

def chatbot():
    print("Hello! I'm SKITBOT, your friendly chatbot. Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":           # Start the chatbot
    chatbot()


# In[ ]:




