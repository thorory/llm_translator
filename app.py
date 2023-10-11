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
translator.load_prompt_template()

text = """
This paper examines the causes and satisfaction consequences of work-to-family \ 
and family-to-worksynergy for a sample of organizationally-employed parents while \ 
controlling two types of work-familyconflict: work interfering with family and family \ 
interfering with work. Participants included 1193respondents from the 2002 National \ 
Study of the Changing Workforce who had a child under the age of 18years at home. \ 
Work-family synergy is the frequency of experiencing positive energy and mood states \ 
fromparticipating in both work and family. Synergy was significantly related to attitude \ 
toward employerlearning opportunities, autonomy, job pressure, supervisor support, dependent \ 
care, family income, mentalhealth, self-rated health, and satisfaction outcomes. Gender \ 
similarities and differences in work-familysynergy were identified. Implications and directions \ 
for future research are discussed.
"""

resposne = translator.run(input_language="English", output_language="Chinese", text=text)
print(resposne)