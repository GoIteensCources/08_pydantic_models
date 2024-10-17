from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="allow"
    )

    DEBUG: bool = False
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "temp"

    def pg_dsn(self):
        return (f"postgres://{self.DB_USER}:{self.DB_PASSWORD}"
                f"@localhost:5432/{self.DB_NAME}")

    def sqlite_dsn(self):
        return f"sqlite3:///./{self.DB_NAME}.db"


settings_app = Settings()

DATABASE_URL = settings_app.sqlite_dsn()
