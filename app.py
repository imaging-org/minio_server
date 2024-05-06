import json

from flask import Flask, request, Response
from flask_cors import CORS
from utils.logger import logger

from services.minio_service import MinioService

app = Flask(__name__)
CORS(app)
minio_client = MinioService()


@app.post("/get_presigned_url")
def get_presigned_url():
    try:
        object_name = request.json.get("object_name")
        if object_name is None:
            raise ValueError("Object name is not valid")

        presigned_url = minio_client.get_presigned_ur(object_name=object_name)

        return Response(
            status=200,
            response=json.dumps({
                "presigned_url": presigned_url
            })
        )
    except Exception as err:
        logger.error(f"Error in getting presigned url : {err}")
        return Response(
            status=500,
            response=json.dumps({
                "error": str(err)
            })
        )


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=9191)
