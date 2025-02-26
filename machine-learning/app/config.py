from pydantic import BaseSettings

class Settings(BaseSettings):
    cache_folder: str = "/cache"
    classification_model: str = "microsoft/resnet-50"
    clip_image_model: str = "clip-ViT-B-32"
    clip_text_model: str = "clip-ViT-B-32"
    facial_recognition_model: str = "buffalo_l"
    min_tag_score: float = 0.9
    eager_startup: bool = True
    model_ttl: int = 300
    host: str = "0.0.0.0"
    port: int = 3003
    workers: int = 1
    min_face_score: float = 0.7

    class Config(BaseSettings.Config):
        env_prefix = 'MACHINE_LEARNING_'
        case_sensitive = False


settings = Settings()
