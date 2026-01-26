import logging
from langchain_community.llms.ollama import Ollama

from config.settings import MODEL_NAME, TEMPERATURE, OLLAMA_BASE_URL

logger = logging.getLogger(__name__)


def create_llm():
    logger.info("Initializing LLM: %s", MODEL_NAME)
    return Ollama(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        base_url=OLLAMA_BASE_URL,
    )
