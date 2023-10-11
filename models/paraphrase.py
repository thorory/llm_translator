from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from .worker import Worker
import os

class Translator(Worker):
    prompt = ""

    def __init__(self, api_base, api_key, llm_model="gpt-3.5-turbo") -> None:
        super().__init__(api_base, api_key, llm_model)

    def load_prompt_template(self, prompt_template_dir='./prompts/paraphrase.txt'):
        if not os.path.exists(prompt_template_dir):
            raise FileNotFoundError("文件不存在")
        
        with open(prompt_template_dir, "r", encoding="utf-8") as f:
            self.prompt = f.read()

        return self.prompt
    
    def run(self, text=""):
        input_template = "{text}"
        chat_prompt = ChatPromptTemplate.from_messages([
            ("system", self.prompt),
        ])
        
        messages = chat_prompt.format_messages(passage = text)
        print(messages)
        return super().run(messages)