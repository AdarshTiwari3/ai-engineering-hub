from llm.client import create_llm
from prompts.prompts import PROMPT


def create_chain():
    llm = create_llm()
    return PROMPT | llm
