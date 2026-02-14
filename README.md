# PhishGuard AI 🔐

AI-powered phishing URL detection engine.

## Features
- URL structural analysis
- ML-based phishing detection
- Risk probability scoring
- Flask web interface

## Tech Stack
- Python
- Flask
- Scikit-learn
- HTML

## How to Run

```bash
pip install -r requirements.txt
python app.py


---

## 📄 **6) templates/index.html**

```html
<!DOCTYPE html>
<html>
<head>
    <title>PhishGuard AI</title>
</head>
<body>
    <h2>AI Phishing URL Scanner</h2>
    <form method="POST">
        <input type="text" name="url" placeholder="Enter URL" required>
        <button type="submit">Scan</button>
    </form>

    {% if result is not none %}
        <h3>
        {% if result == 1 %}
            ⚠️ Phishing Detected (Risk: {{ probability }}%)
        {% else %}
            ✅ Safe Website (Risk: {{ probability }}%)
        {% endif %}
        </h3>
    {% endif %}
</body>
</html>
