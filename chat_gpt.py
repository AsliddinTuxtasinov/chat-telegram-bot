import openai

openai.api_key = "<your_openai_api_key>"


def chat_gpt(input_text, model_engine="text-davinci-003"):
    if input_text is None or "":
        return "please, input text"

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=input_text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=None

    )

    res = completion.choices[0].text
    return res
