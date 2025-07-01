import json
import redis
import fakeredis
from fastapi import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

USE_FAKE_REDIS = os.getenv("USE_FAKE_REDIS", "true").lower() == "true"

try:
    if USE_FAKE_REDIS:
        r = fakeredis.FakeStrictRedis()
    else:
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.ping()
    print("✅ Redis connection successful.")
except redis.exceptions.ConnectionError:
    print("❌ Redis connection failed. Using fallback.")
    r = None  # Redis is down

def get_books_cache():
    if not r:
        print("⚠️ Redis not available")
        return None
    try:
        books_json = r.get("books")
        if books_json:
            print("📦 Cache HIT")
            return json.loads(books_json)
        else:
            print("📦 Cache MISS. Fetching from DB...")
    except Exception as e:
        print(f"⚠️ Redis cache read error: {e}")
    return None

def set_books_cache(data):
    if not r:
        print("⚠️ Redis unavailable")
        return
    try:
        json_data = json.dumps(data)
        r.set("books", json_data, ex=30)  # expire in 5 mins
        print("✅ Cache SET")
    except Exception as e:
        print(f"⚠️ Redis WRITE error: {e}")
