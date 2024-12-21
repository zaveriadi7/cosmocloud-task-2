import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from redis import Redis, RedisError

# Load environment variables from the .env file
load_dotenv()

# Get the Redis URI from the environment variables
REDIS_URI = os.getenv("REDIS_URI")

if not REDIS_URI:
    raise ValueError("REDIS_URI environment variable not set")

# Initialize Redis client
try:
    client = Redis.from_url(REDIS_URI, decode_responses=True)
    # Test Redis connection
    client.ping()
    print("Connected to Redis")
except RedisError:
    raise ConnectionError("Failed to connect to Redis")

# Initialize FastAPI app
app = FastAPI()

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Root endpoint to increment and return hits count
@app.get("/")
def read_root():
    try:
        hits = client.incr("hits")
        return {"hits": hits}
    except RedisError:
        raise HTTPException(status_code=500, detail="Redis error")
