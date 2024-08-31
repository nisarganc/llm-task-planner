import openai


def GPT(prompt, gpt_version, max_tokens=128, temperature=0, stop=None, logprobs=1, frequency_penalty=0):
    
    if "gpt" not in gpt_version:
        response = openai.Completion.create(model=gpt_version, 
                                            prompt=prompt, 
                                            max_tokens=max_tokens, 
                                            temperature=temperature, 
                                            stop=stop, 
                                            logprobs=logprobs, 
                                            frequency_penalty = frequency_penalty)
        
        return response, response["choices"][0]["text"].strip()
    
    else:
        response = openai.ChatCompletion.create(model=gpt_version, 
                                            messages=prompt, 
                                            max_tokens=max_tokens, 
                                            temperature=temperature, 
                                            frequency_penalty = frequency_penalty)
        
        return response, response["choices"][0]["message"]["content"].strip()