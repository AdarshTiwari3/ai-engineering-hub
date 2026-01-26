from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import StreamingResponse

import logging

from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import PromptTemplate


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# model configuaration

MODEL_NAME = "llama3:latest"
TEMPERATURE = 0.1


# LLM Setup


def create_llm():
    logger.info("Initializing LLM: %s", MODEL_NAME)
    return Ollama(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        base_url="http://localhost:11434",
    )


# prompt


PROMPT = PromptTemplate(
    input_variables=["question"],
    template="""
You are a helpful assistant.
Answer clearly and concisely.

Question: {question}
Answer:
""",
)


"""A chain creates an execution pipeline that takes structured input, applies prompt templating to provide proper context and instructions, sends the formatted prompt to the LLM, and returns the generated respon"""


def create_chain():
    llm = create_llm()
    return PROMPT | llm


chain = create_chain()


# --------- Fast API ---------

app = FastAPI(title="Local LLaMA API", version="1.0.0", docs_url="/docs")


class AskQuestion(BaseModel):
    question: str


class AskResponse(BaseModel):
    answer: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask_question", response_model=AskResponse)
def ask_question(req: AskQuestion):
    try:
        answer = chain.invoke({"question": req.question})
        return {"answer": answer}
    except Exception as e:
        logger.exception("LLM Execution failed")
        raise HTTPException(status_code=500, detail=str(e))


"""This endpoint sends the LLM response token by token (streaming) instead of waiting for the full answer."""


@app.post("/ask_question-stream", response_model=AskQuestion)
def ask_question_stream(req: AskQuestion):
    """Get the response word by word like ChatGPT"""

    try:

        def token_generator():
            for token in chain.stream({"question": req.question}):
                yield token

        return StreamingResponse(token_generator(), media_type="text/plain")

    except Exception as e:
        logger.exception("Streaming failed")
        raise HTTPException(status_code=500, detail=str(e))
