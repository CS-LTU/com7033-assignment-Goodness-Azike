from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_USERNAME = os.getenv("mongo_user")
MONGODB_PASSWORD = os.getenv("mongo_password")
MONGODB_CLUSTER = os.getenv("mongo_cluster")
MONGODB_DB_NAME = os.getenv("mongo_name")

stroke_collection = None
client = None
db = None


def init_mongo():
    """
    Initialise MongoDB connection if configuration is present.

    MongoDB is optional:
    - If env vars are missing, the app skips Mongo and continues with MySQL.
    - If connection fails, it logs the error and keeps stroke_collection = None.
    """
    global client, db, stroke_collection

    if not all([MONGODB_USERNAME, MONGODB_PASSWORD, MONGODB_CLUSTER, MONGODB_DB_NAME]):
        print("MongoDB not configured. Skipping Mongo connection.")
        stroke_collection = None
        return

    mongodb_uri = (
        f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}"
        f"@{MONGODB_CLUSTER}/?retryWrites=true&w=majority"
    )

    try:
        client = MongoClient(
            mongodb_uri,
            serverSelectionTimeoutMS=3000,
            tls=True,
            tlsAllowInvalidCertificates=False,
            tlsAllowInvalidHostnames=False,
        )

        client.admin.command("ping")

        db = client[MONGODB_DB_NAME]
        stroke_collection = db["stroke_data"]

        print("MongoDB connection initialised successfully.")

    except ConnectionFailure as e:
        print(f"MongoDB connection failure: {e}")
        client = None
        db = None
        stroke_collection = None
    except Exception as e:
        print(f"MongoDB connection error: {e}")
        client = None
        db = None
        stroke_collection = None


init_mongo()


