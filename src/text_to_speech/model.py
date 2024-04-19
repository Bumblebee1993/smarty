
# Models: 
# https://huggingface.co/coqui/XTTS-v2

# https://huggingface.co/parler-tts/parler_tts_mini_v0.1


# plain tts 
# https://pypi.org/project/TTS/
import torch
from TTS.api import TTS
import espeakng
mySpeaker = espeakng.Speaker()
mySpeaker.say('Hello, World!')



# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
OUTPUT_PATH = "../data/"
# List available 🐸TTS models
print(TTS().list_models())

# Init TTS with the target model name
tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=True).to(device)

# Run TTS
tts.tts_to_file(text="Ich bin eine Testnachricht.", file_path=OUTPUT_PATH)