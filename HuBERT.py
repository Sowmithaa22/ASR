import librosa
import torch
from transformers import HubertForCTC, AutoProcessor

audio_file=r'C:\Users\Dell\Downloads\harvard.wav'

processor= AutoProcessor.from_pretrained("facebook/hubert-large-ls960-ft")
model=HubertForCTC.from_pretrained("facebook/hubert-large-ls960-ft")

speech, rate= librosa.load(audio_file, sr=16000)

inputs= processor(speech, return_tensors='pt', sampling_rate=rate).input_values

with torch.no_grad():
    logits= model(inputs).logits
predicted_ids= torch.argmax(logits, dim=-1)

transcription= processor.batch_decode(predicted_ids)
print(transcription)