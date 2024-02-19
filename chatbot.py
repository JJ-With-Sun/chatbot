from openai import AzureOpenAI
from dotenv import load_dotenv

dotenv_path = '/home/kic/yskids/service/app/credentials/.env'
load_dotenv(dotenv_path)

generation_config = {
    "temperature": 0.3,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048
    }

class Chatbot:
    def __init__(self, 
                company:str = "KPMG"):
        self.path = f"/home/kic/yskids/service/data/{company}"
        with open(f'{self.path}/instruction.txt', 'r') as f:
            self.data = f.read()
        with open(f'{self.path}/company_project_info.txt', 'r') as f:
            self.company_project_info = f.read()
        
        self.client = AzureOpenAI(api_key = os.getenv('AZURE_API_KEY'),
                            api_version = os.getenv('AZURE_API_VERSION'),
                            azure_endpoint = os.getenv('AZURE_ENDPOINT')
                            )
        
    def information(self, question:str):
        data = self.data.format(information=self.company_project_info, question = question)
        messages = [{"role": "user", "content": data}]
        response = self.client.chat.completions.create(model=os.getenv('AZURE_DEPLOYMENT'), messages=messages, 
                                                    temperature = generation_config['temperature'], 
                                                    top_p = generation_config['top_p'],
                                                    max_tokens = generation_config['max_output_tokens'] )
        output = response.choices[0].message.content
        return output

if __name__ == '__main__':
    
    a = Chatbot("KPMG")
    a.information("What is your company project?")
    while True:
        question = input('질문을 입력하세요: ')
        print(a.information(question))