import ollama
from src.utils.main_logger import logger_general, logger_error

def ask_ai(question):
    try:
        query = str(question)
        logger_general.debug(f"query: {query}")
        logger_general.info("memulai pengambilan response")
        response = ollama.chat(
            model="llama3.1:latest",
            messages=[
                {
                    "role": "user", 
                    "content": query
                    }
            ]
        )
        logger_general.info("response telah diambil")
        logger_general.debug(f"response : {response['message']['content']}")
        return response['message']['content']
    except Exception as e:
        logger_error.error(e)
        return "Error: " + str(e)