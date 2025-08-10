import openai
from dotenv import load_dotenv
import os


load_dotenv('.env')
client = openai.OpenAI(
    api_key = os.getenv('APIKEY'),
    base_url ="https://api.openai.iniad.org/api/v1"
)

class GPT:
    def __init__(self, prompt=None, model="gpt-4o-mini"):
        self.prompt = prompt
        self.model = model
        self.history = [{"role": "system", 
                         "content": ("Your best System" if self.prompt is None else self.prompt)}]

    def res(self, question):
        self._add_to_history('user', question)
        answer = common_process(self.history, self.model)
        self._add_to_history('assistant', answer)
        return answer

    def get_str_history(self,drop_first_question = False, user_name="user", AI_name="assistant"):
        result = ""
        start_index = 1 if drop_first_question == False else 2
        for i in self.history[start_index:]:
            speaker = AI_name if i['role'] == "assistant" else user_name
            result += f"{speaker}: {i['content']}\n\n"
        return result
    
    def get_dict_history(self,drop_first_question = False, user_name="user", AI_name="assistant"):
        return self.history

    def reset_history(self):
        self.history = [self.history[0]]

    def _add_to_history(self, role, content):
        self.history.append({'role': role, 'content': content})

    @classmethod
    def res_simple(cls, question, model="gpt-4o-mini"):
        messages = [
            {"role": "system",
             "content": "Your best System"},
            {'role':'user',
            'content': question},
        ]
        return common_process(messages, model)


def common_process(messages, model="gpt-4o-mini"):
    response = client.chat.completions.create(
        model = model,
        messages = messages
    )
    return response.choices[0].message.content
