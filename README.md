# SentinelLLM-AI-Data-Leakage
AI-powered system to detect sensitive data leakage in LLM usage
# 🛡️ SentinelLLM — AI Data Leakage Detection for LLMs

## 🚨 Problem

As organizations adopt AI tools, employees often paste sensitive data (API keys, emails, internal information) into prompts, leading to potential data leaks and security risks.

---

## 💡 Solution

SentinelLLM is a lightweight AI system that detects sensitive data in prompts before they are sent to LLMs, helping prevent accidental data exposure.

---

## 🚀 Features

* Real-time prompt analysis
* API key & secret detection (regex-based)
* Email detection (PII)
* Name detection (basic PII recognition)
* Risk scoring system (0–100)
* Live deployed API for testing

---

## 🧠 How It Works

1. User sends a prompt
2. System scans for:

   * API keys / secrets
   * Emails
   * Names
3. Each detection contributes to a risk score
4. Final output includes:

   * Risk Score
   * Risk Level (Low / Medium / High)
   * Detected sensitive elements

---

## 🛠️ Tech Stack

* Backend: FastAPI (Python)
* NLP: Regex-based detection
* Deployment: Render

---

## 🌐 Live Demo

https://sentinelllm-ai-data-leakage.onrender.com

Try:

```
/analyze?prompt=John Doe email is john@gmail.com and key AKIAIOSFODNN7EXAMPLE
```

---

## 🧪 Example

### Input

```
John Doe email is john@gmail.com and key AKIAIOSFODNN7EXAMPLE
```

### Output

```
Risk Score: 95
Risk Level: HIGH
Detected:
- Email
- Name
- API Key
```

---

## 📈 Future Improvements

* LLM-based semantic classification
* Real-time monitoring dashboard
* Browser extension for prompt interception
* Enterprise-level alerting system

---

## 👨‍💻 Author

Amaan Momin
