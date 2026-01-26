from langchain_core.prompts import PromptTemplate


PROMPT = PromptTemplate(
    input_variables=["question"],
    template="""
You are a helpful assistant.
Answer clearly and concisely.

Question: {question}
Answer:
""",
)
