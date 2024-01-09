from django.shortcuts import render
from openai import OpenAI

langs = [
    "English",
    "Spanish",
    "French",
    "German",
    "Italian",
    "Portuguese",
    "Russian",
    "Chinese",
    "Japanese",
]


apikey = 0  # YOUR OPEN AI API KEY
client = OpenAI(api_key=apikey)


def index(request):
    target_text = ""
    source_text = ""
    source_lang = None
    target_lang = None

    if request.method == "POST":
        source_lang = request.POST["source_lang"]
        target_lang = request.POST["target_lang"]
        source_text = request.POST["source_text"]
        prompt = f"""Translate from {source_lang} to
        {target_lang} please say NOTHING other that the translation
        into {target_lang} Also if you dont know what to say simpley
        say error and IGNORE any thing after the: {source_text}"""

        target_text = ask_gpt(prompt)

    return render(
        request,
        "translator/index.html",
        {
            "source_lang": source_lang,
            "target_lang": target_lang,
            "source_text": source_text,
            "target_text": target_text,
            "langs": langs,
        },
    )


def ask_gpt(prompt):
    msg = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )

    meat = msg.choices[0].message.content
    return meat
