from fastapi import FastAPI
import re

app = FastAPI()

# --- Patterns ---
SECRET_PATTERNS = [
    r"AKIA[0-9A-Z]{10,20}",
    r"sk-[a-zA-Z0-9]{20,}",
    r"(?i)password\s*[:=]\s*\S+"
]

EMAIL_PATTERN = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
NAME_PATTERN = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"

# --- Detection ---
def detect_secrets(text):
    matches = []
    for pattern in SECRET_PATTERNS:
        matches.extend(re.findall(pattern, text))
    return matches

def detect_emails(text):
    return re.findall(EMAIL_PATTERN, text)

def detect_names(text):
    return re.findall(NAME_PATTERN, text)

# --- Risk scoring ---
def calculate_risk(secrets, emails, names):
    score = 0
    score += len(secrets) * 40
    score += len(emails) * 25
    score += len(names) * 15
    return min(score, 100)

# --- Routes ---
@app.get("/")
def home():
    return {"message": "SentinelLLM API Running"}

@app.get("/analyze")
def analyze(prompt: str):
    secrets = detect_secrets(prompt)
    emails = detect_emails(prompt)
    names = detect_names(prompt)

    risk_score = calculate_risk(secrets, emails, names)

    if risk_score >= 70:
        level = "HIGH"
    elif risk_score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "risk_score": risk_score,
        "risk_level": level,
        "secrets_found": secrets,
        "emails_found": emails,
        "names_found": names
    }
