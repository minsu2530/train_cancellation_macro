from pydantic_config import SettingsModel, SettingsConfig

class Settings(SettingsModel):
    platform: str
    id: str
    password: str
    departure_loc: str
    arrival_loc: str
    date: str
    time: str
    discord_webhook: str

    model_config = SettingsConfig(
        config_file=['config.json']
    )

config = Settings()

def get_config() -> Settings:
    return config