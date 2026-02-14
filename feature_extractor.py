import re
import tldextract
import requests
from urllib.parse import urlparse

def extract_features(url):
    features = {}

    parsed = urlparse(url)
    ext = tldextract.extract(url)

    features['url_length'] = len(url)
    features['num_dots'] = url.count('.')
    features['has_https'] = 1 if parsed.scheme == "https" else 0
    features['num_digits'] = sum(c.isdigit() for c in url)
    features['has_ip'] = 1 if re.match(r"^\d+\.\d+\.\d+\.\d+", parsed.netloc) else 0
    features['subdomain_length'] = len(ext.subdomain)

    try:
        response = requests.get(url, timeout=3)
        features['status_code'] = response.status_code
    except:
        features['status_code'] = 0

    return list(features.values())
