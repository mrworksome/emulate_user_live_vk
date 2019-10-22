import os

SELENIUM = (
    "./chromedriver" if "SELENIUM" not in os.environ else os.environ.get("SELENIUM")
)
GRPC_HOST = (
    "localhost:50551" if "GRPC_HOST" not in os.environ else os.environ.get("GRPC_HOST")
)
HOST = "localhost" if "HOST" not in os.environ else os.environ.get("HOST")
PORT = 6379 if "PORT" not in os.environ else os.environ.get("PORT")
DB = 1 if "DB" not in os.environ else os.environ.get("DB")
