from openai import OpenAI
import os
from os.path import join, dirname
from dotenv import load_dotenv
#import bigFive

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
#client = OpenAI()

client = OpenAI(
   api_key='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',
)



# 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

cont = True #create infinite loop
print("Welcome to Psychoanaylsis chatbot. Type 'Goodbye!' to exit")

name = input("What is your name? ")

text = "" #only users inputs for psych report

totaltext = "" #create transcript of whole convo
while cont:
  userMessage = input("\nEnter: ")
  if userMessage == "Goodbye!": #end convo when you see this typed
    cont = False
  text = text + userMessage
  
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",

    messages = [
      {
          "role": "user",
          "content": "You are a psychologist chatbot. The user asked you the following message. Please respond with a question to the user. Question should be about getting to know user's personality on a very deep level.\n\n Message from user: " +
           userMessage + "\n\n Chatbot's response: ",
      }
    ],
    temperature=0.3, #convo needs to be boring
    max_tokens=256,
    
  )
  print("\n")
  print(response.choices[0].message.content)
  print("\n")
  totaltext = totaltext + "\n" + userMessage + "\n" + response.choices[0].message.content

analysis = client.chat.completions.create(
    model="gpt-3.5-turbo",

    messages = [
      {
          "role": "user",
          "content": "You are a chatbot. Your job is to take the following text and rate the user on a percentage on the following personality traits: Openness, Consciousnes, Extraversion, Agreeableness and Neuroticism. Give a detailed reason for why each catagory is the way it is \n" +
           text + "\n\n Chatbot's response: ",
      }
    ],
    temperature=0.3,
    max_tokens=1000, #for a detailed response
    
  )

print("\nYour analysis is:\n")
print(analysis.choices[0].message.content)

file_path = name + ".txt"
file_pathRecord = name + "Record.txt"

# Open the file in write mode and write the string
with open(file_path, 'w') as file:
    file.write(analysis.choices[0].message.content)

with open(file_pathRecord, 'w') as file:
    file.write(totaltext)