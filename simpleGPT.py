import openai
from dotenv import load_dotenv
import os
import re

load_dotenv('.env')
client = openai.OpenAI(
    api_key = os.getenv('APIKEY'),
    base_url ="https://api.openai.iniad.org/api/v1"
)

class GPT:
    def __init__(self, prompt=None, model=None):
        self.prompt = prompt
        self.model = model
        self.history = [{"role": "system","content": ("Your best System" if self.prompt is None else self.prompt)}]

    def Res(self, question):
        self.His_add('user', question)
        answer = common_process(question, self.model, self.prompt, self.history)
        self.His_add('system', answer)
        return answer
    
    def Get_his(self, AI_name=None, user_name=None):
        result = ""
        AI_name = "system" if AI_name is None else AI_name
        user_name = "user" if user_name is None else user_name
        for i in self.history:
            speaker = AI_name if i['role'] == "system" else user_name
            result += f"{speaker}: {i['content']}\n\n"
        return result
    
    def His_add(self, role, content):
        self.history.append({'role': role, 'content': content})

    @classmethod
    def ResSimple(cls, question):
        return common_process(question)


def common_process(question, model=None, prompt=None, history = None):
    if history is None:
        messages = [
            {"role": "system",
                "content": ("Your best System" if prompt is None else prompt)},
            {'role':'user',
            'content': question},
        ]
    else:
        messages = history

    response = client.chat.completions.create(
        model = "gpt-4o-mini" if model is None else model,
        messages = messages
    )
    return response.choices[0].message.content
