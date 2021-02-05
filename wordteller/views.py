from django.shortcuts import render
from textblob import Word
from django.contrib import messages

def index(request):
    Note = "Not Found"
    if request.method=='POST':
        text = request.POST['text']
        lower = text.lower()
        defination = Word(lower).definitions
        final = ' '.join(map(str, defination))
        if final is "":
            messages.error(request, 'Either spelling mistake or can\'t find your word')
        context = {
            "defination":final
        }
        return render(request, 'index.html',context)
    return render(request, 'index.html')
    