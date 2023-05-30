from elevenlabs import set_api_key, get_api_key, voices
import os
import tempfile
from fastapi import APIRouter
from dotenv import load_dotenv
import requests

load_dotenv()
set_api_key(os.getenv("ELEVENLABS_API_KEY"))

router = APIRouter(
    prefix="/tts",
    tags=["text-to-speech"],
)

voice_ids = {
    "Rachel": "21m00Tcm4TlvDq8ikWAM",  # Rachel
    "Domi": "AZnzlk1XvdvUeBnXmlld",  # Domi
    "Bella": "EXAVITQu4vr4xnSDxMaL",  # Bella
    "Antoni": "ErXwobaYiN019PkySvjV",  # Antoni
    "Elli": "MF3mGyEYCl7XYWbV9V6O",  # Elli
    "Josh": "TxGEqnHWrfWFTfGW9XjX",  # Josh
    "Arnold": "VR6AewLTigWG4xSOukaG",  # Arnold
    "Adam": "pNInz6obpgDQGcFmaJgB",  # Adam
    "Sam": "yoZ06aMxZJJ28mfd3POQ",  # Sam
    "Midudev": "jwFrUxxY6tVy1pMGyASd",  # Midudev
}

CHUNK_SIZE = 1024


@router.post("/generate/")
def generate_tts(text_prompt):
    print(voices())
    voice_id = voice_ids["Midudev"]
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": get_api_key(),
    }
    data = {
        "text": f"{text_prompt}",
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.9, "similarity_boost": 0.9},
    }

    response = requests.post(url, json=data, headers=headers)

    # Save audio data to a temporary file
    with open("output.mp3", "wb") as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
        f.flush()
