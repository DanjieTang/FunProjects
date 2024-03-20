from fastapi import FastAPI, File, UploadFile, Form
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline, AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from TTS.api import TTS
from fastapi.responses import FileResponse

app = FastAPI()

# Model setting
tts_model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
stt_model_name = "openai/whisper-small"
device = "cuda" if torch.cuda.is_available() else "cpu"
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

# Instantiate models
tts_model = TTS(tts_model_name).to(device)
stt_model = AutoModelForSpeechSeq2Seq.from_pretrained(stt_model_name)
processor = AutoProcessor.from_pretrained(stt_model_name)
pipe = pipeline(
    "automatic-speech-recognition",
    model=stt_model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    device=device
)
tokenizer = AutoTokenizer.from_pretrained("NousResearch/Llama-2-13b-chat-hf")
llm_model = AutoModelForCausalLM.from_pretrained("NousResearch/Llama-2-13b-chat-hf", quantization_config=bnb_config)

@app.post("/chat_with_llm")
async def chat_with_llm(file: UploadFile = File(...), question: str = Form(...)) -> FileResponse:
    """
    Talking to large language model.

    :param file: The wav file that contains user message.
    :return: The wav file that contain llm response.
    """
    # Receive the wav file
    wav_file = await file.read()

    # Speech to text processing
    user_message = pipe(wav_file, generate_kwargs={"language": "english"})

    # # Format prompt and input to llm
    prompt = f"""You are a helpful assistant working at a hospital. You've just finished a rehabilitation session with a patient, you are asking the patient to fill out a form. Give a short reply to user's response as encouragement.
For this question: How's today's session? Did any part of your body hurt during today's session?
User responded with: I felt a little pain on my hip.
Your reply: Can you tell me more about the pain you're feeling in your hip?

For this question: How challenging was today's session?
User responded with: I feel like it is really difficult.
Your reply: It's great to see you stepping outside your comfort zone.

For this question: How motivated do you feel after today's session?
User responded with: I'm not really motivated.
Your reply: I'm sorry to hear that. Perhaps you'll enjoy tomorrow's session more.

For this question: {question}
User responded with: {user_message["text"]}
Your reply: """
    encoded_input = tokenizer(prompt, return_tensors='pt')
    encoded_input = {k: v.to(device) for k, v in encoded_input.items()}
    output = llm_model.generate(**encoded_input, max_new_tokens=512)
    llm_response = tokenizer.decode(output[0], skip_special_tokens=True)
    llm_response = llm_response[len(prompt):]
    
    # Text to speech
    tts_model.tts_to_file(
        text=llm_response,
        file_path="output.wav",
        speaker_wav="my_voice.wav",
        language="en"
    )

    return FileResponse(path="output.wav", media_type="audio/wav", filename="llm_response.wav")

    
