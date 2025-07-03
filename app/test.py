from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('secret_key')
print(key)