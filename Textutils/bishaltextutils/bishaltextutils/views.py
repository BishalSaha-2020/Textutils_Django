#from  django.http import  HttpResponse

#def index(request):
  #  return HttpResponse('''<h1>Hello Bro</h1> <a href="https://www.youtube.com/">BishalAmazon </a>''')

from django.http import HttpResponse
from django.shortcuts import render

# Code for video 7

def index(request):
   # return HttpResponse("Home")
    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    nocaps = request.POST.get('nocaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    try:
        if removepunc == "on":
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
            params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
           # return render(request, 'analyze.html', params)
            djtext=analyzed

        if(fullcaps=="on"):
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()

            params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
            # Analyze the text
          #  return render(request, 'analyze.html', params)
            djtext = analyzed


        if(nocaps=="on"):
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.lower()

            params = {'purpose': 'Changed to LowerCas', 'analyzed_text': analyzed}
            # Analyze the text
          #  return render(request, 'analyze.html', params)
            djtext = analyzed

        if(extraspaceremover=="on"):
            analyzed = ""
            for index, char in enumerate(djtext):
                if not(djtext[index] == " " and djtext[index+1]==" "):
                    analyzed = analyzed + char

            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            # Analyze the text
            #return render(request, 'analyze.html', params)
            djtext = analyzed

        if (newlineremover == "on"):
            analyzed = ""
            for char in djtext:
                if char != "\n":
                    analyzed = analyzed + char


            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            # Analyze the text
            #return render(request, 'analyze.html', params)
            djtext = analyzed
        return render(request, 'analyze.html', params)
    except:
        return render(request,'index.html')
