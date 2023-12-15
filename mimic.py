from openai import OpenAI
import os
from os.path import join, dirname
from dotenv import load_dotenv
#import bigFive
import sys

if __name__ == "__main__":
    # Check if a file argument is provided
    if len(sys.argv) != 2:
        print("Usage: python mimic.py <text_file>")
        sys.exit(1)

    # Get the file path provided as an argument
    text_file = sys.argv[1] #takes name.txt as input argument

    # Process the text file
    name = text_file.split('.')[0]
    print("Hello. I am " + name + ". Enter 'Goodbye!' to stop talking to me.")

    file_path = "C:\Yale\CS488\project\Mimic\\" + text_file #IMPORTANT may need to change to actual directory

    try:
        with open(file_path, 'r') as file:
            analysis = file.read()
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    client = OpenAI(
    api_key='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',
    )
    text = ""
    cont = True
    while cont:
      userMessage = input("\nEnter: ")
      if userMessage == "Goodbye!":
        print("Goodbye to you!")
        cont = False
      
      response = client.chat.completions.create(
        model="gpt-3.5-turbo",

        messages = [
          {
            "role": "user",
            "content": "Let's do a role play. The user is a stranger trying to meet you. You are a person with the following psychological profile based on the five big psychological descriptors as well as an explanation for why they got that score: \n" + analysis + " \nanswer as this person would answer\n\n Message from user: " +
             userMessage + "\n\n Chatbot's response: ",
          }
        ],
        temperature=0.9, #create a more creative response than PC therapist
        max_tokens=256,
    
      )
      print("\n")
      print(response.choices[0].message.content)
      print("\n")

    text = text + "\n" + userMessage + "\n" +  response.choices[0].message.content + "\n"

    filePathMimic = name + "mimic.txt"
    with open(filePathMimic, 'w') as file:
      file.write(text)


    

