from openai import OpenAI
from config import apikey
client = OpenAI(api_key=apikey)

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="write a email for bass",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
# print

# import openai
# from config import apikey
# openai.api_key=apikey
#
# response = openai.Completion.create(
#   model="gpt-3.5-turbo-instruct",
#   prompt="write a email for bass",
#   temperature=0.7,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )

print(response)