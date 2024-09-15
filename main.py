#! python3.7
import os
import argparse
import numpy as np
import speech_recognition as sr
import faster_whisper

from behaviors.General import GeneralBehavior

model_size = "large-v3"

import torch
import requests
import pyttsx3
from datetime import datetime, timedelta
from queue import Queue
from time import sleep
from sys import platform
from mic_control import mute_mic, unmute_mic
from utils.ignore_hashtags import ignoreHasthags

engine = pyttsx3.init()
engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0")
engine.setProperty("rate",125)

messages = [{"role":"system", "content":"Siempre contestaré en español. Mi nombre es pepeue"},]

def main():
    unmute_mic()
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="tiny", help="Model to use",
                        choices=["tiny", "base", "small", "medium", "large"])
    parser.add_argument("--non_english", action='store_true',
                        help="Don't use the english model.")
    parser.add_argument("--energy_threshold", default=1000,
                        help="Energy level for mic to  detect.", type=int)
    parser.add_argument("--record_timeout", default=2,
                        help="How real time the recording is in seconds.", type=float)
    parser.add_argument("--phrase_timeout", default=3,
                        help="How much empty space between recordings before we "
                             "consider it a new line in the transcription.", type=float)
    if 'linux' in platform:
        parser.add_argument("--default_microphone", default='pulse',
                            help="Default microphone name for SpeechRecognition. "
                                 "Run this with 'list' to view available Microphones.", type=str)
    args = parser.parse_args()

    # The last time a recording was retrieved from the queue.
    phrase_time = None
    # Thread safe Queue for passing data from the threaded recording callback.
    data_queue = Queue()
    # We use SpeechRecognizer to record our audio because it has a nice feature where it can detect when speech ends.
    recorder = sr.Recognizer()
    recorder.energy_threshold = args.energy_threshold
    # Definitely do this, dynamic energy compensation lowers the energy threshold dramatically to a point where the SpeechRecognizer never stops recording.
    recorder.dynamic_energy_threshold = False

    # Important for linux users.
    # Prevents permanent application hang and crash by using the wrong Microphone
    
    source = sr.Microphone(1,sample_rate=16000)

    # Load / Download model
    model = args.model
    if args.model != "large" and not args.non_english:
        model = model + ".en"
    audio_model = faster_whisper.WhisperModel('medium')
	
    #def record_callback(_, audio:sr.AudioData) -> None:
    #    """
    #    Threaded callback function to receive audio data when recordings finish.
    #    audio: An AudioData containing the recorded bytes.
    #    """
    #    # Grab the raw bytes and push it into the thread safe queue.
    #    data = audio.get_raw_data()
    #    data_queue.put(data)

    # Create a background thread that will pass us raw audio bytes.
    # We could do this manually but SpeechRecognizer provides a nice helper.
    # Cue the user that we're ready to go.
    print("Model loaded.\n")
    while True:
        try:
            with source:
                recorder.adjust_for_ambient_noise(source)                
                audio_trigger_data = recorder.listen(source, 500, phrase_time_limit=2000)
            now = datetime.utcnow()
            data = audio_trigger_data.get_raw_data() 
            # Pull raw recorded audio from the queue.
                # If enough time has passed between recordings, consider the phrase complete.
                # Clear the current working audio buffer to start over with the new data.
    
                # This is the last time we received new audio data from the queue.
                
                # Combine audio data from queue

                
                # Convert in-ram buffer to something the model can use directly without needing a temp file.
                # Convert data from 16 bit wide integers to floating point with a width of 32 bits.
                # Clamp the audio stream frequency to a PCM wavelength compatible default of 32768hz max.
            audio_np = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0

                # Read the transcription.
            segments, info = audio_model.transcribe(audio_np)
            text = "" 
            for segment in segments:
              text+=ignoreHasthags(segment.text)
                # If we detected a pause between recordings, add a new item to our transcription.
                # Otherwise edit the existing one.
                # Clear the console to reprint the updated transcription.
            print(text)
            if text=="":
              continue
            messages.append({ "role" : "user" , "content":text.__str__()})
            payload = {
					    "messages":messages,
						  "stream":"false",
        		 "max_tokens":"-1"
				    }
            print(payload)
            try:
                response = GeneralBehavior.respond(text.__str__())
               # post = requests.post('http://192.168.1.99:1234/v1/chat/completions',json=payload ,timeout=100000)
            
                #response = post.json()["choices"][0]["message"]["content"]
            except Exception as e:
                print("error during post",e)
                continue
          #  messages.append({ "role" : "assistant" , "content":response})
            mute_mic()
            engine.say(response)
            engine.runAndWait()
            sleep(1)
            unmute_mic()
            print("\n Por favor hable")
        except KeyboardInterrupt:
            break
        except sr.WaitTimeoutError:
          print("dont hear")
          sleep(25)


if __name__ == "__main__":
  main()