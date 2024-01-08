from django.shortcuts import render

langs = [
        "Spanish",
        "English",
        "French",
        "German",
        "Italian",
        "Portuguese",
        "Russian",
        "Chinese",
        "Japanese",
        ]


def index(request):
    if request.method == "POST":
        source_lang = request.POST["source_lang"]
        target_lang = request.POST["target_lang"]
        source_text = request.POST["source_text"]
        print(source_lang, target_lang, source_text)

    return render(request, "translator/index.html", {
        "source_lang": None,
        "target_lang": None,
        "source_text": None,
        "target_text": None,
        "langs": langs,
        })
