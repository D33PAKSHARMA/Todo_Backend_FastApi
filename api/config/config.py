from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    secret_key:str
    algorithm:str
    access_token_expire_minutes: int = 30
    
    model_config = SettingsConfigDict(env_file=".env")
    
settings = Setting()