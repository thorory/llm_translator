from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from .worker import Worker
import os

class Translator(Worker):
    prompt = ""

    def __init__(self, api_base, api_key, llm_model="gpt-3.5-turbo") -> None:
        super().__init__(api_base, api_key, llm_model)

    def load_prompt_template(self, prompt_template_dir='./prompts/translator.txt'):
        if not os.path.exists(prompt_template_dir):
            raise FileNotFoundError("文件不存在")
        
        with open(prompt_template_dir, "r", encoding="utf-8") as f:
            self.prompt = f.read()

        return self.prompt
    
    def run(self, text="", input_language="English", output_language="Chinese"):
        input_template = "{text}"
        chat_prompt = ChatPromptTemplate.from_messages([
            ("system", self.prompt),
            ("human", input_template),
        ])

        messages = chat_prompt.format_messages(input_language=input_language, output_language=output_language, text=text)
        print(messages)
        return super().run(messages)