from http import client
import json
from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion
from chat.Chat import Chat
from services.Spotify import SpotifyService


class LLM:
    client = None
    thread = None
    tools = None
    
    @classmethod
    def initLLM (cls):
        cls.tools = [
        {
            "type":"function",
            "function": {
                "name": "PLAY_SONG",
                "description": "",
                "strict": True,
                "parameters": {
                    "type": "object",
                    "properties": {
                    "songName": {
                        "type": "string"
                    },
                    "songUri": {
                        "type": "string"
                    }
                    },
                    "required": [
                    "songName",
                    "songUri"
                    ],
                    "additionalProperties": False
                    }
                }}
        ]
        cls.client = OpenAI()

    

        
    @classmethod
    def call (cls) -> str:
        if not cls.client:
            raise Exception("Error connecting to openai")
        post:ChatCompletion =   cls.client.chat.completions.create(
        model="gpt-4o-mini",

        messages=[*Chat.messages],
        stream=False,
        tools=cls.tools
        )   
        response = post.choices[0].message.content
        if response is not None:
            Chat.addMessage('user',response)
            
        print(f'post: {post}')
        if post.choices[0].finish_reason != 'tool_calls':
            return response
        print(response)
        tool_call = post.choices[0].message.tool_calls[0]
        if tool_call.function.name != "PLAY_SONG":
            print("function does not exist")
            return
        arguments = json.loads(tool_call.function.arguments)
        print(f'arguments: {arguments}')
        songUri = arguments['songUri']
        songName = arguments['songName']
        print(f"playing {songName} {songUri}")
        SpotifyService.playSong(songUri)
        if response == None:
            response="ok"
        return response
