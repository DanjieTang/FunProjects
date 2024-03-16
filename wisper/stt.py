from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

model_id = "openai/whisper-medium"

model = AutoModelForSpeechSeq2Seq.from_pretrained(model_id)
processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
)

result = pipe("my_voice.wav", generate_kwargs={"language": "english"})

print(result)

