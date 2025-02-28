import json
import time

def pretty_print(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))

def retry_request(func, max_retries=3, delay=2):
    """Retries a request in case of failure."""
    for _ in range(max_retries):
        try:
            return func()
        except Exception as e:
            print(f"Retrying due to error: {e}")
            time.sleep(delay)
    raise Exception("Max retries reached")