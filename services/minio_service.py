from datetime import timedelta

from minio import Minio
from utils.config import MinioConfig
from utils.logger import logger


class MinioService:
    def __init__(self):
        self._client = Minio(
            MinioConfig.MINIO_ENDPOINT,
            access_key=MinioConfig.ACCESS_KEY,
            secret_key=MinioConfig.SECRET_KEY,
            secure=False
        )

    def get_presigned_ur(self, object_name):
        logger.debug("Fetching presigned url")
        return self._client.presigned_get_object(
            bucket_name=MinioConfig.BUCKET_NAME,
            object_name=object_name,
            expires=timedelta(seconds=MinioConfig.EXPIRATION_SECONDS)
        )
