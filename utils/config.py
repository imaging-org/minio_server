from dataclasses import dataclass
from os import getenv


@dataclass
class MinioConfig:
    MINIO_ENDPOINT = getenv("MINIO_ENDPOINT", "localhost:9000")
    ACCESS_KEY = getenv("ACCESS_KEY", "myX1pg4oZSIGvf0bE8jy")
    SECRET_KEY = getenv("SECRET_KEY", "GFzxcPO0kvPI1j2SdegLdTG9peUYZ8RvdOzLl93Q")
    BUCKET_NAME = getenv("BUCKET_NAME", "test-bucket")
    EXPIRATION_SECONDS = int(getenv("EXPIRATION_SECONDS", 3600))
