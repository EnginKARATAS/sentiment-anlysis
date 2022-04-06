import os #package that allows to access env. variables
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

print(os.getenv("API_KEY"))

print(os.getenv("cloud_id"))
print(os.getenv("user"))
print(os.getenv("password"))