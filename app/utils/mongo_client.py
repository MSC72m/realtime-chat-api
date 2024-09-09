from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

# Initialize the MongoDB client
mongo_client = AsyncIOMotorClient("mongodb://localhost:27017")
db = mongo_client["chat_app"]

# Initialize the ODMantic engine
engine = AIOEngine(motor_client=mongo_client, database="chat_app")