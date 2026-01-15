import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch.nn.functional as F

model_id = "meta-llama/Llama-2-7b-chat-hf"  # Replace with your local path if needed
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, dtype=torch.float16, device_map="mps")

prompt = "Yo what's up, how are you"

# 1. Forward pass for input tokens to find log probability
inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=True).to(model.device)

with torch.no_grad():
    outputs = model(**inputs)

    # Chop off the first for input and last for output(next token prediction)
    input_logits = outputs.logits[:, :-1, :]
    input_labels = inputs.input_ids[:, 1:]
    
    # Calculate log_softmax and extract the logprobs for actual tokens
    input_logprobs = F.log_softmax(input_logits, dim=-1)
    input_token_logprobs = torch.gather(input_logprobs, index=input_labels.unsqueeze(-1), dim=-1).squeeze(-1)

# 2. Generate tokens and keep log probability
gen_outputs = model.generate(
    **inputs, 
    max_new_tokens=50, 
    return_dict_in_generate=True, 
    output_scores=True,
    output_logits=True,
    num_return_sequences=1,
    temperature=1
)

# Do log prob calculation
output_logits = torch.stack(gen_outputs.logits, dim=1) 
output_logprobs = F.log_softmax(output_logits, dim=-1)
output_labels = gen_outputs.sequences[:, inputs.input_ids.shape[-1]:]
output_token_logprobs = torch.gather(output_logprobs, index=output_labels.unsqueeze(-1), dim=-1).squeeze(-1)

log_probs = input_token_logprobs[0].tolist() + output_token_logprobs[0].tolist()
print(log_probs)