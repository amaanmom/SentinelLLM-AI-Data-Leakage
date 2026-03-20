from fastapi import FastAPI
import re

app = FastAPI()

# Simple secret detection patterns
SECRET_PATTERNS = [
    r"AKIA[0-9A-Z]{16}",  # AWS key
    r"sk-[a-zA-Z0-9]{40,}",  # OpenAI key
    r"(?i)password\s*[:=]\s*\S+"
]

def detect_secrets(text):
    matches = []
    for pattern in SECRET_PATTERNS:
        matches.extend(re.findall(pattern, text))
    return matches

@app.get("/")
def home():
    return {"message": "SentinelLLM API Running"}

@app.get("/analyze")
def analyze(prompt: str):
    secrets = detect_secrets(prompt)

    if secrets:
        return {
            "risk": "HIGH",
            "message": "Sensitive data detected",
            "found": secrets
        }
    else:
        return {
            "risk": "LOW",
            "message": "Safe prompt"
        }
