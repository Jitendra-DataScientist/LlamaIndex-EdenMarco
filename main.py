import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv
    print ("Hello world llama-index course")
    print (f'OPENAI_API_KEY : {os.environ["OPENAI_API_KEY"]}')