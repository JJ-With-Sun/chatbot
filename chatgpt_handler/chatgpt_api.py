import os
from openai import AzureOpenAI
import json
from dotenv import load_dotenv
import time

load_dotenv('.env')
# # JSON 파일에서 API 키를 불러오는 함수
# def load_api_keys(file_path):
#     with open(file_path, 'r') as file:
#         return json.load(file)

# API_KEYS_FILE_PATH = "./credentials/api_keys.txt"
# api_keys = load_api_keys(API_KEYS_FILE_PATH)

# generation_config, safety_settings 설정
generation_config = {
  "temperature": 0,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 128
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE",
  }
]

criteria = './instructions/grading_criteria.txt'

grading = './instructions/grading.txt'


class ChatGPTAPI:
    def __init__(self, 
                 generation_config = generation_config, model:str = "543c7b3a-a3c3-495c-9ec5-8e36c3f314e4") -> None:
      self.model = model
      self.generation_config = generation_config
      self.client = AzureOpenAI(api_key = os.getenv('API_KEY'),
                                api_version = os.getenv('API_VERSION'),
                                azure_endpoint = os.getenv('AZURE_ENDPOINT')
                                )
      
    def gradings(self, guideline:str, self_introduction_1:str, self_introduction_2:str):
      with open('./instructions/grading.txt', 'r') as f:
        data = f.read()
        data = data.format(guideline=guideline, self_introduction_1=self_introduction_1, self_introduction_2=self_introduction_2)
        messages = [{"role": "user", "content": data}]
        start = time.time()
        response = self.client.chat.completions.create(model=self.model, messages=messages, 
                                                  temperature = generation_config['temperature'], 
                                                  top_p = generation_config['top_p'],
                                                  max_tokens = generation_config['max_output_tokens'] )
        end = time.time()
        print(f'generation time: {end-start}')
        output = response.choices[0].message.content
        return output