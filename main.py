## sudo pipenv install llama-index-readers-file
## sudo pipenv install llama-index-readers-web
from llama_index import SimpleWebPageReader

import os
from dotenv import load_dotenv
# from llama_index import SimpleWebPageReader,VectorStoreIndex     # outdated now
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex
# from llama_index.core.readers.file.base import SimpleWebPageReader


if __name__ == "__main__":
    load_dotenv()
    print ("Hello world llama-index course")
    print (f'OPENAI_API_KEY : {os.environ["OPENAI_API_KEY"]}')