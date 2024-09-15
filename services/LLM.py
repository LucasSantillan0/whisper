import requests

from chat.Chat import Chat


class LLM:
    @classmethod
    def call (cls:'LLM') -> str:
         payload = {
				 "messages":Chat.messages,
				 "stream":"false",
        		 "max_tokens":"-1"}
         post = requests.post('http://192.168.1.99:1234/v1/chat/completions',json=payload ,timeout=100000)
         response = post.json()["choices"][0]["message"]["content"]
         return response