from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # You can change this to "http://127.0.0.1:5500"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Feedback Model
class Feedback(BaseModel):
    student_name: str
    topic: str
    rating: int
    comment: str

# GET request
@app.get("/feedback")
def get_feedback():
    return {
        "message": "Use POST request to submit feedback."
    }

# POST request
@app.post("/feedback")
def submit_feedback(feedback: Feedback):
    return {
        "message": "Feedback Submitted Successfully!",
        "data": feedback
    }