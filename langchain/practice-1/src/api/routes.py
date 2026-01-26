import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi.responses import StreamingResponse

from chain.chain import create_chain

logger = logging.getLogger(__name__)

router = APIRouter()
chain = create_chain()


class AskQuestion(BaseModel):
    question: str


class AskResponse(BaseModel):
    answer: str


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/ask_question", response_model=AskResponse)
def ask_question(req: AskQuestion):
    try:
        answer = chain.invoke({"question": req.question})
        return {"answer": answer}

    except Exception as e:
        logger.exception("LLM execution failed")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/ask_question-stream")
def ask_question_stream(req: AskQuestion):
    try:

        def token_generator():
            for token in chain.stream({"question": req.question}):
                yield token

        return StreamingResponse(token_generator(), media_type="text/plain")

    except Exception as e:
        logger.exception("Streaming failed")
        raise HTTPException(status_code=500, detail=str(e))
