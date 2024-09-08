import requests
import json


class Discord():
    def __init__(self, webhook_url:str):
        self.webhook_url = webhook_url
    
    def send(self, message: str):
        BODY = {
            "content": message
        }
        requests.post(
            self.webhook_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(BODY)
        )

    
