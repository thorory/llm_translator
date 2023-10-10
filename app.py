import os
import json
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import ChatPromptTemplate
from models.translator import Translator

llm_model = "gpt-3.5-turbo"


if not os.path.exists('config.json'):  
    raise FileNotFoundError("文件不存在")

with open('config.json', "r", encoding="utf-8") as f:
    data = json.load(f)

translator = Translator(api_key=data['api_key'], api_base=data['api_base'])
resposne = translator.run("this is a test")
print(resposne)