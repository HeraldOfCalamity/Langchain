from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from files import get_new_at_index
from config import OPENAI_API_KEY


llm = OpenAI(
    api_key=OPENAI_API_KEY,
)

summary_template_1 = PromptTemplate.from_template(
    """Summarize this text: {news_text}"""
)
summary_template_2 = PromptTemplate.from_template(
    """Process this text: {news_text}, then make a report like this: 
                                                  Title: (Title of the text or main topic)
                                                  Keywords: (Keywords of the text)
                                                  Word count: (Number of words does the text has)
                                                  Paragraph count: (Number of paragraphs does the text has)
                                                  Summary: (A clear, concise summary of the text)"""
)
summary_template_3 = PromptTemplate.from_template(
    """Process this text: {news_text}, then make a report like this, where the summary is mandatory: 
                                                  Title: (Title of the text or main topic)\n
                                                  Keywords: (Most important keywords of the text)\n
                                                  Word count: (Number of words does the text has)\n
                                                  Paragraph count: (Number of paragraphs does the text has)\n
                                                  Summary: (Summary of the text).\n"""
)
summary_template_4 = PromptTemplate.from_template(
    """Process this text: {news_text}, then make a report like this, where the summary is mandatory: 
                                                  Title: (Title of the text or main topic)\n
                                                  Word count: (Number of words does the text has)\n
                                                  Paragraph count: (Number of paragraphs does the text has)\n
                                                  Summary: (Summary of the text)."""
)
summary_template_5 = PromptTemplate.from_template(
    """Process this text (text between: ```): ```{news_text}``` Then make a report like this, where the summary is mandatory: 
                                                  Title: (Title of the text or main topic)\n
                                                  Word count: (Number of words does the text has)\n
                                                  Paragraph count: (Number of paragraphs does the text has)\n
                                                  Summary: (Summary of the text)."""
)


news = get_new_at_index(4)


prompt1 = summary_template_1.format(news_text=news)
prompt2 = summary_template_2.format(news_text=news)
prompt3 = summary_template_3.format(news_text=news)
prompt4 = summary_template_4.format(news_text=news)
prompt5 = summary_template_5.format(news_text=news)


response = llm.invoke(prompt5)

print(response)
print("========================================")
print(f"| News length: {len(news.split(' '))}             |")
print(f"| Response length: {len(response)}     |")
print("========================================")
