
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate

import os

class Worker():
    def __init__(self, api_base, api_key, llm_model="gpt-3.5-turbo") -> None:
        self.llm_model = llm_model
        self.api_base = api_base
        self.api_key = api_key

        os.environ["OPENAI_API_KEY"] = self.api_key
        os.environ["OPENAI_API_BASE"] = self.api_base

        print(self.api_key)
        print(self.api_base)

        self.chatBot = ChatOpenAI(model = self.llm_model)

        pass

    def llm_model(self):
        return self.llm_model
    
    def api_base(self):
        return self.api_base
    
    def api_key(self):
        return self.api_key
    
    def run(self, prompt):
        return self.chatBot.predict_messages(prompt)
    

