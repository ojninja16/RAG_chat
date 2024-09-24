import requests
import os
import base64
from dotenv import load_dotenv
load_dotenv()
class TTSService:
    def __init__(self):
        self.url = "https://api.sarvam.ai/text-to-speech"
        self.api_key = os.getenv("SARVAM_API_KEY")
        self.headers = {
            "api-subscription-key": self.api_key,
            "Content-Type": "application/json"
        }
    def generate_audio(self, text, language_code="hi-IN", speaker="meera",enable_preprocessing=True):
        payload = {
            "inputs": [text],
            "target_language_code": language_code,
            "speaker": speaker,
            "pitch": 0,
            "pace": 1,
            "loudness": 1.5,
            "speech_sample_rate": 8000,
            "enable_preprocessing": enable_preprocessing,
            "model": "bulbul:v1"
        }
        try:
            response = requests.post(self.url, json=payload, headers=self.headers)
            response.raise_for_status()
            audio_data = response.json().get('audios', [])
            return audio_data[0] if audio_data else None
        except requests.RequestException as e:
            print(f"Error generating audio: {str(e)}")
            return None

tts_service = TTSService()