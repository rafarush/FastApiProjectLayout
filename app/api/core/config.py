from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = 'PeopleApi'
    PROJECT_VERSION: str = '0.0.1'
    DATABASE_URL: str
    
    class Config:
        env_file = '.env'
        
settings = Settings()