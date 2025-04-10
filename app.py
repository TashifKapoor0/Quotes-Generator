import json
import random
import sys
import threading
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

# Load quotes
def load_quotes():
    try:
        with open("quotes.json", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("Error loading quotes:", e)
        return {}

quotes = load_quotes()

# Map of keywords to categories
category_keywords = {
    "motivational": ["motivate", "motivation", "inspire", "inspiration", "driven", "focus", "grind"],
    "funny": ["funny", "laugh", "joke", "humor", "hilarious"],
    "love": ["love", "romantic", "relationship", "heart", "affection"],
    "sad": ["sad", "depressed", "down", "cry", "upset", "unhappy"],
    "life": ["life", "living", "exist", "reality", "journey"]
}

# Exit keywords
exit_keywords = ["exit", "bye", "quit", "goodbye"]

# Serve HTML page
@app.get("/", response_class=HTMLResponse)
async def home():
    try:
        with open("index.html", encoding="utf-8") as f:
            return f.read()
    except:
        return HTMLResponse(content="HTML file not found.", status_code=404)

# Shutdown function
def shutdown_server():
    print("Shutting down the server...")
    sys.exit()

# Handle quote requests
@app.get("/query")
async def get_quote(query: str = Query(...)):
    user_input = query.lower().strip()

    # Check for exit intent
    if any(word in user_input for word in exit_keywords):
        threading.Timer(1.0, shutdown_server).start()
        return {"quote": "Goodbye! Have a nice day 😊", "category": "exit"}

    words = user_input.split()
    matched_category = None

    # Check if user asked for multiple quotes
    num_quotes = 1
    for word in words:
        if word.isdigit():
            num_quotes = int(word)
            break

    # Match a category
    for category, keywords in category_keywords.items():
        if any(word in keywords for word in words):
            matched_category = category
            break

    if matched_category:
        selected_quotes = random.sample(quotes[matched_category], min(num_quotes, len(quotes[matched_category])))
        if num_quotes == 1:
            return {"category": matched_category, "quote": selected_quotes[0]}
        else:
            return {"category": matched_category, "quotes": selected_quotes}

    # Return suggestion message if no category matched
    return JSONResponse(
        status_code=404,
        content={
            "message": "Sorry, I didn’t understand. Try words like 'motivate', 'sad', 'funny', 'love', or 'life'."
        }
    )
