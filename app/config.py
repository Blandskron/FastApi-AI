from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    LLM_MODEL_PATH: str = "EleutherAI/gpt-neo-1.3B"  # Define LLM_MODEL_PATH
    ELASTICSEARCH_URL: str = "http://localhost:9200"
    elasticsearch_index: str = "my_index"

    class Config:
        env_file = ".env"

settings = Settings()
